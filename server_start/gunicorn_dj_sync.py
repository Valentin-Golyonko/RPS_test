wsgi_app = "dj_config.wsgi:application"
#
command = "./venv/bin/gunicorn"
pythonpath = "."
bind = ":8000"
workers = 4
raw_env = "DJANGO_SETTINGS_MODULE=dj_config.settings"
errorlog = "./logs/gunicorn_dj_sync.log"
# max_requests = 100
