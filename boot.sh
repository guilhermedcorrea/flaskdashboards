#!/bin/sh
export FLASK_APP='app:create_app()'
gunicorn -w 4 -b 0.0.0.0:5000 "wsgi:create_app()"