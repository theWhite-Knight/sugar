import time
import sys

#-------
from welcomeToShop import shop as S
from ToDoList import todo
# Global variables accessible across modules
money = 200
day = 1

LemonSet = []

# For Recipe, A list turns to this (Dictionary) 

Usage = {}

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
p = input("Would you like to play the game? (Y/N)\n")
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
            LemonSet = float(input("What would you like to set your Lemonade price to?\n   (Note: You can change this later, and add decimals to the hundreths place)\n"))

            if LemonSet.isdigit():
                print(f"You have {money} Money. \nYour Inventory contains of {ingredients}. \nYou are on Day {day}. \nYour Recipe consists of {Usage}.\n")
                print(f"The price of your Lemonade is {LemonSet}")

                print("NOTE: You cannot start the sales day if your Lemonade Price equals 0, and if your Recipe doesn't have Lemons, Cups, Ice, and Sugar with a set amount of each\n")
                print(">>>")
                print(">>>")
                print("-----------------------------------------------------------------------------------------------------------------")
                what = input("What would you like to do? (1) Shop, (2) change recipe, (3) Change pricing, (4) Start the day, (5) Quit.\n")
                #-------
                if what == "TODO":
                    todo()
                
                elif what == "1":
                    def enterShop():
                        # Access global variables from main_one
                        print("--------------------------------------------------")
                        enter = input("Would you like to enter the shop? (Y/N):\n")
                        if enter.lower() == "y":
                            print("Entering shop...")
                            # Update global variables before each shop call
                            print(f"\nYou have {ingredients}.")
                            print(">>>")
                            print(f"You have ${money:.2f} dollars.")
                            # Set globals in welcomeToShop module before calling shop

                            
                            
                            S()

                        elif enter.lower() == "n":
                            print("Cancelling...")

                        else:
                            print("Invalid input...")
                    if what == "1":
                        enterShop()   
                        #-------
                    # --------
                elif what == "2":
                    print("--------------------------------------------------")
                    print("You chose to change your recipe") # Recipe

                    def price():
                        global Usage
                        recipe_items = []
                        while True:
                            item = input("What would you like to add to your recipe? (Type STOP to Stop)\n")
                            amount = input("How much would you like to add?\n")
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
                    

                elif what == "4":
                    #-------
                    def startday():
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
                credit_roll = input("Would you like to roll Credits?\n")

                if credit_roll.lower() in ("y", "yes", "ok", "okay", "sure"):
                    print("Now rolling Credits...")
                    sys.sleep(0.75)
                    print("Front End...")
                    sys.sleep(0.75)
                    print("Jet")
                    sys.sleep(0.75)
                    print("Alexandra")
                    sys.sleep(0.75)
                    print("Back End...")
                    sys.sleep(0.75)
                    print("Dillan")
                    sys.sleep(0.75)
                    print("Evaristo")
                    sys.sleep(0.75)
                    print("Testers...")
                    sys.sleep(0.75)
                    print("Tristan")
                    sys.sleep(0.75)
                    print("Evaristo")
                    sys.sleep(0.75)
                    print("The End!")
                    sys.sleep(0.75)
                    print("Thanks for Playing!")
                    sys.exit()
                
                if credit_roll.lower() in ("no", "n"):
                    print("Okay, Thanks for Playing!")
                    sys.sleep(0.75)
                    sys.exit()

            if not LemonSet.isdigit():
                print("Please try again!")
                game_run = True
                while True:
                    game()
                    game_run = False


    game_run = True
    while True:
        game()
        game_run = False
        



elif p.lower() == "n":
    print("Exiting...")
    sys.exit()

else:
    print("Invalid input. Exiting...")
    sys.exit()


