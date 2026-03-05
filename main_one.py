# ~ The Lemonade Stand Game ~
# Explanation for unknown terminology in... C:\Users\al547645\Documents\GitHub\sugar\explanation_for_main.py
# --- Imports ---
import time
import sys
import random
import math
import datetime
# Import functions from other modules
from ToDoList import todo
from welcomeToShop import set_globals, S
#-------
# Global variables accessible across modules
money = 250
day = 1
LemonSet = 0
# For Recipe, A list turns to this (Dictionary) 
Usage = {}
start = True
lemon = True
# Customer preference tracking
customer_preferences = {
    "sweet": 0,
    "sour": 0,
    "balanced": 0
}
ingredients = {
    "Lemons": 0,
    "Sugar": 0,
    "Cups": 0, 
    "Ice": 0,
}
# Recipe amounts (for customer preference calculation)
recipe = {
    "Lemons": 0,
    "Sugar": 0,
    "Ice": 0
}
# NOTE: On the What Input, if you put "TODO" it will print up our TODO list.
# NOTE: The next section is all Customer Preference Calculation and Sales Processing. It calculates how many customers prefer sweet, sour, or balanced lemonade based on the recipe,
# And then processes sales based on the price and customer preferences, while also updating the player's money and inventory accordingly.
def calculate_customer_preference():
    # Calculate customer preference based on recipe (Lemons = sour, Sugar = sweet)
    # Ice, and Cups are required to sell, but don't affect customer preference, just the amount of customers you can sell to
    global customer_preferences    
    lemons = recipe.get("Lemons", 0)
    sugar = recipe.get("Sugar", 0)
    Ice = recipe.get("Ice", 0)   
    # If no lemons or sugar, customers won't buy
    if lemons == 0 and sugar == 0 and ingredients["Ice"] > 0:
        print("\n WARNING: Your recipe has no LEMON or SUGAR! Customers won't buy your lemonade!")
        return 0    
    # Calculate ratio
    total = lemons + sugar + Ice  # Total ingredients in the recipe (Ice is included to ensure customers prefer a recipe with ice, but it doesn't affect sweet/sour preference)
    if total == 0:
        return 0
    lemon_ratio = lemons / total
    sugar_ratio = sugar / total
    ice_ratio = Ice / total
    # Determine preference distribution
    if lemon_ratio > 0.7:
        # Very sour - mostly sour preference customers
        customer_preferences["sweet"] = int(10 * sugar_ratio)
        customer_preferences["sour"] = int(30 * lemon_ratio)
        customer_preferences["balanced"] = int(10 * (1 - abs(lemon_ratio - 0.5)))
        print(f"\n Customer preference: VERY SOUR ({lemons} lemons, {sugar} sugar)")
    elif lemon_ratio > 0.5:
        # Sour - more sour preference
        customer_preferences["sweet"] = int(20 * sugar_ratio)
        customer_preferences["sour"] = int(25 * lemon_ratio)
        customer_preferences["balanced"] = int(15 * (1 - abs(lemon_ratio - 0.5)))
        print(f"\n Customer preference: SOUR ({lemons} lemons, {sugar} sugar)")
    elif sugar_ratio > 0.7:
        # Very sweet - mostly sweet preference customers
        customer_preferences["sweet"] = int(30 * sugar_ratio)
        customer_preferences["sour"] = int(10 * lemon_ratio)
        customer_preferences["balanced"] = int(10 * (1 - abs(sugar_ratio - 0.5)))
        print(f"\n Customer preference: VERY SWEET ({lemons} lemons, {sugar} sugar)")
    elif sugar_ratio > 0.5:
        # Sweet - more sweet preference
        customer_preferences["sweet"] = int(25 * sugar_ratio)
        customer_preferences["sour"] = int(20 * lemon_ratio)
        customer_preferences["balanced"] = int(15 * (1 - abs(sugar_ratio - 0.5)))
        print(f"\n Customer preference: SWEET ({lemons} lemons, {sugar} sugar)")
    elif ice_ratio > 0.7:
        # Icy - more balanced preference

        customer_preferences["sweet"] = int(20 * sugar_ratio)
        customer_preferences["sour"] = int(20 * lemon_ratio)
        customer_preferences["balanced"] = int(20 * ice_ratio)
        print(f"\n Customer preference: ICY ({lemons} lemons, {sugar} sugar, {Ice} ice)")
    elif ice_ratio > 0.5:
        # Icy - more balanced preference

        customer_preferences["sweet"] = int(15 * sugar_ratio)
        customer_preferences["sour"] = int(15 * lemon_ratio)
        customer_preferences["balanced"] = int(25 * ice_ratio)
        print(f"\n Customer preference: ICY ({lemons} lemons, {sugar} sugar, {Ice} ice)")
    else:
        # Balanced
        customer_preferences["sweet"] = 20
        customer_preferences["sour"] = 20
        customer_preferences["balanced"] = 20
        print(f"\n Customer preference: BALANCED ({lemons} lemons, {sugar} sugar)") 
    # Total potential customers based on recipe quality
    return min(50, (lemons + sugar + Ice) * 2)
