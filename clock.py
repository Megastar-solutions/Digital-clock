from tkinter import Tk 
from tkinter import Label #allows users to put text on screen
import time
import sys

master = Tk()
master.title("Digital Clock")


# the function updates the time after every 200 milliseconds
def get_time():
    timeVar = time.strftime("%I:%M:%S:%p")
    clock.config(text=timeVar)
    clock.after(200, get_time)


#the background and text color formatting
     
#Label(master, font=("Arial", 30), text="Digital Clock System", fg="white", bg="black").pack() 

clock = Label(master, font=("Calibri", 90),bg="black",fg="red" )
clock.pack()
get_time()

master.mainloop() #a popup window  showing the time