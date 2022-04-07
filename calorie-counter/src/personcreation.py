<<<<<<< HEAD
import sqlite3

class userdata():
    def __init__(self):
        with open("user.db", "w") as u:
            pass
        self.db = sqlite3.connect("user.db")
        self.db.isolation_level = None

        self.db.execute("create table User (name TEXT, age INTEGER, sex INTEGER, height REAL, weight REAL)")
    
    def NewPerson(self, name, age, sex, height, weight):
        self.db.isolation_level = None
        self.db.execute(f"insert into User (name, age, sex, height, weight) values ('{name}', {age}, {sex}, {height}, {weight})")

if __name__ == "__main__":
    u = userdata()
=======
from sqlite3 import db

>>>>>>> bb56f654b57392dff0a2a35cfcfa814602639aa3
