from cgitb import text
from tkinter import *
from tkinter import font
from unicodedata import name
root=Tk()
root.geometry('700x500')
Label(root, text="Old Customer Purchase History Generator",font=("Arial", 20, "bold"), bg="sky blue", fg="Black").place(x=30, y=10)


Label(root, text="Customer Phone Number",font=("Arial", 15, "bold"), fg="Black").place(x=100, y=95)
T = Text(root, height = 2, width = 25).place(x=150, y=150)
Button(root, text="Generate QR Code",height = 2, width = 13).place(x=200, y=200)
root.mainloop()