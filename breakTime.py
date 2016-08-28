#This python module opens triggers a youtube video afte continue 1 hour of work.
import webbrowser
import time
import urllib.request
import random
from tkinter import *
#procedure to read the source code for the youtube page
def get_page(url):
    with urllib.request.urlopen(url) as response:
        #return html source code
        return response.read()

#checks the occurance of each link the given string
def get_next_link(page):
    #search for the string  <a href= as every link in html as <a href="www.google.com">link</a>
    startLink = page.find(b"<a href=") 
    #if link not found end 
    if startLink == -1:
        return None,0
    startQuote = page.find(b'"',startLink)
    endQuote = page.find(b'"',startQuote+1)
    url = page[startQuote+1:endQuote]
    return url,endQuote

#Procedure finds all the available links of the youtube page and filters only watchable videos
def get_all_links(page):
    while True:
        url,endpos = get_next_link(page)
        if url:
            #only get videos which can viewed eliminating channels in the page
            if url.find(b'watch') == 1:
                global playList
                playList.append(url)
            page = page[endpos: ]
        else:
            break


#Procedure to play a random video
def playVideo():
    global playList
    get_all_links(get_page("https://www.youtube.com/"))
    videoToPlay = playList[random.randint(0,len(playList))].strip().decode('utf-8')
    print(videoToPlay)
    url = "http://www.youtube.com/"+videoToPlay
    webbrowser.open(url)

def doNothing():
    global alertWin
    alertWin.destroy()

playList = []
#How many times should program work
for i in range(5):
    time.sleep(1*60*60) #argument will is in seconds
    #creating alert window
    alertWin=Tk()
    alertWin.geometry("200x200+100+10")
    #setting up title
    alertWin.title("Break Time Window !!")
    label1=Label(alertWin,text="Taka a break !!",fg="red").grid(row=0,column=3)
    #creating ok button and play video if ok
    ok=Button(alertWin,text="Ok",command=playVideo).grid(row=5,column=1)
    #creating cancel button and play nothing to continue to work
    notOk = Button(alertWin,text="Not Ok",command=doNothing).grid(row=5,column=5)
    alertWin.mainloop()
   
