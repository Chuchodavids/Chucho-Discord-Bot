import sqlite3
from datetime import date
from datetime import timedelta

con = sqlite3.connect('/home/discord/config/users.db') #todo parametize this so we can have db in a different location
cur = con.cursor()
delta = timedelta(days=30)

class sqldb:

    def check_table(self):
        cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Users'")
        if cur.fetchone()[0]==0 : 
            cur.execute("CREATE TABLE Users(ID text NOT NULL primary key, Name text, JoinedDate TEXT, MembershipExpires TEXT)")
            print("User table does not exist. Table created")
        else:
            print('Table user exists')

    def check_user(self, id):
        _id = (id,)
        cur.execute("SELECT * FROM Users WHERE ID=?", _id)
        result = cur.fetchone()
        if result:
            return True
        else:
            return False
        
    def insert(self, id, name):
        result = self.check_user(id)
        deltonio = str(date.today() + delta)
        if result: 
            new_date = (deltonio, id)
            cur.execute(" UPDATE users SET MembershipExpires=? where ID=?", new_date)
            print(f"Updated user {name} ")
        else:
            today = str(date.today())
            tup = (id, name, today, deltonio)
            cur.execute(" INSERT INTO users (ID, Name, JoinedDate, MembershipExpires) values (?, ?, ?, ?)", tup)
            print(f"inserted user {name} ")
        con.commit()

    # def check_expired(id):