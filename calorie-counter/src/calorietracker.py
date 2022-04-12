from calculator import Calculator
from personcreation import Userdata



class Calorie_Tracker():
    def __init__(self):
        self.data = Userdata()


    def initial_call(self):
        print("Welcome to the calorie tracker.")
        print("Please give us some infromation about you,")
        print("so we can calculate your base metabolic rate.")
        name = str(input("First we will require your name: "))
        age = int(input("Then your age: "))
        while True: 
            sex = int(input("Then your sex, (input 0 if you are a man, 1 if you are a woman):"))
            if sex==1 or sex==0:
                break
            print("invalid input")
            print("try again")
        height = float(input("Now, give us your height in centimeters: "))
        weight = float(input("And finally, give us your current weight in kilograms"))
        self.data.new_person(name,age,sex,height,weight)
        print("Thank you for your patience.")
        print("Now we can begin tracking your calories.")

    def calculate(self):
        data = self.data.give_user_data()
        calculator = Calculator(data[1],data[2],data[3],data[4])
        basicrate = calculator.resting()
        return basicrate

    def add_meal(self):
        what = str(input("What you ate: "))
        calories = float(input("How many calories it was: "))
        self.data.new_meal(0,what,calories)

    def add_workout(self):
        what = str(input("What you did: "))
        calories = float(input("How many calories it was: "))
        self.data.new_exercise(0,what,calories)        

    def base(self):
        print("Your current basal caloric rate is:")
        basic_rate = self.Calculate()
        print(basic_rate)
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
    tracker = Calorie_Tracker()
    tracker.Run()