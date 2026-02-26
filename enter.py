import sys
import time
from welcomeToShop import shop

#-------
#-------
def startday():
    print("Starting the day!")
    print("selling...")
    time.sleep(1)
    print("selling...")
    time.sleep(1)
    print("selling...")
    time.sleep(1)
#-------
def enter1(money,ingredients,shop):
    play = input("Would you like to enter the shop? - ")
    if play.lower == "yes" or play.lower == "ok" or play.lower == "y":
        print("Entering shop...")
        shop()
        exit_code = 0
        while True:
            print(f"\nYou have {ingredients}.")
            print(">>>")
            print(f"You have {money} dollars.")
            money, exit_code = shop(ingredients,money)
            if exit_code == -1:
                break
    #-------
    if play.lower == "no" or play.lower == "nope" or play.lower == "n":
        print("Cancelling...")
    #-------
    if money <= 0:
        print("You lost!")
        print("------------------")
        print("GAME OVER!")
        sys.exit()
#-------