import time
import sys
#-------
import welcomeToShop
import enter
import main_two
from main_two import game as g
#-------
ingredients = {
    "Lemons": 0,
    "Sugar": 0,
    "Cups": 0, 
    "Ice": 0,
}
#-------
money = 200
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
    g(money,ingredients)

if p.lower() == "n":
    print("Exiting...")
    sys.exit()
 
else:
    print("Try again")
    sys.exit()
if TypeError:
    print("Try again")
    sys.exit()
