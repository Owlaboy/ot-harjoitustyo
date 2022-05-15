import unittest
import os
from userdata import Userdata
from datetime import date


class TestUserdata(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("user.db")
        except:
            pass
        self.userdata = Userdata()
        self.userdata.initiation()

    def test_personal_data(self):
        self.userdata.new_person("Pekka",50,0,200,100)

        data = self.userdata.give_user_data()
        self.assertEqual(data,("Pekka",50,0,200,100))

    def test_calorie_return_1(self):
        self.userdata.new_meal(0, "chicken", 800)
        self.userdata.new_meal(0, "beef", 1600)

        self.assertEqual(self.userdata.give_calories(0), 2400)

    def test_calorie_return_2(self):
        self.userdata.new_meal(1, "chicken", 800)
        self.userdata.new_meal(1, "beef", 1000)

        self.assertEqual(self.userdata.give_calories(1), 1800)

    def test_todays_calories_initially(self):
        self.assertEqual(self.userdata.give_todays_calories(), 0)

    def test_todays_bruned_calories_initially(self):
        self.assertEqual(self.userdata.calories_burned_today(), 0)

    def test_todays_calories_with_food(self):
        today = date.today().strftime("%Y-%m-%d")
        self.userdata.new_meal(today, "chicken", 800)
        self.userdata.new_meal(today, "chicken", 800)
        self.assertEqual(self.userdata.give_todays_calories(), 1600)

    def test_todays_burned_calories(self):
        today = date.today().strftime("%Y-%m-%d")

        self.userdata.new_exercise(today, "full body", 500)
        burned = self.userdata.calories_burned_today()
        self.assertEqual(burned, 500)
