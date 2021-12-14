#This is the calculator window which allows the user to do currency conversions

#Imports required modules
import tkinter as tk
from tkinter import *

def calwindow():
    #Setting up frame
    frame = tk.Tk()
    frame.title('Calculator')
    frame.geometry('600x600')
    frame.configure(bg='white')

    #Makes a list of what you can choose from in the dropdown box
    options = ['EUR','JPY','AUD','USD','CAD']

    #Making instruction label 
    infolabel = tk.Label(text='Please enter the amount you wish to convert',bg='white')
    infolabel.place(relx=0.5, rely=0.2, anchor= N)

    #Makes the first dropdown box 
    clicked1 = StringVar()
    clicked1.set('USD')
    drop1 = OptionMenu(frame,clicked1,*options)
    drop1.place(relx=0.5, rely=0.3, anchor='ne')

    #Makes the second dropdown box
    clicked2 = StringVar()
    clicked2.set('JPY')
    drop2 = OptionMenu(frame,clicked2,*options)
    drop2.place(relx=0.5, rely=0.3, anchor='nw')

    #Making the input box
    entrybox = tk.Entry(frame,bg = '#A8F2FC')
    entrybox.place(relx = 0.5, rely = 0.25, anchor = N)

    def convertclick():
        intcheck = True
        #Gets the inputed text and checks to see if it is a number
        num2con = entrybox.get()
        try:
            check = int(num2con)
        except ValueError:
            intcheck = False
        #If not a number it prints a error
        if intcheck == False:
            infolabel.config(text='Invalid Input: Please only enter integers with no spaces')
    
        #If it is a valid number, gets selected currencies and converts it 
        if intcheck == True:
           import module1
           mycur = clicked1.get()
           wantcur = clicked2.get()
           curamount = int(num2con)
           if curamount > 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
               infolabel.config(text='Invalid Input: Number too large')
           else:
               convertednum = module1.calculate.conversion(mycur,wantcur,curamount)
               #Making it strings post conversion to be displayed
               convnum_str = str(convertednum)
               curamount_str = str(curamount)
               output = ('Conversion Complete:',curamount_str,mycur,'is',convnum_str,wantcur)
               #Changes label to display the conversion
               infolabel.config(text=output)

    #Making button you press to convert the selected options 
    convertButton = tk.Button(frame,bd=4,bg='#A8F2FC',text='Convert',height=1,width=7,command=convertclick)
    convertButton.place(relx=0.5,rely=0.4,anchor=CENTER)
    
    #Function for the back button
    def backfunction():
        frame.destroy()
        import CurrencyCalculator
        CurrencyCalculator.mainscreen()

    #Button to go back to main screen
    backButton = tk.Button(frame,bg = '#A8F2FC',text = 'Go Back',height = 1, width = 6,command=backfunction)
    backButton.place(relx = 0.5, rely = 0.5, anchor = S)

    frame.mainloop()
