class Calculator():
    def __init__(self,age,sex,height,weight):
        self.age = age
        self.sex = sex
        self.height = height
        self.weigth = weight

    def resting(self):
        if self.sex == "male":
            return(13.397*self.weigth + 4.799*self.height - 5.677*self.age + 88.362)
        else:
            return(9.247*self.weight + 3.098*self.height - 4.330*self.age + 447.593)