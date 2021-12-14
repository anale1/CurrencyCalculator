#This is the "?" button page to show information about the program and link the user to the user manual

#Imports required modules
import tkinter as tk
from tkinter import *
import webbrowser

def helpwindow():
    
    #Function to open user manual
    def openlink():
        webbrowser.open('https://docs.google.com/document/d/1ThAQ4r8OOQwJU5CPaC9eKaiL-kK4fGoJU4wAZ7PImjY/edit?usp=sharing')

    #Setting up frame
    frame = tk.Tk()
    frame.title('Help')
    frame.geometry('750x750')
    frame.configure(bg='white')

    #Making info labels
    infolabel1 = tk.Label(frame,bd = 4,bg='white',text = 'WARNING: This program requires a internet connection to work and conversion might be slightly off due to database not updated yet')
    infolabel1.pack()
    infolabel2 = tk.Label(frame,bd = 4,bg='white',text = 'Click "Show Currencies" to show the supported currencies.')
    infolabel2.pack()
    infolabel3 = tk.Label(frame,bd = 4,bg='white',text = 'Click "Calculator" to access the CurrencyCalculator.')
    infolabel3.pack()
    infolabel4 = tk.Label(frame,bd = 4,bg='white',text = 'Click "exit" to exit out of the program')
    infolabel4.pack()
    infolabel5 = tk.Label(frame, bd = 4,bg='white',text = 'For more information click the User Manual below')
    infolabel5.pack()

    #Creating a clickable image to make user go to user manual 
    photo = PhotoImage(file='usermanual.png')
    clickableim = tk.Button(frame,image=photo,command=openlink)
    clickableim.pack()

    #Function to go back to main screen
    def backfunction():
        frame.destroy()
        import CurrencyCalculator
        CurrencyCalculator.mainscreen()

    #Button to go back to main screen
    backButton = tk.Button(frame,bg = '#A8F2FC',text = 'Go Back',height = 1, width = 6,command=backfunction)
    backButton.pack()

    frame.mainloop()