import sys

from tkinter import *

def callhi():

    mytext = myString.get()
    hilabel = Label(myGUI,text=mytext,fg='blue',font=('Helvetica', 32)).grid(row=3,column=1)
    return

myGUI = Tk()
myGUI.geometry('400x400+100+100')
myGUI.title('Hello World!')

myString = StringVar()

mylabel = Label(myGUI,text="Hi, I am Label",font=('Helvetica', 48)).grid(row=0,column=1)

myEntry = Entry(myGUI,textvariable=myString).grid(row=1,column=1)

helloButton = Button(myGUI,text="Hi",command=callhi).grid(row=2,column=0)
quitButton = Button(myGUI,text="Quit",command=quit).grid(row=2,column=1)


myGUI.mainloop()


