from tkinter import *
root = Tk()

num = 0
bold = 0
def typeA():
    lblText.configure(text='A')

def font32():
    global num
    if bold == 0:
        lblText.configure(font=('',32))
        num += 1
    else:
        lblText.configure(font=('',32,'bold'))
        
    print(num)
    
def boldtext():
    global bold
    if num == 0:
        lblText.configure(font=('',0,'bold'))
    
    else:
        lblText.configure(font=('',32,'bold'))
        
    bold += 1

def changecolor():
    btnChangeColor.configure(bg='green')

def display(a, b):
    name = txtName.get()
    lblText.configure(text=name + '-' + a + ' ' + b)

btnTypeA = Button(text='Type A', command=typeA)
btnFont32 = Button(text='Font 32', command=font32)
btnBoldText = Button(text='Bold Text', command=boldtext)
btnChangeColor = Button(text='Change Color', command=changecolor)
lblText = Label(text='Label')

course = 'BSCS'
dept = 'CICS'
btnPress = Button(text='Press', command=lambda a=course, b=dept:display(a, b))
lblName = Label(text='Enter name:')
txtName = Entry()

lblText.grid(row=0, columnspan=4)
btnTypeA.grid(row=1, column=0)
btnFont32.grid(row=1, column=1)
btnBoldText.grid(row=1, column=2)
btnChangeColor.grid(row=1, column=3)
lblName.grid(row=2, column=0)
txtName.grid(row=2, column=1, columnspan=3)
btnPress.grid(row=3, column=0)


