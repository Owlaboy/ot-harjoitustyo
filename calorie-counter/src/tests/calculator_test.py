import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.male = Calculator(20, "male", 180, 65)
        self.female = Calculator(25, "female", 165, 70)

    def test_age(self):
        self.assertEqual(self.male.age, 20)
