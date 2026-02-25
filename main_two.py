#-------
import time
import sys

from welcomeToShop import shop
from recipe import change
from recipe import price
from enter import enter1
from enter import startday
#-------
#-------
ingredients = {
    "Lemons": 0,
    "Sugar": 0,
    "Cups": 0, 
    "Ice": 0,
}
#-------
money = 200
day = 1
#-------
LemonSet = 0

def game(LemonSet,money,ingredients):
    what = input("What would you like to do? (1) Shop, (2) change recipe, (3) Change pricing, (4) Start the day.\n")
    #-------
    if what == "1":
        enter1(money,ingredients,shop)
    elif what == "2":
        print("You chose to change your recipe")
        price(money)
    elif what == "3":
        print("You chose to change your lemonade recipe")
        LemonSet = int(input("What would you like to set your lemonade price to?\n "))
        if LemonSet <= .01:
            print(f"You set your lemonade price to {LemonSet}!")
        elif LemonSet <= 0:
            print("Please try again...")
            what()
        elif TypeError:
            print("Please try again...")
            what()
        else:
            print("Please try again...")
            what()    
        
    elif what == "4":
        startday()
    else:
        print("Please try again")
        game(money,ingredients)