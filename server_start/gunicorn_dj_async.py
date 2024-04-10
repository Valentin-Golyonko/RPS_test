from uvicorn.workers import UvicornWorker


class MyUvicornWorker(UvicornWorker):
    CONFIG_KWARGS = {
        "loop": "uvloop",  # auto | asyncio | uvloop
        "http": "httptools",  # auto | h11 | httptools
        "lifespan": "off",
        "workers": 1,
        "interface": "asgi3",  # auto | asgi3 | asgi2 | wsgi
        "reload": False,
    }


wsgi_app = "dj_config.asgi:application"
# worker_class = "uvicorn.workers.UvicornWorker"
worker_class = "server_start.gunicorn_dj_async.MyUvicornWorker"
command = "./venv/bin/gunicorn"
pythonpath = "."
bind = ":8001"
workers = 4
raw_env = "DJANGO_SETTINGS_MODULE=dj_config.settings"
errorlog = "./logs/gunicorn_dj_async.log"
keepalive = 120
