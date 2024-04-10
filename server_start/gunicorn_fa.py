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


wsgi_app = "main_fast_api:app"
# worker_class = "uvicorn.workers.UvicornWorker"
worker_class = "server_start.gunicorn_fa.MyUvicornWorker"
command = "./venv/bin/gunicorn"
pythonpath = "."
bind = ":8002"
workers = 4
errorlog = "./logs/gunicorn_fa.log"
keepalive = 120
