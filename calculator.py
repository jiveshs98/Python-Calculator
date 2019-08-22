# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:48:50 2019

@author: Jivesh singh
"""

from tkinter import *

expression = "" # globally declare the expression variable 
h = 3
w = 10

def press(num): 
    # point out the global expression variable 
    global expression 

    # concatenation of string 
    expression = expression + str(num) 

    # update the expression by using set method 
    equation.set(expression)


# Function to evaluate the final expression 
def equalpress():

    try: 

        global expression 

        total = str(eval(expression)) 

        equation.set(total)

        expression = "" 

    except: 

        equation.set(" error ") 
        expression = ""


def clear(): 
    global expression 
    expression = "" 
    equation.set("")


root = Tk()

# set the title of GUI window 
root.title("Simple Calculator")

# set the configuration of GUI window 
root.geometry("545x270")
gui = Frame(root)
gui.grid()

# StringVar() is the variable class 
# we create an instance of this class 
equation = StringVar()

# create the text entry box for 
# showing the expression . 
expression_field = Entry(gui, textvariable=equation, font = ('times',30,'bold'))

expression_field.grid(columnspan=4,rowspan = 1, ipadx=70)

equation.set('enter your expression') 

button1 = Button(gui, text=' 1 ', command=lambda: press(1), height=h, width=w) 
button1.grid(row=3, column=0,sticky = E+W)

button2 = Button(gui, text=' 2 ',command=lambda: press(2), height=h, width=w) 
button2.grid(row=3, column=1,sticky = E+W)

button3 = Button(gui, text=' 3 ', command=lambda: press(3), height=h, width=w) 
button3.grid(row=3, column=2,sticky = E+W)

button4 = Button(gui, text=' 4 ', command=lambda: press(4), height=h, width=w) 
button4.grid(row=4, column=0,sticky = E+W)

button5 = Button(gui, text=' 5 ', command=lambda: press(5), height=h, width=w) 
button5.grid(row=4, column=1,sticky = E+W)

button6 = Button(gui, text=' 6 ', command=lambda: press(6), height=h, width=w) 
button6.grid(row=4, column=2,sticky = E+W)

button7 = Button(gui, text=' 7 ', command=lambda: press(7), height=h, width=w) 
button7.grid(row=5, column=0,sticky = E+W)

button8 = Button(gui, text=' 8 ', command=lambda: press(8), height=h, width=w) 
button8.grid(row=5, column=1,sticky = E+W)

button9 = Button(gui, text=' 9 ',command=lambda: press(9), height=h, width=w) 
button9.grid(row=5, column=2,sticky = E+W)

button0 = Button(gui, text=' 0 ', command=lambda: press(0), height=h, width=w) 
button0.grid(row=6, column=0,sticky = E+W)

plus = Button(gui, text=' + ', command=lambda: press("+"), height=h, width=w) 
plus.grid(row=3, column=3,sticky = E+W)

minus = Button(gui, text=' - ', command=lambda: press("-"), height=h, width=w) 
minus.grid(row=4, column=3,sticky = E+W)

multiply = Button(gui, text=' * ', command=lambda: press("*"), height=h, width=w) 
multiply.grid(row=5, column=3,sticky = E+W)

divide = Button(gui, text=' / ', command=lambda: press("/"), height=h, width=w) 
divide.grid(row=6, column=3,sticky = E+W)

equal = Button(gui, text=' = ', command=equalpress, height=h, width=w) 
equal.grid(row=6, column=2,sticky = E+W)

clear = Button(gui, text='Clear', command=clear, height=h, width=w) 
clear.grid(row=6, column='1',sticky = E+W)

mainloop()

