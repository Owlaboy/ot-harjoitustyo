class Calculator():

    """This class is used to calculate the basal metabolic rate of the user.
    The class recieves the user's information at initialization.a
    """

    def __init__(self, age, sex, height, weight):
        self.age = age
        self.sex = sex
        self.height = height
        self.weigth = weight

    def resting(self):
        """This function calculates the basal metabolic rate of the user.
        The function checks the sex of the user and applies the right formula accordingly.

        Returns:
            Float: The basal metabolic rate of the user
        """
        if self.sex == 0:
            return 13.397*self.weigth + 4.799*self.height - 5.677*self.age + 88.362
        return 9.247*self.weigth + 3.098*self.height - 4.330*self.age + 447.593
