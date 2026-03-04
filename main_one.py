import time
import sys
import random

# Import functions from other modules
from ToDoList import todo
from welcomeToShop import set_globals, S

#-------

# Global variables accessible across modules
money = 200
day = 1

LemonSet = 0

# For Recipe, A list turns to this (Dictionary) 

Usage = {}

ask = True
start = True
lemon = True
day_cycle = False

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
    "Cups": 0,
    "Ice": 0
}

# NOTE: On the What Input, if you put "TODO" it will print up our TODO list.



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
if p.lower() in ("y", "yes", "ok", "okay", "sure"):
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
    
    def calculate_customer_preference():
        # Calculate customer preference based on recipe (Lemons = sour, Sugar = sweet)
        global customer_preferences
        
        lemons = recipe.get("Lemons", 0)
        sugar = recipe.get("Sugar", 0)
        
        # If no lemons or sugar, customers won't buy
        if lemons == 0 and sugar == 0 and ingredients["Cups"] > 0 and ingredients["Ice"] > 0:
            print("\n WARNING: Your recipe has no Lemon or Sugar! Customers won't buy your lemonade!")
            return 0
        
        # Calculate ratio
        total = lemons + sugar
        if total == 0:
            return 0
            
        lemon_ratio = lemons / total
        sugar_ratio = sugar / total
        
        # Determine preference distribution
        if lemon_ratio > 0.7:
            # Very sour - mostly sour preference customers
            customer_preferences["sweet"] = int(10 * sugar_ratio)
            customer_preferences["sour"] = int(30 * lemon_ratio)
            customer_preferences["balanced"] = int(10 * (1 - abs(lemon_ratio - 0.5)))
            print(f"\n Customer Preference: VERY SOUR ({lemons} lemons, {sugar} sugar)")
        elif lemon_ratio > 0.5:
            # Sour - more sour preference
            customer_preferences["sweet"] = int(20 * sugar_ratio)
            customer_preferences["sour"] = int(25 * lemon_ratio)
            customer_preferences["balanced"] = int(15 * (1 - abs(lemon_ratio - 0.5)))
            print(f"\n Customer Preference: SOUR ({lemons} lemons, {sugar} sugar)")
        elif sugar_ratio > 0.7:
            # Very sweet - mostly sweet preference customers
            customer_preferences["sweet"] = int(30 * sugar_ratio)
            customer_preferences["sour"] = int(10 * lemon_ratio)
            customer_preferences["balanced"] = int(10 * (1 - abs(sugar_ratio - 0.5)))
            print(f"\n Customer Preference: VERY SWEET ({lemons} lemons, {sugar} sugar)")
        elif sugar_ratio > 0.5:
            # Sweet - more sweet preference
            customer_preferences["sweet"] = int(25 * sugar_ratio)
            customer_preferences["sour"] = int(20 * lemon_ratio)
            customer_preferences["balanced"] = int(15 * (1 - abs(sugar_ratio - 0.5)))
            print(f"\n Customer Preference: SWEET ({lemons} lemons, {sugar} sugar)")
        else:
            # Balanced
            customer_preferences["sweet"] = 20
            customer_preferences["sour"] = 20
            customer_preferences["balanced"] = 20
            print(f"\n Customer Preference: BALANCED ({lemons} lemons, {sugar} sugar)")
        
        # Total potential customers based on recipe quality
        return min(50, (lemons + sugar) * 2)
    
    def sell_to_customers(price, potential_customers):
        # Process sales based on customer preferences and price
        global money
        global ingredients
        
        if ingredients["Cups"] == 0 or ingredients["Ice"] == 0:
            print("\n WARNING: You need cups and ice to sell lemonade!")
            return 0
            
        sold = 0
        # Customer tolerance: they'll pay more for sweeter/balanced drinks
        base_willingness = 3.00  # Base price customers are willing to pay
        
        # Adjust willingness based on preference match
        for pref_type, pref_count in customer_preferences.items():
            for _ in range(pref_count):
                # Determine what customer is willing to pay
                if pref_type == "sweet":
                    willingness = base_willingness + random.uniform(-0.50, 1.00)
                elif pref_type == "sour":
                    willingness = base_willingness + random.uniform(-0.50, 0.75)
                else:  # balanced
                    willingness = base_willingness + random.uniform(-0.25, 0.50)
                
                # Customer buys if price is within willingness
                if price <= willingness and ingredients["Cups"] > 0 and ingredients["Ice"] > 0:
                    sold += 1
                    money += price
                    ingredients["Cups"] -= 1
                    ingredients["Ice"] -= 1
                    # Use some lemons and sugar
                    if recipe["Lemons"] > 0:
                        ingredients["Lemons"] = max(0, ingredients["Lemons"] - (recipe["Lemons"] / 10))
                    if recipe["Sugar"] > 0:
                        ingredients["Sugar"] = max(0, ingredients["Sugar"] - (recipe["Sugar"] / 10))
        
        return sold

    def game():
        global day
        global money
        global ingredients
        global recipe
        while day <= 7:
            print("New Day...")
            print(f"Day {day} begins!")

            if day_cycle == False:
                day = 1
                day_cycle = True
            
            if day_cycle == True:
                day += 1

            try:
                if ask == True:
                    LemonSet = float(input("What would you like to set your Lemonade price to?\n   (Note: You can change this later, and add decimals to the hundreths place, For example 2.99)\nNOTE: Don't add a Dollar Sign $\n"))
                    ask = False

            except ValueError:
                print("Please enter a valid number!")
                continue

            except KeyboardInterrupt:
                print("\nExiting...")
                sys.exit()

            
            if isinstance(LemonSet, (int, float)) and LemonSet > 0:

                print("------------------------------------------------------------------------------------------------------------------------------------")
                print(f"You have {money} Money. \nYour Inventory contains of {ingredients}. \nYou are on Day {day}. \nYour Recipe consists of {Usage}.")
                print(f"The price of your Lemonade is ${LemonSet}\n")

                print("NOTE: You cannot start the sales day if your Lemonade Price equals 0, and if your Recipe doesn't have Lemons, Cups, Ice, and Sugar with a set amount of each\n")
                print(">>>")
                print(">>>")
                print("-----------------------------------------------------------------------------------------------------------------")
                try:
                    what = input("What would you like to do? (1) Shop, (2) change recipe, (3) Change pricing, (4) Start the day.\n")

                except KeyboardInterrupt:
                    print("\nExiting...")
                    sys.exit()
                #-------
                if what == "TODO":
                    todo()
                
                elif what == "1":
                    # Access global variables from main_one
                    print("--------------------------------------------------")
                    try:
                        enter = input("Would you like to enter the shop? (Y/N):\n")

                    except KeyboardInterrupt:
                        print("\nExiting...")
                        sys.exit()
                    if enter.lower() == "y":
                        print("Entering shop...")
                        # Update global variables before each shop call
                        print(f"\nYou have {ingredients}.")
                        print(">>>")
                        print(f"You have ${money:.2f} dollars.")
                        # Set globals in welcomeToShop module before calling shop
                        set_globals(money, ingredients)
                        returned_money, returned_ingredients = S()
                        # Sync back the updated values
                        money = returned_money
                        ingredients = returned_ingredients
                    elif enter.lower() == "n":
                        print("Cancelling...")
                    else:
                        print("Invalid input...")
                        #-------
                    # --------
                elif what == "2":
                    print("--------------------------------------------------")
                    print("You chose to change your recipe") # Recipe
                    
                    print("\n Recipe Guide:")
                    print("  - Lemons add SOURNESS (customers who like sour will pay more)")
                    print("  - Sugar adds SWEETNESS (customers who like sweet will pay more)")
                    print("  - Balance is key! Too much of either may reduce customers.")
                    print("  - Ice, Lemons, and Sugar are all REQUIRED to sell lemonade\n")

                    def price():
                        global Usage
                        global recipe
                        recipe_items = []
                        while True:
                            try:
                                item = input("What would you like to add to your recipe? (Lemons, Sugar, Ice - Type STOP to Stop)\n")

                            except KeyboardInterrupt:
                                print("\nExiting...")
                                sys.exit()
                            
                            if item.lower() == 'stop':
                                break
                                
                            # Validate ingredient
                            if item.lower() not in ("lemons", "sugar", "ice"):
                                print("Please enter a valid ingredient (Lemons, Sugar, Ice)")
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
                    print("You chose to change your lemonade price")
                    try:
                        LemonSet = float(input("What would you like to set your lemonade price to?\n "))

                        if LemonSet > 0.01:
                            print(f"You set your lemonade price to ${LemonSet}!")

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
                            print(" You need cups and ice to sell lemonade! Visit the shop.")
                            return
                        
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
                            sold = sell_to_customers(LemonSet, potential_customers)
                            print(f"\n You sold {sold} cups of lemonade!")
                            print(f" You earned ${sold * LemonSet:.2f}")
                            print(f" Current money: ${money:.2f}")
                            print(f" Remaining ingredients: {ingredients}")
                        else:
                            print("\n No customers bought your lemonade! Check your recipe.")
                        
                        day += 1
                        print(f"\nDay {day} begins!")

                    #-------

                    startday()

                if ValueError:
                    print("Please enter a valid number!")
                    continue

        
            if day >= 7:
                print("--------------------------------------------------")
                print("You have survived 7 Days of Buisness")
                try:
                    credit_roll = input("Would you like to roll Credits?\n")
                except KeyboardInterrupt:
                    print("\nExiting...")
                    sys.exit()

                if credit_roll.lower() in ("y", "yes", "ok", "okay", "sure"):
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
                    sys.exit()
                
                if credit_roll.lower() in ("no", "n"):
                    print("Okay, Thanks for Playing!")
                    time.sleep(0.75)
                    sys.exit()

            if not (isinstance(LemonSet, (int, float)) and LemonSet > 0):
                print("Please try again!")
                continue

    if start == True:
        game()
        start = False

elif p.lower() == "n":
    print("Exiting...")
    sys.exit()

else:
    print("Invalid input. Exiting...")
    sys.exit()

