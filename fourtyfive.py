# This is the ingredients and money Code

# Money

import sys


Money = 200

# ingredients

lemons = 0
sugar = 0
cups = 0
ice = 0


ingredients = {
    "Lemons ": lemons,
    "Sugar ": sugar,
    "Cups ": cups, 
    "Ice ": ice,
}

def shop():
    print("You have entered the shop!")
    print("------------------------------------------------------")
    when = input("What would you like to purchase? (1) Lemons, (2) Sugar, (3) Cups, (4) Ice - ")

    if when == "1":
        print("You have decided to pick Lemons!")
        amount_1 = int(input("How much do you want to buy? - "))

    if when == "2":
        print("You have decided to pick Sugar!")

    if when == "3":
        print("You have decided to pick Cups!")

    if when == "4":
        print("You have decided to pick Ice!")

    else:
        print("Please try again...")
        shop()


if Money <= 0:
    print("you lost!")
    sys.exit

print("You have ",ingredients,".")
print("You have ",Money," Money.")
shop()

print("------------------------------------------------------")
