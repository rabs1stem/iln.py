from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

class Reason(BaseModel):
    text: str

@app.get("/reasons")
def get_reasons():
    cursor.execute("SELECT * FROM reasons ORDER BY id DESC")
    return cursor.fetchall()

@app.post("/reasons")
def add_reason(reason: Reason):
    cursor.execute(
        "INSERT INTO reasons(text) VALUES(%s) RETURNING *",
        (reason.text,)
    )
    return cursor.fetchone()