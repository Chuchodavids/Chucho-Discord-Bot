import sqlite3
from datetime import date

con = sqlite3.connect('users.db')
cur = con.cursor()

class sqldb:

    def check_table(self):
        cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users'")
        if cur.fetchone()[0]==0 : 
            cur.execute("CREATE TABLE users(id text NOT NULL primary key, name text, date TEXT)")
            print("User table does not exist. Table created")
        else:
            print('Table user exists')
    def insert(self, id, name):
        _id = (id,)
        cur.execute("SELECT * FROM users WHERE id=?", _id)
        result = cur.fetchone()
        today = str(date.today())
        if result: 
            new_date = (today, id)
            cur.execute(" UPDATE users SET date=? where id=?", new_date)
            print(f"Updated user {name} with {id} date in table")
        else:
            tup = (id, name, today)
            cur.execute(" INSERT INTO users (id, name, date) values (?, ?, ?)", tup)
            print(f"inserted user {name} with {id} in table")
        con.commit()