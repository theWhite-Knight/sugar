# ALex's take on "Ingredients and Money"
#-------
import sys
# Money
money = 200
#-------
# Ingredients
lemons = 0
sugar = 0
cups = 0
ice = 0
#-------
# Cost of ingredients.
lemonPrice = 1.99
sugarPrice = 0.60
cupPrice = 0.50
icePrice = 0.99
#-------
ingredients = {
    "Lemons ": lemons,
    "Sugar ": sugar,
    "Cups ": cups, 
    "Ice ": ice,
}
#-------
def shop():
    global money
    print("You have entered the shop!") # Takes count of what the user wants >>
    print("------------------------------------------------------")
    when = input("What would you like to purchase? \
    (1) Lemons [1.99 per], (2) Sugar [0.60 per lb], (3) Cups [0.50 per], (4) Ice [0.99 per lb]:\n" "Enter EXIT to exit.\n")
    # Math on the cost*Usercount for each ingredient >>
    if when == "1":
        print("You have decided to pick Lemons!")
        amount_1 = int(input("How much would you like to buy?:\n"))
        if money*lemonPrice >= money:
            print("You don't have enough money")
            shop()
        elif money*lemonPrice <= money:
            money = money-amount_1*lemonPrice
            print(money)
            shop()     
    if when == "2":
        print("You have decided to pick Sugar!")
        amount_2 = int(input("How much would you like to buy?:\n"))
        if money*sugarPrice >= money:
            print("You don't have enough money")
            shop()
        elif money*sugarPrice <= money:
            money = money-amount_2*sugarPrice
            print(money)
            shop()
    if when == "3":
        print("You have decided to pick Cups!")
        amount_3 = int(input("How much would you like to buy?:\n"))
        if money*cupPrice >= money:
            print("You don't have enough money")
            print(money)
            shop()
        elif money*cupPrice <= money:
            money = money-amount_3*cupPrice
            print(money)
            shop()
    if when == "4":
        print("You have decided to pick Ice!")
        amount_4 = int(input("How much would you like to buy?:\n"))
        if money*icePrice >= money:
            print("You don't have enough money")
            print(money)
            shop()
        elif money*icePrice <= money:
            money = money-amount_4*icePrice
            print(money)
            shop()
    if when == "EXIT":
        print(f"Your balance is: {money}")
        sys.exit()
    else:
        shop()
#-------
if money <= 0:
    print("You lost!")
    print("------------------")
    print("GAME OVER!")
    sys.exit()
#-------
print(f"You have {ingredients}.")
print(f"You have {money} money.")
shop()
#-------
print("------------------------------------------------------")
# Did you know that your brain is constantly eating itself? No context.
