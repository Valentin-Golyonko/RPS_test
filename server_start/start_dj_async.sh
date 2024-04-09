#!/bin/bash

touch ./logs/gunicorn_dj_async.log
sleep 0.1
gunicorn -c ./server_start/gunicorn_dj_async.py

#daphne -p 8001 dj_config.asgi:application
