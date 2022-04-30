from tkinter import *
from calorie_counter.src.personcreation import Userdata

class Loginview():
    def __init__(self,root):
        self.root = root

        self.start = Label(self.root,text="Welcome to the calorie tracker.")
        self.start2 = Label(self.root,text="Please give us some infromation about you,")
        self.start3 = Label(self.root,text="so we can calculate your caloric consumption.")

        self.prompt_name = Label(self.root,text="What is your name?")
        self.entry_name = Entry(self.root)

        self.prompt_age = Label(self.root,text="What is your age?")
        self.entry_age = Entry(self.root)
        self.prompt_sex = Label(self.root,text="What is your sex?")
        self.entry_sex = Entry(self.root)
        self.prompt_height = Label(self.root,text="What is your height?")
        self.entry_height = Entry(self.root)
        self.prompt_weigth = Label(self.root,text="What is your weight?")
        self.entry_weigth = Entry(self.root)


        self.save_button = Button(self.root, text="Save data",command=self.save_data)

        elements = [self.start,self.start2,self.start3,self.prompt_name,self.entry_age,self.prompt_sex,self.entry_sex,self.prompt_height,self.entry_height,self.prompt_weigth,self.entry_weigth,self.save_button]

        for element in elements:
            element.pack()

        self.root.mainloop()

    def save_data(self):
        data_base = Userdata()

        name = self.entry_name.get()
        age = self.entry_age.get()
        sex = self.entry_sex.get()
        heigth = self.entry_height.get()
        weigth = self.entry_weigth.get()
        
        data_base.new_person(name,age,sex,heigth,weigth)
