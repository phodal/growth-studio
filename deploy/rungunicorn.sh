#!/bin/bash

NAME="growth-studio"
VIRTUALENVDIR=/home/phodal/py35env            
APPDIR=/home/phodal/growth-studio
SOCKFILE=/hoem/phodal/growth-studio//gunicorn.sock

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ${VIRTUALENVDIR}/bin/gunicorn ${APPDIR}/growth_studio.wsgi:application \
  --workers 2 \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=${APPDIR}/logs/log.txt