#The show all currencies page which list all avaiable currencies

#importing required modules
import tkinter as tk

def curwindow():
    #Setting up frame
    frame = tk.Tk()
    frame.title('Available Currencies')
    frame.geometry('600x600')
    frame.configure(bg='white')

    #text box to show currency
    currencyav = tk.Label(frame, bd = 4, text = 'Available Currencies')
    currencyav.pack()

    #listbox to show all currencies
    lbox = tk.Listbox(frame,bg ='#A8F2FC',activestyle = 'dotbox')

    #Inserts text into listbox
    lbox.insert(1,'EUR = Euro ')
    lbox.insert(2,'JPY = Japanese Yen')
    lbox.insert(3,'AUD = Australian Dollar')
    lbox.insert(4,'USD = United States Dollar')
    lbox.insert(5,'CAD = Canadian Dollar')
    lbox.pack(padx=10,pady=10,fill=tk.BOTH,expand=True)

    #Function for the back button
    def backfunction():
        frame.destroy()
        import CurrencyCalculator
        CurrencyCalculator.mainscreen()

    #Button to go back to main screen
    backButton = tk.Button(frame,bg = '#A8F2FC',text = 'Go Back',height = 1, width = 6,command=backfunction)
    backButton.pack()

    frame.mainloop()