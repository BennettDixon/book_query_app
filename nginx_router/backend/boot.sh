#!/bin/bash

# wait for Postgres to start
function postgres_ready(){
python << END
import sys
import psycopg2
import os
try:
    conn = psycopg2.connect(dbname=os.environ.get("PGDATABASE"), user=os.environ.get("PGUSER"), password=os.environ.get("PGPASSWORD"), host=os.environ.get("PGHOST"))
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

python manage.py runserver 0.0.0.0:5005