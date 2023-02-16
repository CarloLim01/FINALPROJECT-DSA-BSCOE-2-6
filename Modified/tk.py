#Import all the necessary libraries
from tkinter import *
#Define the tkinter instance
interface= Tk()
interface.title("Rounded Button")

#Define the size of the tkinter frame
interface.geometry("500x300")
interface.resizable(False, False)
interface.configure(bg='#40444B')

#Define the working of the button

btn_inactive =PhotoImage(file='start_normal_small.png')
btn_active =PhotoImage(file='start_white_small.png')

def nextpage():
   interface.destroy()
   import main

def on_enter(e):
    button.config(image=btn_active)

def on_leave(e):
    button.config(image=btn_inactive)

#Create a Button
button= Button(interface, image=btn_inactive, bg='#40444B',relief='sunken',activebackground='#40444B', bd=0, command=nextpage)
button.pack(pady=114, padx=173)

#Bind the Enter and Leave Events to the Button
button.bind('<Enter>', on_enter)
button.bind('<Leave>', on_leave)

interface.mainloop()
