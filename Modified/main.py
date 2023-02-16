from tkinter import *


def secondpage():
    interface.destroy()
    import game


def leaderboards():
    interface.destroy()
    import lead


def exit_win():
    interface.destroy()


interface = Tk()

interface.geometry('500x300')
interface.resizable(False, False)
interface.configure(bg='#40444B')

jeo = Label(interface, text="ANACONDA", font='Montserrat 40 bold', bg='#40444B', fg='#F5F5DC')
jeo.place(x=85, y=10)

start_button = Button(interface, text='START', font='Avenir 8 bold', padx=10, pady=5, bg='#40444B', fg='#F5F5DC', bd=0,
                      command=secondpage)
start_button.place(x=220, y=105)
start_button.config(activebackground='#F5F5DC')

LB_button = Button(interface, text='Leader\nBoards', font='Avenir 10 bold', padx=13, pady=5, bg='#40444B', fg='#F5F5DC',
                   bd=0, command=leaderboards)
LB_button.place(x=213, y=140)
LB_button.config(activebackground='#F5F5DC')

exit_button = Button(interface, text='EXIT', font='Avenir 8 bold', padx=16, pady=5, bg='#40444B', fg='#F5F5DC', bd=0,
                     command=exit_win)

exit_button.place(x=220, y=200)
exit_button.config(activebackground='#F5F5DC')

interface.mainloop()
