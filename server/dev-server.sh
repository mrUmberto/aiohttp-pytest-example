#!/bin/sh

alembic upgrade head

adev runserver ./engine/app.py --port $PORT
