import sqlite3

class userdata():
    def __init__(self):
        with open("user.db", "w") as u:
            pass
        self.db = sqlite3.connect("user.db")
        self.db.isolation_level = None

        self.db.execute("create table User (name TEXT, age INTEGER, sex INTEGER, height REAL, weight REAL)")
        self.db.execute("create table Meals (date TEXT, description TEXT, calories REAL)")
        self.db.execute("create table Exercises (date TEXT, description TEXT, calories REAL)")
    
    def NewPerson(self, name, age, sex, height, weight):
        self.db.isolation_level = None
        self.db.execute(f"insert into User (name, age, sex, height, weight) values ('{name}', {age}, {sex}, {height}, {weight})")

    def NewMeal(self, date, description, calories):
        self.db.isolation_level = None
        self.db.execute(f"insert into Meals (date, description, calories) values ('{date}', '{description}', '{calories}')")

    def NewExercise(self, date, description, calories):
        self.db.isolation_level = None
        self.db.execute(f"insert into Exercises (date, description, calories) values ('{date}', '{description}', '{calories}')")

if __name__ == "__main__":
    u = userdata()
