import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.male = Calculator(20, 1, 180, 65)
        self.female = Calculator(25, 0, 165, 70)

    def test_age(self):
        self.assertEqual(self.male.age, 20)

    def test_male_resting(self):
        self.assertEqual(self.male.resting(), 
                         (9.247*65 + 3.098*180 - 4.330*20 + 447.593))

    def test_female_resting(self):
        self.assertEqual(self.female.resting(),
                         (13.397*70 + 4.799*165 - 5.677*25 + 88.362))
