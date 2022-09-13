FROM nginx

# アクセスログを標準出力、エラーログを標準エラー出力へ
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# ポート80を公開
EXPOSE 80

COPY nginx.conf /etc/nginx/nginx.conf
