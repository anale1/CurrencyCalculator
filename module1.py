#This module does all the conversions

#Imports required modules
import tkinter as tk
import requests

#Sets API currency data base
url = 'https://open.er-api.com/v6/latest/USD'

#Setting up API for CurrencyConverter 
class CurrencyConverter():
    def __init__(self,url):
        self.importdata = requests.get(url).json()
        self.currency = self.importdata['rates']
    #Function to convert currency
    def conversion(self,currency1,currency2,amount):
        starting_amount = amount
        #Needs to convert to USD first since the data base in using USD
        if currency1 != 'USD' :
            amount = amount / self.currency[currency1]
        amount = round(amount * self.currency[currency2], 4)
        return amount

#Gives class its URL to use
calculate = CurrencyConverter(url)


