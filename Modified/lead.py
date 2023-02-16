from tkinter import *

def main_menu():
    interface.destroy()
    import main

interface = Tk()
interface.eval('tk::PlaceWindow . center')
interface.geometry('500x700')
interface.configure(bg='#40444B')

LB= [["Micheal",['80']],["Rafael",['54']],["Justine",['50']],["Gina",['40']]]

type(Tk.frame)
interface.geometry('500x300')
interface.configure(bg='#FFFFFF')

text1 = Label(interface, text="Leader Boards", font='Avenir 40 bold', bg='#FFFFFF', fg='#40444B')
text1.place(x=20, y=20)

text2 = Label(interface, text=LB[0][0], font='montserrat 15 bold', bg='#FFFFFF', fg='#40444B')
text2.place(x=25, y=85)
text12 = Label(interface, text=LB[0][1], font='montserrat 15 bold', bg='#FFFFFF', fg='#40444B')
text12.place(x=125, y=85)

text3 = Label(interface, text=LB[1][0], font='montserrat 15 bold', bg='#FFFFFF', fg='#40444B')
text3.place(x=25, y=115)
text13 = Label(interface, text=LB[1][1], font='montserrat 15 bold', bg='#FFFFFF', fg='#40444B')
text13.place(x=125, y=115)

text4 = Label(interface, text=LB[2][0], font='montserrat 15 bold', bg='#FFFFFF', fg='#40444B')
text4.place(x=25, y=145)
text14 = Label(interface, text=LB[2][1], font='montserrat 15 bold', bg='#FFFFFF', fg='#40444B')
text14.place(x=125, y=145)

text5 = Label(interface, text=LB[3][0], font='montserrat 15 bold', bg='#FFFFFF', fg='#40444B')
text5.place(x=25, y=175)
text15 = Label(interface, text=LB[3][1], font='montserrat 15 bold', bg='#FFFFFF', fg='#40444B')
text15.place(x=125, y=175)

exit_button = Button(interface, text='EXIT', font='Avenir 8 bold', padx=10, pady=5, bg='#FFFFFF', fg='#40444B', bd=0,
                     command=main_menu)

exit_button.place(x=425, y=250)
exit_button.config(activebackground='#40444B')

interface.mainloop()
