import sqlite3

# 数据库文件路径
DB_FILE = 'database/goals.db'


# 创建目标表
def create_goals_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            goal_text TEXT,
            total_progress INTEGER,
            current_progress INTEGER
        )
    ''')
    conn.commit()
    conn.close()


# 初始化用户目标
def init_goal_db(user_id, goal_text, total_progress):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO goals (user_id, goal_text, total_progress, current_progress) VALUES (?, ?, ?, ?)',
                   (user_id, goal_text, total_progress, 0))
    conn.commit()
    conn.close()


# 设置此次完成数
def update_now_db_db(user_id, goal_text, current_progress):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('UPDATE goals SET current_progress = current_progress+? WHERE user_id = ? AND goal_text = ?',
                   (current_progress, user_id, goal_text))
    conn.commit()
    conn.close()


# 设置已经完成数
def update_already_db(user_id, goal_text, current_progress):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('UPDATE goals SET current_progress = ? WHERE user_id = ? AND goal_text = ?',
                   (current_progress, user_id, goal_text))
    conn.commit()
    conn.close()


# 获取用户所有目标
def get_goals_db(user_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT goal_text, total_progress, current_progress FROM goals WHERE user_id = ?', (user_id,))
    goals = cursor.fetchall()
    conn.close()
    return goals


# 示例代码
if __name__ == "__main__":
    # 获取用户所有目标
    user_id = 6324497448
    user_goals = get_goals_db(user_id)
    print(user_goals[0])
    print(f"已经初始化。User {user_id} Goals:")
    for goal, total_progress, current_progress in user_goals:
        print(f"Goal: {goal}, Total Progress: {total_progress}, Current Progress: {current_progress}")