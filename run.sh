#!/bin/sh

exec /usr/local/bin/gunicorn \ 
    -b 0.0.0.0:8000 \
    -w 4 \
    -k uvicorn.workers.UvicornWorker main:app \
    --chdir /app \
    --access-logfile "${ACCESS_LOG}" \
    --error-logfile "${ERROR_LOG}"