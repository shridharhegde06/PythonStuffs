#This python module opens a youtube video at intervals of time
#opening browser window
import webbrowser
import time
#import Tkinter
#import tkMessageBox

#import ctypes
#making program to wait for given period amount of time
#print("Starting at "+ time.ctime())
for i in range(3):
 #   ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)
   # top=Tkinter.Tk()
    #top.withdraw()
    #tkMessageBox.showinfo("Break","chill ")
    time.sleep(10) #argument will is in seconds
    webbrowser.open("https://www.youtube.com/watch?v=k4yXQkG2s1E")
