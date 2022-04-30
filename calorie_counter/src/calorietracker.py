from datetime import date
from calculator import Calculator
from personcreation import Userdata

class Calorietracker():
    def __init__(self):
        self.data = Userdata()

    def initial_call(self):
        print("Welcome to the calorie tracker.")
        print("Please give us some infromation about you,")
        print("so we can calculate your base metabolic rate.")
        name = str(input("First we will require your name: "))
        age = int(input("Then your age: "))
        while True:
            sex = int(
                input("Then your sex, (input 0 if you are a man, 1 if you are a woman):"))
            if sex in (1,0):
                break
            print("invalid input")
            print("try again")
        height = float(input("Now, give us your height in centimeters: "))
        weight = float(
            input("And finally, give us your current weight in kilograms"))
        self.data.new_person(name, age, sex, height, weight)
        print("Thank you for your patience.")
        print("Now we can begin tracking your calories.")

    def calculate(self):
        data = self.data.give_user_data()
        calculator = Calculator(float(data[1]), float(data[2]), float(data[3]), float(data[4]))
        calories_needed = calculator.resting() + self.data.calories_burned_today()
        return calories_needed

    def add_meal(self):
        today = date.today().strftime("%Y-%m-%d")
        what = str(input("What you ate: "))
        calories = float(input("How many calories it was: "))
        self.data.new_meal(today, what, calories)

    def add_workout(self):
        today = date.today().strftime("%Y-%m-%d")
        what = str(input("What you did: "))
        calories = float(input("How many calories it was: "))
        self.data.new_exercise(today, what, calories)

    def base(self):
        print(f"You have consumed {self.data.give_todays_calories()} calories")
        basic_rate = self.calculate()
        print(f"You have burned {basic_rate} calories")
        print("To add a meal input: 1")
        print("To add a workout input: 2")
        print("To exit the program input: 0")
        choice = int(input("input: "))

        if choice == 0:
            return False
        if choice == 1:
            self.add_meal()
        if choice == 2:
            self.add_workout()

    def Run(self):
        self.initial_call()
        while True:
            if not self.base():
                break


if __name__ == "__main__":
    tracker = Calorietracker()
    tracker.Run()
    print(tracker.calculate())
    