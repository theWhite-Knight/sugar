# ALex's take on "Ingredients and Money"
#-------
import sys
#-------
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
#-------
ingredients = {
    "Lemons": lemons,
    "Sugar": sugar,
    "Cups": cups, 
    "Ice": ice,
}
#-------
def shop():
    when = input("What would you like to purchase? \
    (1) Lemons [1.99 per], (2) Sugar [0.60 per lb], (3) Cups [0.50 per], (4) Ice [0.99 per lb]:\n" "Enter EXIT to exit.\n")
    while when != "exit":
        global money, ingredients
        print(f"\nYou have {ingredients}.")
        print(">>>")
        print(f"You have {money} dollar(s).")
        print("\nYou have entered the shop!") # Takes count of what the user wants >>
        print("------------------------------------------------------")
        
        # Math on the cost*Usercount for each ingredient >>
        if when == "1":
            print("You have decided to pick Lemons!")
            amount= int(input("How much would you like to buy?:\n"))
            if amount*lemonPrice >= money:
                print("You don't have enough money")
            elif amount*lemonPrice <= money:
                money = money-amount*lemonPrice
                ingredients["Lemons"] += amount
            print(f"You now have a balance of {money}")
        if when == "2":
            print("You have decided to pick Sugar!")
            amount = int(input("How much would you like to buy?:\n"))
            if amount*sugarPrice >= money:
                print("You don't have enough money")
            elif amount*sugarPrice <= money:
                money = money-amount*sugarPrice
                ingredients["Sugar"] += amount
            print(f"You now have a balance of {money}")
        if when == "3":
            print("You have decided to pick Cups!")
            amount = int(input("How much would you like to buy?:\n"))
            if amount*cupPrice >= money:
                print("You don't have enough money")
                print(money)
            elif amount*cupPrice <= money:
                money = money-amount*cupPrice
                ingredients["Cups"] += amount
            print(f"You now have a balance of {money}")
        if when == "4":
            print("You have decided to pick Ice!")
            amount = int(input("How much would you like to buy?:\n"))
            if amount*icePrice >= money:
                print("\nYou don't have enough money\n")
                print(money)
            elif amount*icePrice <= money:
                money = money-amount*icePrice
                ingredients["Ice"] += amount
            print(f"You now have a balance of {money}")
        if when.lower() == "exit":
            print(f"Your balance is: {money}")
            return -1
#-------
#-------
# print("------------------------------------------------------")
# The fear of long words is Hippopotomonstrosesquippedaliophobia.







# def shop():
#     global money, ingredients
#     # print("\nYou have entered the shop!") # Takes count of what the user wants >>
#     print("------------------------------")
#     when = input("What would you like to purchase? \
# (1) Lemons [1.99 per], (2) Sugar [0.60 per lb], (3) Cups [0.50 per], (4) Ice [0.99 per lb]:\nEnter EXIT to exit.\n")
#     # Math on the cost*Usercount for each ingredient >>
#     if when == "1":
#         print("You have decided to pick Lemons!")
#         amount = int(input("How much would you like to buy?:\n"))
#         cost = amount * lemonPrice
#         if cost >= money:
#             print("You don't have enough money")
#         else:
#             money = money - cost
#             ingredients["Lemons"] += amount
#             print(f"You bought {amount} lemon(s)!")
            
#     elif when == "2":
#         print("You have decided to pick Sugar!")
#         amount = int(input("How much would you like to buy?:\n"))
#         cost = amount * sugarPrice
#         if cost >= money:
#             print("You don't have enough money")
#         else:
#             money = money - cost
#             ingredients["Sugar"] += amount
#             print(f"You bought {amount} lb of sugar!")
            
#     elif when == "3":
#         print("You have decided to pick Cups!")
#         amount = int(input("How much would you like to buy?:\n"))
#         cost = amount * cupPrice
#         if cost >= money:
#             print("You don't have enough money")
#             print(money)
#         else:
#             money = money - cost
#             ingredients["Cups"] += amount
#             print(f"You bought {amount} cup(s)!")
            
#     elif when == "4":
#         print("You have decided to pick Ice!")
#         amount = int(input("How much would you like to buy?:\n"))
#         cost = amount * icePrice
#         if cost >= money:
#             print("\nYou don't have enough money\n")
#             print(money)
#         else:
#             money = money - cost
#             ingredients["Ice"] += amount
#             print(f"You bought {amount} lb of ice!")
            
#     elif when.lower() == "exit":
#         print(f"Your balance is: ${money:.2f}")
#         return money, -1
#     else:
#         print("Invalid choice. Please try again.")
        
#     return money, 0

# #-------
# # The fear of long words is Hippopotomonstrosesquippedaliophobia.
# print("------------------------------------------------------")