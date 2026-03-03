import time
import sys
#-------
from welcomeToShop import shop
# Global variables accessible across modules
cash = 200
day = 1
#-------
LemonSet = 0
#-------
# For Recipe, A list turns to this (Dictionary) 
#-------
Usage = {}
#-------
ingredients = {
    "Lemons": 0,
    "Sugar": 0,
    "Cups": 0, 
    "Ice": 0,
}
def enterShop():
    global cash
    enter = input("Would you like to enter the shop? (Y/N):\n")
    if enter.lower() == "y":
        print("Entering shop...")
        cash = shop(cash,ingredients)
    elif enter.lower() == "n":
        print("Cancelling...")
    else:
        print("Invalid input...")

   

def startday():
    print("Starting the day!")
    print("selling...")
    time.sleep(1)
    print("selling...")
    time.sleep(1)
    print("selling...")
    time.sleep(1)
    day += 1
    print(f"Day {day} begins!")

def price():
    global Usage
    recipe_items = []
    while True:
        item = input("What would you like to add to your recipe? [lemons, sugar, ice, (exit)]\n")
        if item.lower() == "exit":
            print("Cancelling...")
        amount = input("How much would you like to add?\n")
        recipe_items.append(item + amount)
        print(f"Added: {item} ")
        Usage["recipe"] = recipe_items
        print(f"Your Item was added to you Recipe: {Usage}")
#----------------------------
def game():
    global cash
    global day, ingredients
    while True:
        what = input("What would you like to do? (1) Shop, (2) change recipe, (3) Change pricing, (4) Start the day, (5) Quit.\n")
        #-------
        if what == "1":
            enterShop() 
        elif what == "2":
            print("You chose to change your recipe") 
            # Recipe
            price()
        elif what == "3":
            print("You chose to change your lemonade price...")
            try:
                LemonSet = float(input("What would you like to set your lemonade price to?\n "))
                if LemonSet > 0.01:
                    print(f"You set your lemonade price to ${LemonSet}!")
                elif LemonSet <= 0.01:
                    print("Price must be greater than 0.01. Please try again...")
                else:
                    print("Please try again...")
            except ValueError:
                print("Please enter a valid number...")
            

        elif what == "4":
            #-------
            startday()
        elif what == "5":
            print("Thanks for playing!")
            break
        else:
            print("Please try again")
    while day >= 1:
        print("New day...")
        print("------------------------------")
        game()
        if money <= 0:
            print("You lost!")
            print("------------------")
            print("GAME OVER!")
            sys.exit()
    if day <= 7:
        print("You have survived 7 Days of Buisness")
        credit_roll = input("Would you like to roll Credits?\n")

        if credit_roll.lower() == "y" or "yes" or "ok" or "okay" or "sure":
            print("Now rolling Credits...")
        
        if credit_roll.lower() == "no" or "n":
            print("Okay, Thanks for Playing!")
            sys.exit()
    elif p.lower() == "n":
        print("Exiting...")
        sys.exit()

    else:
        print("Invalid input. Exiting...")
        sys.exit()
# NOTE: FINISH CREDITS ON THE BOTTOM OF THE CODE!!!
#-------
print("------------------------------")
print("★~ The Lemonade Stand Game ~★")
print("------------------------------")
p = input("Would you like to play the game? (Y/N)\n")
#-------

    
if p.lower() != "y":
    print("Until next time, sucker! XD")
    sys.exit()
else:
    # print("Starting game...")
    # time.sleep(1)
    # print("3...")
    # time.sleep(1)
    # print("2...")
    # time.sleep(1)
    # print("1...")
    # time.sleep(1)
    game()

#---------------------
    




