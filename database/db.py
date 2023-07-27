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
def update_now_db(user_id, goal_text, current_progress):
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


# 获取用户所有内容
def get_goals_db(user_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT goal_text, total_progress, current_progress FROM goals WHERE user_id = ?', (user_id,))
    goals = cursor.fetchall()
    conn.close()
    return goals


# 获取用户的所有目标
def get_goals_text_db(user_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT goal_text FROM goals WHERE user_id = ?', (user_id,))
    goals = cursor.fetchall()
    conn.close()
    return goals


def check_goal_exists(user_id, goal_text):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM goals WHERE user_id = ? AND goal_text = ?', (user_id, goal_text))
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0


# 删除目标
def delete_goal_db(user_id, goal_text):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM goals WHERE user_id = ? AND goal_text = ?', (user_id, goal_text))
    conn.commit()
    conn.close()


# 删除一个用户的所有目标
def delete_all_goals(user_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # 使用 user_id 删除所有目标
    cursor.execute('DELETE FROM goals WHERE user_id = ?', (user_id,))

    conn.commit()
    conn.close()


# 示例代码
if __name__ == "__main__":
    # 获取用户所有目标
    user_id = 1001
    delete_all_goals(user_id)
