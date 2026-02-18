import time
import sys
#-------
from main_two import game
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
if p == "y":
    print("Starting game...")
    game(money,ingredients)    
else:
    print("Try again")
    sys.exit()