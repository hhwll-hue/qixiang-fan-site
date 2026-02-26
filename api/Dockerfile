FROM python:3.12-slim

<<<<<<< HEAD
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8000
=======
# 工作目录
WORKDIR /app

# 先装依赖（利用 Docker 缓存）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 再复制代码
COPY . .

EXPOSE 8000

# 启动 FastAPI
>>>>>>> e1d1c30cb70e5af2936902b64dc0dc092868325b
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