# ------
def sell_to_customers(price, potential_customers):
    global money, ingredients, recipe, customer_preferences
    if ingredients["Ice"] <= 0:
        print("\n WARNING: You need ice to sell Lemonade!")
        return 0
    if ingredients["Cups"] <= 0:
        print("\n WARNING: You need cups to sell Lemonade!")
        return 0 
    if ingredients["Lemons"] <= 0:
        print("\n WARNING: You need lemons to sell Lemonade!")
        return 0 
    if ingredients["Sugar"] <= 0:
        print("\n WARNING: You need sugar to sell Lemonade!")
        return 0
    sold = 0
    base_willingness = 3.00
    # Loop through all customers based on preference distribution
    for pref_type, pref_count in customer_preferences.items():
        for _ in range(pref_count):
            # Determine willingness to pay
            if pref_type == "sweet":
                willingness = base_willingness + random.uniform(-0.50, 1.00)
            elif pref_type == "sour":
                willingness = base_willingness + random.uniform(-0.50, 0.75)
            else:  # balanced
                willingness = base_willingness + random.uniform(-0.25, 0.50)
            # Check if customer buys
            if (
                price <= willingness
                and ingredients["Cups"] > 0
                and ingredients["Ice"] > 0
            ):
                sold += 1
                money += price
                # Use 1 cup and 1 ice per sale
                ingredients["Cups"] -= 1
                ingredients["Ice"] -= 1
                # Use recipe-based amounts per cup
                ingredients["Lemons"] = max(0, ingredients["Lemons"] - recipe["Lemons"])
                ingredients["Sugar"] = max(0, ingredients["Sugar"] - recipe["Sugar"])
                # Stop if we run out mid‑sales
                if (
                    ingredients["Cups"] <= 0
                    or ingredients["Ice"] <= 0
                    or ingredients["Lemons"] <= 0
                    or ingredients["Sugar"] <= 0
                ):
                    return sold
    return sold
