# 別コンテナのnginxから接続するので0.0.0.0で起動
bind = "0.0.0.0:8000"

# リクエストの長さ制限をオフにする
limit_request_line = 0

# workersの推奨値は (CPUコア数 x 2)+1、AWS Fargateは最小でも2コア使えるので5に設定
# CPU処理が多い場合、threadsを増やしても処理能力は上がらないので1
worker_class = "gthread"
workers = 5
threads = 1

# worker-tmp-dirのデフォルトは/tmpだが、/tmpはdockerのoverlayFSを通してホストのストレージに繋がるので遅い(特にEBS)
# インメモリの/dev/shmを使うように変更
worker_tmp_dir = "/dev/shm"

timeout = 360
keepalive = 360
max_requests = 500
max_requests_jitter = 200

accesslog = "-"
access_log_format = '%(p)s %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%({x-forwarded-for}i)s"'
