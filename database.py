import sqlite3

db = sqlite3.connect("2048.sqlite")

cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS RECORDS (name text, score integer)")

def get_best():
    cur.execute("""
    SELECT * FROM RECORDS 
    ORDER BY score DESC
    limit 3
    """)
    return cur.fetchall()

def insert_result(name, score):
    cur.execute("INSERT INTO RECORDS VALUES (?, ?)", (name, score))
    db.commit()

print(get_best())