#!/usr/bin/env python3

import sqlite3

DATABASE='database.db'

def get_db():
    conn=sqlite3.connect(DATABASE)
    conn.row_factory=sqlite3.Row
    return conn

# Database initialization.

def init_db():
    with get_db() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS brute(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            words TEXT UNIQUE NOT NULL)''')
        conn.commit()

init_db()

# Adding content to db.

def add_word(word):
    with get_db() as conn:
        conn.execute('INSERT OR IGNORE INTO brute (words) VALUES (?)',
        (word,))
        conn.commit()

if __name__=="__main__":

    db=get_db()
    words=db.execute('SELECT * FROM brute ORDER BY id ASC').fetchall()


    password='voldemort'
    for row in words:
        guess=row['words']
        if guess==password:
            print("logged in")
            print(f"the password: {guess}")
            break
    else:
        print("login failed")
    db.close()
