import psycopg2
import os

conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "localhost"),
    database="iln",
    user="postgres",
    password="postgres"
)

conn.autocommit = True
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reasons (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL
)
""")