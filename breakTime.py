#This python module opens triggers a youtube video afte continue 2 hours of work.
import webbrowser
import time
from tkinter import *

def playVideo():
    webbrowser.open("https://www.youtube.com/watch?v=k4yXQkG2s1E")

def doNothing():
    global alertWin
    alertWin.destroy()
#How many times should program work
for i in range(5):
    time.sleep(1*60*60) #argument will is in seconds
    #creating alert window
    alertWin=Tk()
    #setting up title
    alertWin.title("Break Time Window !!")
    label1=Label(alertWin,text="Taka a break !!",fg="red").grid(row=0,column=3)
    #creating ok button and play video if ok
    ok=Button(alertWin,text="Ok",command=playVideo).grid(row=5,column=1)
    #creating cancel button and play nothing to continue to work
    notOk = Button(alertWin,text="Not Ok",command=doNothing).grid(row=5,column=5)
    alertWin.mainloop()
   
