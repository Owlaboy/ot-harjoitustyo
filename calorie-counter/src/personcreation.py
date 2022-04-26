import sqlite3
from datetime import date


class Userdata():
    def __init__(self):
        try:
            open("user.db")
        except IOError:
            with open("user.db", "w") as iniation:
                pass
            self.data_base = sqlite3.connect("user.db")
            self.data_base.isolation_level = None

            self.data_base.execute(
                "create table User (name TEXT, age INTEGER, sex INTEGER, height REAL, weight REAL)")
            self.data_base.execute(
                "create table Meals (date TEXT, description TEXT, calories REAL)")
            self.data_base.execute(
                "create table Exercises (date TEXT, description TEXT, calories REAL)")
        else:
            self.data_base = sqlite3.connect("user.db")
            self.data_base.isolation_level = None

    def new_person(self, name, age, sex, height, weight):
        self.data_base.isolation_level = None
        self.data_base.execute(
            f"insert into User (name,age,sex,height,weight) values ('{name}',{age},{sex},{height},{weight})") # pylint: disable=line-too-long

    def new_meal(self, day, description, calories):
        self.data_base.isolation_level = None
        self.data_base.execute(
            f"insert into Meals (date,description,calories) values ('{day}','{description}','{calories}')") # pylint: disable=line-too-long

    def new_exercise(self, day, description, calories):
        self.data_base.isolation_level = None
        self.data_base.execute(
            f"insert into Exercises (date,description,calories) values ('{day}','{description}','{calories}')") # pylint: disable=line-too-long

    def give_user_data(self):
        data = self.data_base.execute("select * from User").fetchone()
        return data

    def give_calories(self, day):
        data = self.data_base.execute(
            f"select sum(calories) from Meals where date = '{day}'").fetchall()
        if data[0][0] is None:
            return 0
        return data[0][0]

    def give_todays_calories(self):
        today = date.today().strftime("%Y-%m-%d")
        return self.give_calories(today)

    def calories_bruned(self, day):
        data = self.data_base.execute(
            f"select sum(calories) from Exercises where date = '{day}'").fetchall()
        if data[0][0] is None:
            return 0
        return data[0][0]

    def calories_burned_today(self):
        today = date.today().strftime("%Y-%m-%d")
        return self.calories_bruned(today)
