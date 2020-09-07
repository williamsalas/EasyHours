from tkinter import *
from tkcalendar import *
from datetime import datetime

"""
William Salas
9/6/20
Purpose: Designing a program to input and track hours worked, etc.
"""

# basic tkinter starter code
root = Tk()
root.title('EasyHours')
root.geometry('600x400')
file = open("text.txt", "a+")
# date data type, todays date in YYYY-MM-DD format
todayIs = datetime.date(datetime.now())

# calendar opens to the current date
cal = Calendar(root, selectmode='day', year=todayIs.year, month=todayIs.month, day=todayIs.day)
cal.pack(pady=20, fill='both', expand=True)


# to be used with a button to write to text file
def add_date():
    my_label.config(text='Selected date is: ' + cal.get_date())
    file.write(cal.get_date() + "\n")


# button when pressed grabs date of selected date in calendar
my_button = Button(root, text='Get Date', command=add_date)
my_button.pack(pady=20)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
file.close()
