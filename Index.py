from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import calendar

root = tk.Tk()
root.geometry('400x300')
root.title('Calender')
  
def show():
    m = int(month.get())
    y = int(year.get())
    output = calendar.month(y, m)

    cal.insert('end', output)


def clear():
    cal.delete(1.0, 'end')


def exit():
    root.destroy()

m_label = Label(root, text="Month", font=('verdana', '10', 'bold'))
m_label.place(x=60, y=40)

month = Spinbox(root, from_=1, to=12, width="5")
month.place(x=250, y=40)

y_label = Label(root, text="Year", font=('verdana', '10', 'bold'))
y_label.place(x=500, y=40)

year = Spinbox(root, from_=2000, to=3000, width="8")
year.place(x=650, y=40)

cal = Text(root, width=40, height=30, relief=RIDGE, borderwidth=2)
cal.place(x=70, y=110)

show = Button(root,text="Show", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=4, command=show)
show.place(x=140, y=1400)

clear = Button(root, text="Clear", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=clear)
clear.place(x=440, y=1400)

exit = Button(root, text="Exit", font=('verdana', 10, 'bold'), relief=RIDGE, borderwidth=2, command=exit)
exit.place(x=740, y=1400)

root.mainloop()
