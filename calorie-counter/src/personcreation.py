import sqlite3
from datetime import date


class Userdata():
    def __init__(self):
        with open("user.db", "w") as u:
            pass
        self.db = sqlite3.connect("user.db")
        self.db.isolation_level = None

        self.db.execute(
            "create table User (name TEXT, age INTEGER, sex INTEGER, height REAL, weight REAL)")
        self.db.execute(
            "create table Meals (date TEXT, description TEXT, calories REAL)")
        self.db.execute(
            "create table Exercises (date TEXT, description TEXT, calories REAL)")

    def new_person(self, name, age, sex, height, weight):
        self.db.isolation_level = None
        self.db.execute(
            f"insert into User (name, age, sex, height, weight) values ('{name}', {age}, {sex}, {height}, {weight})")

    def new_meal(self, date, description, calories):
        self.db.isolation_level = None
        self.db.execute(
            f"insert into Meals (date, description, calories) values ('{date}', '{description}', '{calories}')")

    def new_exercise(self, date, description, calories):
        self.db.isolation_level = None
        self.db.execute(
            f"insert into Exercises (date, description, calories) values ('{date}', '{description}', '{calories}')")

    def give_user_data(self):
        data = self.db.execute("select * from User").fetchone()
        return data[0]

    def give_calories(self,day):
        data = self.db.execute(f"select sum(calories) from Meals where date = '{day}'").fetchall()
        if data[0][0] == None:
            return 0
        return data[0][0]
    
    def give_todays_calories(self):
        today = date.today().strftime("%Y-%m-%d")
        return self.give_calories(today)
