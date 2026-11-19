FROM python:3.13-slim

WORKDIR /src

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh","-c","fastapi run api/main.py --host 0.0.0.0 --port ${PORT:-8080}"]
#　$PORTを読む形にする。"0000"部分を編集
