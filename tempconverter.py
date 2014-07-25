from tkinter import *

def tempconverter():
    newtemp = float(temp.get())

    ftemp = (9/5)*newtemp + 32
    ctemp = (5/9)*(newtemp - 32)


    mylabel3 = Label(myGUI,text='Your temp in Celsius is: %.2f' % ctemp).grid(row=7, column=0)
    mylabel4 = Label(myGUI,text='Your temp in Fahrenheit is: %.2f' % ftemp).grid(row=8, column=0)

    return

myGUI = Tk()
myGUI.title('Temp Converter')
myGUI.geometry('600x200')

temp = StringVar()

mylabel1 = Label(myGUI, text="Welcome to Temp Converter", fg='blue').grid(row=0, column=2)

mylabel2 = Label(myGUI, text="Enter a Temperature").grid(row=1, column=0)
myentry = Entry(myGUI, textvariable=temp).grid(row=1, column=2)

mybutton = Button(myGUI, text='Convert',command=tempconverter).grid(row=3,column=0)
exitbutton = Button(myGUI, text='Exit',command=quit).grid(row=3,column=1)



myGUI.mainloop()
