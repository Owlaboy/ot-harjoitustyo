import sqlite3
from datetime import date


class Userdata():
    '''
    This class creates a database to save user data.
    The initializatoin of the class checks if a database file exists,
    if it doesn't exist a new file is created.
    When a new file is created the class creates three tablse.
        A table for the user's personal data.
        A table to save the user's meals.
        A table to save the user's exercises.
    The class provides methods for inputting data into the data base.'''

    def __init__(self):
        try:
            with open("user.db") as test:
                pass
        except IOError:
            with open("user.db", "w") as test:
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
        """This fuction saves the user's personal data into the database.

        Args:
            name (str): The name of the user.
            age (int): The age of the user.
            sex (int): The sex of the user.
            Sex is saved in a binary form where 0 is a male user and 1 is a female user.
            height (float): The heigth of the user.
            weight (float): The weight of the user.
        """
        self.data_base.isolation_level = None
        self.data_base.execute(
            f"insert into User (name,age,sex,height,weight) values ('{name}',{age},{sex},{height},{weight})")  # pylint: disable=line-too-long

    def new_meal(self, day, description, calories):
        """This fuction saves a new meal into the data base.

        Args:
            day (str): The date of the meal
            description (str): A description of the meal
            calories (float): An estimate of how many calories the food was
        """
        self.data_base.isolation_level = None
        self.data_base.execute(
            f"insert into Meals (date,description,calories) values ('{day}','{description}','{calories}')")  # pylint: disable=line-too-long

    def new_exercise(self, day, description, calories):
        """This fuction creates a new exercise into the data base.

        Args:
            day (str): The date of the exercise
            description (str): A description of the exercise
            calories (float): An estimate of how many calories the exercise burned
        """
        self.data_base.isolation_level = None
        self.data_base.execute(
            f"insert into Exercises (date,description,calories) values ('{day}','{description}','{calories}')")  # pylint: disable=line-too-long

    def give_user_data(self):
        """This function returns a tuple with the user's personal data

        Returns:
            Tuple: A tuple with the user's: name, age, sex, height, weight
        """
        data = self.data_base.execute("select * from User").fetchone()
        return data

    def give_calories(self, day):
        """This function returns the calories that have been eaten on a given day

        Args:
            day (str): The day from which data is wanted

        Returns:
            Float: Calories consmed on the date of inquiry
        """
        data = self.data_base.execute(
            f"select sum(calories) from Meals where date = '{day}'").fetchall()
        if data[0][0] is None:
            return 0
        return data[0][0]

    def give_todays_calories(self):
        """The function returns the calories that have been eaten on the day of the function call.

        Returns:
            Float: How many calories have been consumed on the day of inquiry
        """
        today = date.today().strftime("%Y-%m-%d")
        return self.give_calories(today)

    def calories_bruned(self, day):
        """The function returns how many calories have been burned on a given day

        Args:
            day (str): The day from which data is wanted

        Returns:
            Float: How many calories were burned on the date of inqury
        """
        data = self.data_base.execute(
            f"select sum(calories) from Exercises where date = '{day}'").fetchall()
        if data[0][0] is None:
            return 0
        return data[0][0]

    def calories_burned_today(self):
        """The function returns how many calories were burned on the day of the function call

        Returns:
            Float: How many calories have been burned on the day of the function call
        """
        today = date.today().strftime("%Y-%m-%d")
        return self.calories_bruned(today)
