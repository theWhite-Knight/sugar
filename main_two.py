
import time
import sys
from welcomeToShop import shop
from recipe_pricing import change
from recipe_pricing import price as p
from s_day import startday as s
from enter_s import o


ingredients = {
    "Lemons": 0,
    "Sugar": 0,
    "Cups": 0, 
    "Ice": 0,
}

money = 200
day = 1

def game(money,ingredients):
    what = input("What would you like to do? (1) Shop, (2) change recipe, (3) Change pricing, (4) Start the day.\n")

    if what == "1":
        o(money,ingredients,shop)
    elif what == "2":
        print("You chose to change your recipe")
        p(money)
    elif what == "3":
        print("You chose to change your lemonade recipe")
        change(money)
    elif what == "4":
        s()
    else:
        print("Please try again")
        game(money,ingredients)