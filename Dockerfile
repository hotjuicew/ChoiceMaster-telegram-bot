# 使用 Alpine 版本的 Python 镜像
FROM python:3.9-alpine

# 安装编译工具和依赖库以支持 SQLite
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    sqlite-dev

# 工作目录
WORKDIR /app

# 复制 requirements.txt 并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . .

# 设置环境变量
ENV API_TOKEN "<your_token>"

# 容器启动时运行的命令
CMD [ "python", "main.py" ]

# 清理缓存和依赖
RUN apk del .build-deps
