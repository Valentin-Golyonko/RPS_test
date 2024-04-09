#!/bin/bash

touch ./logs/gunicorn_fa.log
sleep 0.1
gunicorn -c ./server_start/gunicorn_fa.py
