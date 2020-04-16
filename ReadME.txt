Broker -> Redis
Run with docker
$docker run -d -p 6379:6379 redis

Celery Worker (run on every change)
$ celery -A tasks worker --loglevel=info