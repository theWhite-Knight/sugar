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
    "Lemons": lemons,
    "Sugar": sugar,
    "Cups": cups, 
    "Ice": ice,
}
#-------
def shop():
    global money
    global ingredients
    print("\nYou have entered the shop!") # Takes count of what the user wants >>
    print("------------------------------------------------------")
    when = input("What would you like to purchase? \
(1) Lemons [1.99 per], (2) Sugar [0.60 per lb], (3) Cups [0.50 per], (4) Ice [0.99 per lb]:\n" "Enter EXIT to exit.\n")
    # Math on the cost*Usercount for each ingredient >>
    if when == "1":
        print("You have decided to pick Lemons!")
        amount= int(input("How much would you like to buy?:\n"))
        if amount*lemonPrice >= money:
            print("You don't have enough money")
        elif amount*lemonPrice <= money:
            money = money-amount*lemonPrice
            ingredients["Lemons"] += amount
    if when == "2":
        print("You have decided to pick Sugar!")
        amount = int(input("How much would you like to buy?:\n"))
        if amount*sugarPrice >= money:
            print("You don't have enough money")
        elif amount*sugarPrice <= money:
            money = money-amount*sugarPrice
            ingredients["Sugar"] += amount
    if when == "3":
        print("You have decided to pick Cups!")
        amount = int(input("How much would you like to buy?:\n"))
        if amount*cupPrice >= money:
            print("You don't have enough money")
            print(money)
        elif amount*cupPrice <= money:
            money = money-amount*cupPrice
            ingredients["Cups"] += amount
    if when == "4":
        print("You have decided to pick Ice!")
        amount = int(input("How much would you like to buy?:\n"))
        if amount*icePrice >= money:
            print("\nYou don't have enough money\n")
            print(money)
        elif amount*icePrice <= money:
            money = money-amount*icePrice
            ingredients["Ice"] += amount
    if when.lower() == "exit":
        print(f"Your balance is: {money}")
        return -1
#-------
if money <= 0:
    print("You lost!")
    print("------------------")
    print("GAME OVER!")
    sys.exit()
#-------
while True:
    print(f"\nYou have {ingredients}.")
    print(">>>")
    print(f"You have {money} dollar(s).")
    if shop() == -1:
        break
#-------
print("------------------------------------------------------")
# The fear of long words is Hippopotomonstrosesquippedaliophobia.