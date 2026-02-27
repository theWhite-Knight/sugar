import time
import sys
#-------
from recipe import price

# Global variables accessible across modules
money = 200
day = 1

LemonSet = 0

ingredients = {
    "Lemons": 0,
    "Sugar": 0,
    "Cups": 0, 
    "Ice": 0,
}
#-------
print("------------------------------")
print("★~ The Lemonade Stand Game ~★")
print("------------------------------")
p = input("Would you like to play the game? (Y/N)\n")
#-------
if p.lower() == "y":
    print("Starting game...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    
    def game():
        global day
        while True:
            what = input("What would you like to do? (1) Shop, (2) change recipe, (3) Change pricing, (4) Start the day, (5) Quit.\n")
            #-------
            if what == "1":
                def enterShop():
                    # Access global variables from main_one
                    
                    enter = input("Would you like to enter the shop? (Y/N):\n")
                    if enter.lower() == "y":
                        print("Entering shop...")
                        
                        while True:
                            # Update global variables before each shop call

                            
                            print(f"\nYou have {ingredients}.")
                            print(">>>")
                            print(f"You have ${money:.2f} dollars.")
                            

                            
                            # Update local variables

                    elif enter.lower() == "n":
                        print("Cancelling...")
                    else:
                        print("Invalid input...")
                    
                    #-------
                # --------
            elif what == "2":
                print("You chose to change your recipe")
                price(money)
            elif what == "3":
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
    
    game()

elif p.lower() == "n":
    print("Exiting...")
    sys.exit()
else:
    print("Invalid input. Exiting...")
    sys.exit()


