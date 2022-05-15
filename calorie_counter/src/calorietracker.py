from datetime import date
from calculator import Calculator
from userdata import Userdata


class Calorietracker():
    def __init__(self):
        self.data = Userdata()

    def value_input(self, datatype, text):
        """This method is used to ask data from the user.
        It checks if the inputted data type is valid,
        and forces the user to try again if the input is invalid.

        Args:
            datatype (str): Defines the data type that is beign asked for.
            text (str): The text that is shown with the input query.

        Returns:
            int, float or str: depending on the function call the function returns
            an integer, a float number or a string.
        """
        if datatype == "int":
            while True:
                try:
                    value = int(input(text))
                except ValueError:
                    print("Invalid input, try again.")
                else:
                    break
        if datatype == "float":
            while True:
                try:
                    value = float(input(text))
                except ValueError:
                    print("Invalid input, try again.")
                else:
                    break
        if datatype == "str":
            value = str(input(text))
        return value

    def initial_call(self):
        """This is a function which is run at the intial call of the application.
        The initial call is used to get the personal information of the user.
        The method also initiates the tables inside the database.
        """
        self.data.initiation()
        print("Welcome to the calorie tracker.")
        print("Please give us some infromation about you,")
        print("so we can calculate your base metabolic rate.")
        name = str(input("First we will require your name: "))

        age = self.value_input("int", "Then your age: ")

        while True:
            sex = int(
                input("Then your sex, (input 0 if you are a man, 1 if you are a woman): "))
            if sex in (1, 0):
                break
            print("invalid input")
            print("try again")

        height = self.value_input(
            "float", "Now, give us your height in centimeters: ")
        weight = self.value_input(
            "float", "And finally, give us your current weight in kilograms: ")

        self.data.new_person(name, age, sex, height, weight)
        print("Thank you for your patience.")
        print("Now you can start the main application.")

    def calculate(self):
        """This function is used to call the Calculator class.
        The function calculates an estimate of how many calories the user has burned today

        Returns:
            Float: How many calories the user has burned/will burn today
        """
        data = self.data.give_user_data()
        calculator = Calculator(float(data[1]), float(
            data[2]), float(data[3]), float(data[4]))
        calories_needed = calculator.resting() + self.data.calories_burned_today()
        return calories_needed

    def add_meal(self):
        """This function is used to log a new meal into database.
        """
        today = date.today().strftime("%Y-%m-%d")
        what = self.value_input("str", "What you ate: ")
        calories = self.value_input("float", "How many calories it was: ")
        self.data.new_meal(today, what, calories)

    def add_workout(self):
        """This funciton is used to log a new workout into the database.
        """
        today = date.today().strftime("%Y-%m-%d")
        what = self.value_input("str", "What you did: ")
        calories = self.value_input("float", "How many calories it was: ")
        self.data.new_exercise(today, what, calories)

    def base(self):
        """This function is the basic cycle of the program,
        The funciton displays the user's consumed calories and burned calories.
        The function provides options of action for the user to add a meal, a workout or
        to exit the program entirely.

        Returns:
            Bool: The function returns a boolean value to the calling function,
            to know when to end the program.
        """
        print(
            f"You have consumed {self.data.give_todays_calories():.2f} calories today.")
        basic_rate = self.calculate()
        print(f"You have burned {basic_rate:.2f} calories today.")
        print("To add a meal input: 1")
        print("To add a workout input: 2")
        print("To exit the program input: 0")
        while True:
            choice = self.value_input("int", "Input: ")
            if choice in (0, 1, 2):
                break
            print("Invalid input, try again")

        if choice == 0:
            return False
        if choice == 1:
            self.add_meal()
            return True
        if choice == 2:
            self.add_workout()
            return True

    def Run(self):
        """This function is used to call the program.
        It checks if the program needs to complete an inital call to create a new database file.
        After checking for a database the function runs infinitely until the program cycle ends.
        """
        print(f"Hello, {self.data.give_user_data()[0]}")
        while True:
            if not self.base():
                break


if __name__ == "__main__":
    tracker = Calorietracker()
    tracker.Run()
