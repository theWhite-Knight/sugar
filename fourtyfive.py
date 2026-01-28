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

        if amount_1 * 1.99 <= Money:
            print("You have bought the items")
            Money -= amount_1 * 1.99

        if amount_1 * 1.99 >= Money:
            print("You dont have enough money!")
            shop()

    if when == "2":
        print("You have decided to pick Sugar!")
        amount_2 = int(input("How much do you want to buy? - "))

            if amount_2 * 1.79 <= Money:
            print("You have bought the items")
            Money -= amount_2 * 1.79

        if amount_2 * 1.979 >= Money:
            print("You dont have enough money!")
            shop()

    if when == "3":
        print("You have decided to pick Cups!")
        amount_3 = int(input("How much do you want to buy? - "))

            if amount_3 * 2.99 <= Money:
            print("You have bought the items")
            Money -= amount_3 * 2.99

        if amount_3 * 2.99 >= Money:
            print("You dont have enough money!")
            shop()

    if when == "4":
        print("You have decided to pick Ice!")
        amount_4 = int(input("How much do you want to buy? - "))

            if amount_4 * 1.59 <= Money:
            print("You have bought the items")
            Money -= amount_4 * 1.59

        if amount_4 * 1.59 >= Money:
            print("You dont have enough money!")
            shop()

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

