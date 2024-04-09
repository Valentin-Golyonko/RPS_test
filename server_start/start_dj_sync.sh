#!/bin/bash

touch ./logs/gunicorn_dj_sync.log
sleep 0.1
gunicorn -c ./server_start/gunicorn_dj_sync.py
