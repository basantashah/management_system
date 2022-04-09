from tkinter import *
from tkinter import messagebox
from subprocess import call

root = Tk()
root.title("Main")
root.geometry("300x200")
global e1
global e2

def Ok():
    call(["python", "registration.py"])

Label(root, text="Welcome to Nepal Book Depot", font="18", bg="purple").place(x=50, y=10)
Button(root, text="Old Customer", command=Ok, height= 3, width= 12, bg="light blue").place(x=100,y=50)



Button(root, text="New Customer", command=Ok, height= 3, width= 12, bg="light blue").place(x=100,y=120)


root.mainloop()