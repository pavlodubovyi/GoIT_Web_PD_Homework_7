# WARNING: This script will completely drop your database and recreate it from zero (empty)
import os
from dotenv import load_dotenv
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

load_dotenv(".env")

# Connect to the PostgreSQL server
user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
db = os.getenv('DB_NAME')
domain = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

connection = connect(
    dbname="postgres", user=user, password=password, host=domain, port=port
)

# Enable autocommit mode
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Now you can execute commands like DROP DATABASE or CREATE DATABASE
cursor = connection.cursor()
cursor.execute(f"DROP DATABASE IF EXISTS {db}")
cursor.execute(f"CREATE DATABASE {db}")
cursor.close()
connection.close()
