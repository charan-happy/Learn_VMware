import tkinter as tk
import datetime 
from PIL import Image, ImageTk

# let's create a window for our app and name it as "Age Calculation App"

windows=tk.Tk()
windows.geometry("620x780")
windows.title("Age Calculation App")


# create labels
name = tk.label(text = "Name")
name.grid(column=0,row=1)
year=tk.Label(text="Year")
name.grid(column=0,row=2)
month=tk.Label(text="Month")
name.grid(column=0,row=3)
date=tk.Label(text = "Day")
name.grid(column=0,row=4)

#using grid method to get respective user inputs

nameEntry =tk.Entry()
nameEntry.grid(column=1, row=1)
yearEntry =tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry =tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry =tk.Entry()
dateEntry.grid(column=1,row=4)

#adding functionality
def getInput():
    name=nameEntry.get()
    Human = person(name,datetime,date((int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get()))))
    textArea =tk.Text(master=window,height=15,width=30)
    textArea.grid(column=1,row=6)
    answer= "Hey {Human}!!!, You are{age} years old!!!".format(Human=name,age=Human.age())
    textArea.insert(tk.End,answer)
#creating a button

button = tk.Button(window,text="calculate Age",command=getInput,bg="pink")
button.grid(column=1,row=5)
#Defining 'person' class. Defining '_init' method and also age method which will calculate the age of the user by subsracting the user's birth date from today's date.

class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate =birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age

#adding image
image=Image.open('age-calculator.jpeg')
image.thumbnail((300,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image=tk.grid(column=1,row=0)

window.mainloop()
