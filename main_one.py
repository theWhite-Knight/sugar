import time
import sys

#-------
from welcomeToShop import shop as S, set_globals
from ToDoList import todo

# Global variables accessible across modules
money = 200
day = 1

LemonSet = 0

# For Recipe, A list turns to this (Dictionary) 

Usage = {}

start = True
lemon = True



ingredients = {
    "Lemons": 0,
    "Sugar": 0,
    "Cups": 0, 
    "Ice": 0,
}


# NOTE: On the What Input, if you put "TODO" it will print up our TODO list.



if money <= 0:
    print("You lost!")
    print("------------------")
    print("GAME OVER!")
    sys.exit()

#-------
print("------------------------------")
print("★~ The Lemonade Stand Game ~★")
print("------------------------------")
try:
    p = input("Would you like to play the game? (Y/N)\n")

except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()
#-------
if p.lower() in ("y", "yes", "ok", "okay", "sure"):
    print("Good Luck!")
    print("Starting game...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("--------------------------------------------------------------------------")
    
    def game():
        global day
        global money
        global ingredients
        while day <= 7:
            print("New Day...")


            try:
                LemonSet = float(input("What would you like to set your Lemonade price to?\n   (Note: You can change this later, and add decimals to the hundreths place, For example 2.99)\nNOTE: Don't add a Dollar Sign $\n"))
                ask = False

            except ValueError:
                print("Please enter a valid number!")
                continue

            except KeyboardInterrupt:
                print("\nExiting...")
                sys.exit()

            
            if isinstance(LemonSet, (int, float)) and LemonSet > 0:

                print("------------------------------------------------------------------------------------------------------------------------------------")
                print(f"You have {money} Money. \nYour Inventory contains of {ingredients}. \nYou are on Day {day}. \nYour Recipe consists of {Usage}.")
                print(f"The price of your Lemonade is ${LemonSet}\n")

                print("NOTE: You cannot start the sales day if your Lemonade Price equals 0, and if your Recipe doesn't have Lemons, Cups, Ice, and Sugar with a set amount of each\n")
                print(">>>")
                print(">>>")
                print("-----------------------------------------------------------------------------------------------------------------")
                try:
                    what = input("What would you like to do? (1) Shop, (2) change recipe, (3) Change pricing, (4) Start the day, (5) Quit.\n")

                except KeyboardInterrupt:
                    print("\nExiting...")
                    sys.exit()
                #-------
                if what == "TODO":
                    todo()
                
                elif what == "1":
                    # Access global variables from main_one
                    print("--------------------------------------------------")
                    try:
                        enter = input("Would you like to enter the shop? (Y/N):\n")

                    except KeyboardInterrupt:
                        print("\nExiting...")
                        sys.exit()
                    if enter.lower() == "y":
                        print("Entering shop...")
                        # Update global variables before each shop call
                        print(f"\nYou have {ingredients}.")
                        print(">>>")
                        print(f"You have ${money:.2f} dollars.")
                        # Set globals in welcomeToShop module before calling shop
                        set_globals(money, ingredients)
                        S()
                    elif enter.lower() == "n":
                        print("Cancelling...")
                    else:
                        print("Invalid input...")
                        #-------
                    # --------
                elif what == "2":
                    print("--------------------------------------------------")
                    print("You chose to change your recipe") # Recipe

                    def price():
                        global Usage
                        recipe_items = []
                        while True:
                            try:
                                item = input("What would you like to add to your recipe? (Type STOP to Stop)\n")

                            except KeyboardInterrupt:
                                print("\nExiting...")
                                sys.exit()
                            try:
                                if item.lower() not == "Lemons" or "Ice" or "Sugar" or "Cups":
                                    amount = input("How much would you like to add?\n")

                            except KeyboardInterrupt:
                                print("\nExiting...")
                                sys.exit()

                            if item.lower() == 'STOP':
                                break

                            recipe_items.append(item)
                            recipe_items.append(amount)
                            print(f"Added: {amount}{item} ")
                            Usage["recipe"] = recipe_items
                            print(f"Your Item was added to you Recipe: {Usage}")
                    price()

                    
                elif what == "3":
                    print("--------------------------------------------------")
                    print("You chose to change your lemonade price")
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

                    except KeyboardInterrupt:
                        print("\nExiting...")
                        sys.exit()
                    

                elif what == "4":
                    #-------
                    def startday():
                        global day
                        print("--------------------------------------------------")
                        print("Starting the day!")
                        print("selling...")
                        time.sleep(1)
                        print("selling...")
                        time.sleep(1)
                        print("selling...")
                        time.sleep(1)
                        day += 1
                        print(f"Day {day} begins!")

                    #-------

                    startday()
                elif what == "5":
                    print("Thanks for playing!")
                    break
                else:
                    print("Please try again")

        
            if day >= 7:
                print("--------------------------------------------------")
                print("You have survived 7 Days of Buisness")
                try:
                    credit_roll = input("Would you like to roll Credits?\n")
                except KeyboardInterrupt:
                    print("\nExiting...")
                    sys.exit()

                if credit_roll.lower() in ("y", "yes", "ok", "okay", "sure"):
                    print("Now rolling Credits...")
                    time.sleep(0.75)
                    print("Front End...")
                    time.sleep(0.75)
                    print("Jet")
                    time.sleep(0.75)
                    print("Alexandra")
                    time.sleep(0.75)
                    print("Back End...")
                    time.sleep(0.75)
                    print("Dillan")
                    time.sleep(0.75)
                    print("Evaristo")
                    time.sleep(0.75)
                    print("Testers...")
                    time.sleep(0.75)
                    print("Tristan")
                    time.sleep(0.75)
                    print("Evaristo")
                    time.sleep(0.75)
                    print("The End!")
                    time.sleep(0.75)
                    print("Thanks for Playing!")
                    sys.exit()
                
                if credit_roll.lower() in ("no", "n"):
                    print("Okay, Thanks for Playing!")
                    time.sleep(0.75)
                    sys.exit()

            if not (isinstance(LemonSet, (int, float)) and LemonSet > 0):
                print("Please try again!")
                continue

    if start == True:
        game()
        start = False

elif p.lower() == "n":
    print("Exiting...")
    sys.exit()

else:
    print("Invalid input. Exiting...")
    sys.exit()