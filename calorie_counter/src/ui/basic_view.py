from tkinter import *

class Basicview():
    def __init__(self, root):
        self.root = root

        bruh =2

        information_label = Label(self.root,text="Today's calorie status:")
        calorie_status = Label(self.root,text=f"{bruh} / ___",)


        add_meal = Button(self.root,text="Add meal")
        add_exercise = Button(self.root,text="Add exercise")

        information_label.grid(row=0,column=1)
        calorie_status.grid(row=1,column=1)
        add_exercise.grid(row=20,column=2)
        add_meal.grid(row=20,column=1)

        self.root.mainloop()



if __name__=="__main__":
    root = Tk()
    bruh = Basicview(root)