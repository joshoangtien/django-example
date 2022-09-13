FROM python:3.9.6-buster

# Pythonの出力バッファリングを無効化
ENV PYTHONUNBUFFERED=1

# 作業ディレクトリ作成
WORKDIR /app_example

# PyPIパッケージのインストール
COPY requirements.txt /app_example//
RUN pip install -r requirements.txt

# 必要なファイルのみコピー
COPY app_example ./app_example
COPY api_example ./api_example
COPY static ./static
# cloudfront.pem 
COPY manage.py docker/api/gunicorn.conf.py ./

# ポート8000を公開
EXPOSE 8000

# .envファイルの読み込みを無効化
ENV DJANGO_READ_ENV_FILE=False

# datadogのランナー経由でgunicornを起動
CMD ddtrace-run gunicorn api_example.wsgi
