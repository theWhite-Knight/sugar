# This is the ingredients and money Code

# Money

import sys


money = 200

# ingredients

lemons = 0
sugar = 0
cups = 0
ice = 0

#cost
lemonPrice = 1.99
sugarPrice = 0.60
cupPrice = 0.50
icePrice = 0.99

ingredients = {
    "Lemons ": lemons,
    "Sugar ": sugar,
    "Cups ": cups, 
    "Ice ": ice,
}

def shop():
    print("You have entered the shop!")
    print("------------------------------------------------------")
    when = input("What would you like to purchase? \
    (1) Lemons [1.99 per], (2) Sugar [0.60 per lb], (3) Cups [0.50 per], (4) Ice [0.99 per lb]- ")

    if when == "1":
        print("You have decided to pick Lemons!")
        amount_1 = int(input("How much would you like to buy? - "))
        if money*lemonPrice >= money:
            print("You dont have enough money")
            shop()
        if money*lemonPrice <= money:
            money-amount_1*lemonPrice
            shop()     
    if when == "2":
        print("You have decided to pick Sugar!")
        amount_2 = int(input("How much would you like to buy? - "))
        if money*sugarPrice >= money:
            print("You don't have enough money")
            shop()
        money-amount_2*sugarPrice
    if when == "3":
        print("You have decided to pick Cups!")
        amount_3 = int(input("How much would you like to buy? - "))
        money-amount_3*cupPrice
    if when == "4":
        print("You have decided to pick Ice!")
        amount_4 = int(input("How much would you like to buy? - "))
        money-amount_4*icePrice
    else:
        print("Please try again...")
    print(f"Your balance is: {money}")
        shop()


if Money <= 0:
    print("You lost!")
    print("------------------")
    print("GAME OVER!")
    sys.exit()

print("You have ",ingredients,".")
print("You have ",Money," Money.")
shop()

print("------------------------------------------------------")
