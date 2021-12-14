#The main menu GUI file, consisting of a calculator,show currencies, and exit button

#Imports required modules
import tkinter as tk
from tkinter import *
import sys

def mainscreen():
    #Making the frame and its dimensions
    frame = tk.Tk()
    frame.title('CurrencyCalculator')
    frame.geometry('600x600')
    frame.configure(bg='white')

    #function to open Show Currencies window
    def imcurwindow():
        frame.destroy()
        import module2
        module2.curwindow()

    #Function to open Calculator window 
    def imcalwindow():
        frame.destroy()
        import module3
        module3.calwindow()

    #Function to open ? window
    def imhelpwindow():
        frame.destroy()
        import module4
        module4.helpwindow()

    #Function to close everything and exit out
    def exitprogram():
        frame.destroy()
        sys.exit()

    #CurrencyCalculator Image 
    Photo = PhotoImage(file='currencycalc.png')
    photobanner = tk.Label(frame,image=Photo)
    photobanner.pack()

    #Button that opens the calculator
    calculateButton = tk.Button(frame,bd = 4,bg = '#A8F2FC',text = 'Calculator',height = 3, width = 40,command=imcalwindow)
    calculateButton.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    #Button that shows aviable currency
    curButton = tk.Button(frame,bd = 4,bg = '#A8F2FC',text = 'Show Currencies',height = 3, width = 40,command=imcurwindow)
    curButton.place(relx = 0.5, rely = 0.3, anchor = N)

    #Button that exits the program
    exitButton = tk.Button(frame,bd = 4,bg = '#A8F2FC',text = 'Exit',height = 3, width = 40,command=exitprogram)
    exitButton.place(relx = 0.5, rely = 0.7, anchor = S)

    #Help button that will link you to the user manual
    helpButton = tk.Button(frame,bg = '#A8F2FC',text = '?',height = 1, width = 1,command=imhelpwindow)
    helpButton.place(relx = 1.0,y = 0, anchor = NE)

    frame.mainloop()

mainscreen()