# Rounds up the customer preferences
# to the nearest whole number, since you can't have a fraction of a customer.
customer_preferences["sweet"] = math.ceil(customer_preferences["sweet"])
customer_preferences["sour"] = math.ceil(customer_preferences["sour"])
customer_preferences["balanced"] = math.ceil(customer_preferences["balanced"])
# -----
def game():
    ask_user = True
    global day
    global money
    global ingredients
    global recipe
    global Usage
    while day < 7:
        print("New Day...\n")
        print(f"Day {day} begins!\n")
        # Prints the Actual Time of Day In Real Life
        print(f"The time of day is: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")        
        print("\n>>>")
        print(">>>\n")
        print("The time in-game is 8:00 AM. Time to set up your stand and get ready for the day!")
        try:
            while ask_user == True:
                LemonSet = float(input("What would you like to set your Lemonade price to?\n (Note: You can change this later; be sure to add decimals to the hundreths place. For example 2.99)\
            \n  Do NOT add a Dollar Sign $\n"))
                print("--------------------------------------------------")
                ask_user = False
        except ValueError:
            print("Please enter a valid number!")
            print(">>>")
            print(">>>")
            continue
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()
        if isinstance(LemonSet, (int, float)) and LemonSet > 0:
            print(f"You have ${money:.2f} dollar(s). \nYour Inventory contains of {ingredients}. \nYou are on Day {day}. \nYour BASE recipe consists of {Usage}.\n(You can change your recipe in the Menu)")
            print(f"Your Lemonade is currently priced at ${LemonSet:.2f} per cup of Lemonade.\n(You can change your price in the Menu)")
            print("NOTE: You have to re-type in your Lemonade price, and your Recipe every day.")
            #-------
            print("NOTE: You cannot start the sales day if your Lemonade Price equals 0, and if your Recipe doesn't have Lemons, Ice, and Sugar with a set amount of each.\n")
            print(">>>")
            print(">>>\n")
            print("-----------------------------------------------------------------------------------------------------------------")
            try:
                what = input("What would you like to do? (Enter the #) \n(1) Shop \n(2) Change recipe \n(3) Change pricing \n(4) Start the day.\n")
            except KeyboardInterrupt:
                print("\nExiting...")
                sys.exit()
            if what != what.int(): # requires testing here...
                print("Please enter a number value...")
            #-------
            # --- Cheat Codes --- #
            if what.lower().strip() == "ENDOFLINE":
                money += 1000
                print("Cheat code activated: ENDOFLINE - You gained $1000!")
            if what.lower().strip() == "ADMIN_ABUSE":
                money += 500
                ingredients["Lemons"] += 100
                ingredients["Sugar"] += 100
                ingredients["Cups"] += 100
                ingredients["Ice"] += 100
                print("Cheat code activated: ADMIN_ABUSE - You gained $500 and 100 of each ingredient!")
            if what.lower().strip() == "areweserious?!":
                money *= 1.2
                print("Cheat code activated: AreWeSerious?! - Your Money is now Multiplied by 1.2x!")
            # --- Todo List ---
            if what == "TODO":
                todo()
            # Actual Options
            elif what == "1":
                # Access global variables from main_one
                print("--------------------------------------------------")
                try:
                    enter = input("Would you like to enter the shop? (Y/N):\n")
                except KeyboardInterrupt:
                    print("\nExiting...")
                    sys.exit()
                if enter.lower().strip() == "y":
                    print("You choose to enter shop...")
                    # Update global variables before each shop call
                    print(">>>")
                    print(">>>")
                    # Set globals in welcomeToShop module before calling shop
                    set_globals(money, ingredients)
                    returned_money, returned_ingredients = S()
                    # Sync back the updated values
                    money = returned_money
                    ingredients = returned_ingredients
                elif enter.lower().strip() == "n":
                    print("Cancelling...")
                else:
                    print("Invalid input... \n")
                #-------
                # --------
            elif what == "2":
                print("--------------------------------------------------")
                print("You choose to change your recipe...") # Recipe
                print("\n Recipe Guide:")
                print(">>>")
                print(">>>\n")
                print("  - Lemons add SOURNESS (customers who like sour will pay more).")
                print("  - Sugar adds SWEETNESS (customers who like sweet will pay more).")
                print("  - Ice adds COLDNESS (customers who like cold will pay more).")
                print("  - Balanced recipes (with a good mix of Lemons, Sugar, and Ice) will attract more customers overall!")
                print("  - Balance is key! Too much of either may reduce customers.")
                print("  - Ice, Lemons, and Sugar are ALL REQUIRED to sell Lemonade.\n")
                print("  - One Cup is automatically used for one set of Lemonade.")
                print(">>>")
                print(">>>\n")
                def price():
                    global Usage
                    global recipe
                    recipe_items = []
                    while True:
                        try:
                            item = input("What would you like to add to your recipe? (Lemons, Sugar, Ice - Type EXIT to exit)\n")
                        except KeyboardInterrupt:
                            print("\nExiting...")
                            sys.exit()
                        if item.lower().strip() == 'exit':
                            break
                        # Validate ingredient
                        if item.lower().strip() not in ("lemons", "sugar", "ice"):
                            print("Please enter a valid ingredient (Lemons, Sugar, Ice)\n")
                            continue
                        try:
                            amount = int(input("How much would you like to add?\n"))
                        except ValueError:
                            print("Please enter a valid number!")
                            continue
                        except KeyboardInterrupt:
                            print("\nExiting...")
                            sys.exit()
                        # Update recipe
                        recipe[item.capitalize()] = amount
                        recipe_items.append(item.capitalize())
                        recipe_items.append(str(amount))
                        print(f"Added: {amount} {item.capitalize()} ")
                        Usage["recipe"] = recipe_items
                        print(f"Your Recipe: {recipe}")
                price()
                # Calculate customer preferences based on new recipe
                calculate_customer_preference()
            elif what == "3":
                print("--------------------------------------------------")
                print("You choose to change your Lemonade price...")
                try:
                    LemonSet = float(input("What would you like to set your Lemonade price to?\n "))
                    if LemonSet > 0.01:
                        print(f"You set your Lemonade price to ${LemonSet}!")
                    elif LemonSet <= 0.01:
                        print("Price must be greater than 0.01. Please try again...")
                    else:
                        print("Please try again...")
                except ValueError:
                    print("Please enter a valid number...")
                except KeyboardInterrupt:
                    print("\nExiting...")
                    sys.exit()
            elif what == "4":
                #-------
                def startday():
                    global day
                    global money
                    global ingredients
                    print("--------------------------------------------------")
                    # Check if recipe is set
                    if recipe["Lemons"] == 0 and recipe["Sugar"] == 0:
                        print(" You need to set up your recipe first! Go to option 2.")
                        return
                    # Check if we have ingredients to sell
                    if ingredients["Cups"] == 0 or ingredients["Ice"] == 0:
                        print(" You need cups and ice to sell Lemonade! Visit the shop.")
                        return
                    # Flush is used to ensure that the "selling..." messages are printed immediately. If Flush isn't 'True' then the selling won't work.
                    # Flush itself doesn't actually do anything, but it forces the print statement to output immediately, which is important for the selling animation to work properly.
                    print("Starting the day!")
                    print("selling...", flush = True)
                    time.sleep(1)
                    print("selling...", flush = True)
                    time.sleep(1)
                    print("selling...", flush = True)
                    time.sleep(1)
                    # Calculate customer preference
                    potential_customers = calculate_customer_preference()
                    if potential_customers > 0:
                        # Sell to customers
                        sold = math.ceil(sell_to_customers(LemonSet, potential_customers))
                        print(f"\n You sold {sold:.2f} cups of Lemonade!")
                        print(f" You earned ${sold * LemonSet:.2f}")
                        print(f" Current money: ${money:.2f}")
                        print(f" Remaining ingredients: {ingredients}")
                    else:
                        print("\n No customers bought your Lemonade! Check your recipe.")
                    day += 1
                    print(f"\nDay {day} begins!")
                #-------
                startday()
            if ValueError:
                print("Please enter a valid number!")
                continue
    if day >= 7:
        print("--------------------------------------------------")
        print("You have survived 7 Days of Buisness!!")
        try:
            credit_roll = input("Would you like to roll Credits?\n")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()
        if credit_roll.lower().strip() in ("y", "yes", "ok", "okay", "sure"):
            print("Now rolling Credits...")
            time.sleep(0.75)
            print("Front End...")
            time.sleep(0.75)
            print("Jet")
            time.sleep(0.75)
            print("Alexandra")
            time.sleep(0.75)
            print("Back End...")
            time.sleep(0.75)
            print("Dillan")
            time.sleep(0.75)
            print("Evaristo")
            time.sleep(0.75)
            print("Testers...")
            time.sleep(0.75)
            print("Tristan")
            time.sleep(0.75)
            print("Evaristo")
            time.sleep(0.75)
            print("The End!")
            time.sleep(0.75)
            print("Thanks for Playing!")
            print(f"Final Money: ${money:.2f}")
            print(f"Final Day: {day}")
            print(f"Final Recipe: {recipe}")
            print(f"Final Ingredients: {ingredients}")
            print(f"Final Lemonade Price: ${LemonSet:.2f}")
            print("Exiting...")
            time.sleep(0.75)
            sys.exit()
        if credit_roll.lower().strip() in ("no", "n"):
            print("Okay, Thanks for Playing!")
            time.sleep(0.75)
            print(f"Final Money: ${money:.2f}")
            print(f"Final Day: {day}")
            print(f"Final Recipe: {recipe}")
            print(f"Final Ingredients: {ingredients}")
            print(f"Final Lemonade Price: ${LemonSet:.2f}")
            time.sleep(0.75)
            sys.exit()
    if not (isinstance(LemonSet, (int, float)) and LemonSet > 0):
        print("Please try again!")
if money <= 0:
    print("You lost!")
    print("------------------")
    print("GAME OVER!")
    sys.exit()
#-------
print("------------------------------")
print("★~ The Lemonade Stand Game ~★")
print("------------------------------")
try:
    p = input("Would you like to play the game? (Y/N)\n")
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()
#-------
if p.lower().strip() in ("y", "yes", "ok", "okay", "sure"):
    print("Good Luck!")
    print("Starting game...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("--------------------------------------------------------------------------")
    if start == True:
        game()
        start = False
elif p.lower() == "n":
    print("Exiting...")
    sys.exit()
else:
    print("Invalid input. Exiting...")
    sys.exit()
# ----------------------------------------------------------------------------------------------------------