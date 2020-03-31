#!/bin/bash

.mysql/run-mysqld.sh &
PYTHONUNBUFFERED=true python3 manage.py runserver &

wait