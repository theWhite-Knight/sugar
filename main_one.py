# ~ The Lemonade Stand Game ~


# This is basically a Dictionary for terms or code you don't know, or just a general explanation of how the code works.


# >>>
# >>>
# >>>


# NOTE: "Abs" stands for "Absolute Value" which is a mathematical function that returns the non-negative value of a number. 
# In the context of the customer preference calculation, it is used to determine how far the lemon or sugar ratio is from a balanced 0.5, which helps to calculate how many 
# customers prefer sweet, sour, or balanced lemonade based on the recipe.
# -----
# Except KeyboardInterrupt is used to allow the user to exit the game gracefully by pressing Ctrl + C. When this happens, 
# it will print "Exiting..." and then terminate the program using sys.exit(). It gets rid of the SyntaxError that would normally occur when a user tries to exit the game by pressing Ctrl + C, 
# and allows for a cleaner exit experience, and doesn't look like we did something wrong.
# -----
# Except ValueError is used to catch cases where the user inputs something that cannot be converted to a number (like letters or symbols) 
# when setting the lemonade price or adding ingredients to the recipe. When this happens, it will print "Please enter a valid number!" and prompt the user to try again, 
# preventing the program from crashing due to invalid input.
# -----
# The Sour + Sweet ratio is calculated to determine customer preferences. If the lemonade is too sour (high lemon ratio) or too sweet (high sugar ratio), 
# it will affect how many customers are willing to buy the lemonade and how much they are willing to pay.
# The game encourages players to find a balance in their recipe to maximize sales.
# -----
# Random.uniform is used to add variability to customer willingness to pay, making the game more dynamic and less predictable. Basically, its just a better 
# way to make the game more fun and less robotic by adding some more randomness than (random.random / random.randit) to how much customers are willing to pay based on their preferences.
# -----
# NOTE: Prefrences are calculated based on the ratio of lemons to sugar in the recipe. If the lemonade is very sour (high lemon ratio), more customers will prefer sour lemonade.
# If it's very sweet (high sugar ratio), more customers will prefer sweet lemonade. The same goes for Lemons, (Sour Ratio). A balanced recipe will attract a more even distribution of customer preferences. And its completly 
# randomized on how much they are willing to pay based on their preferences, which adds more fun and less roboticness to the game.
# -----
# :.2f - This is a string formatting option that formats a floating-point number to two decimal places. In the context of this game, it is used to display the player's money and earnings 
# in a more readable format, showing only two digits after the decimal point (e.g., $10.00 instead of $10.0 or $10.000000). 
# This makes the financial information clearer and more professional-looking for the user.
# -----
# NOTE: The game is still in development, and there are many features that can be added to make it more enjoyable, such as a weather system that affects customer preferences, 
# upgrades for the stand, a storyline, and cheat codes. If you have an idea, feel free to add it to the TODO list in the ToDoList.py file! 
# The TODO list in the ToDoList.py file outlines these potential features and their development status.
# -----
# .Strip() is used to remove any leading or trailing whitespace from the user's input when they type "exit" to leave the shop. 
# This ensures that even if the user accidentally adds extra spaces before or after "exit"
# -----
# .Lower() is used to convert the user's input to lowercase when they type "exit" to leave the shop. This allows the program to recognize "EXIT", "Exit", "eXit", etc. as valid commands to exit the shop, 
# making it more user-friendly and flexible in accepting input.
# -----
# InInstance() is used to check if the lemonade price (LemonSet) is a valid number (either an integer or a float) and greater than 0 before allowing the player to start the sales day.
# This validation ensures that the player has set a proper price for their lemonade, which is essential for the game to function correctly. 
# If the price is not valid, the game will prompt the player to try again, preventing potential errors during the sales process.
# -----
# The game loop ( - Main_Game() - ) is structured to allow the player to manage their lemonade stand over multiple days. Each day, the player can choose to shop for ingredients, change their recipe, adjust their pricing, 
# or start the sales day. The loop continues until the player has completed 7 days of business, at which point they can choose to roll credits or exit the game.
# This structure provides a clear progression and allows for strategic decision-making as the player tries to maximize their profits and survive in the lemonade business.
# -----




# NOTE: Jet was testing random things, and figured out that you can do .lower().strip() in the same line, which was really effecient, and avoided bugs.


# >>>
# >>>
# >>>


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
    

    # NOTE: Lines 154 to 245 is all Customer Preference Calculation and Sales Processing. It calculates how many customers prefer sweet, sour, or balanced lemonade based on the recipe,
    # and then processes sales based on the price and customer preferences, while also updating the player's money and inventory accordingly.



    def calculate_customer_preference():
        # Calculate customer preference based on recipe (Lemons = sour, Sugar = sweet)
        # Ice, and Cups are required to sell, but don't affect preference, just the amount of customers you can sell to

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
                print(f"You have ${money:.2f} Money. \nYour Inventory contains of {ingredients}. \nYou are on Day {day}. \nYour Recipe consists of {Usage}.")
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

                    if enter.lower().strip() == "y":
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

                    elif enter.lower().strip() == "n":
                        print("Cancelling...")

                    else:
                        print("Invalid input... \n")
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
                    print("  - Once Cup is automatically used for one set of lemonade.")
                    print(">>>")
                    print(">>>\n")

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
                            
                            if item.lower().strip() == 'stop':
                                break
                                
                            # Validate ingredient

                            if item.lower() not in ("lemons", "sugar", "ice"):
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
                    print("Final Money: ${money:.2f}")
                    print("Final Day: {day}")
                    print("Final Recipe: {recipe}")
                    print("Final Ingredients: {ingredients}")
                    print("Final Lemonade Price: ${LemonSet:.2f}")
                    print("Exiting...")
                    sys.exit()
                
                if credit_roll.lower().strip() in ("no", "n"):
                    print("Okay, Thanks for Playing!")
                    print("Final Money: ${money:.2f}")
                    print("Final Day: {day}")
                    print("Final Recipe: {recipe}")
                    print("Final Ingredients: {ingredients}")
                    print("Final Lemonade Price: ${LemonSet:.2f}")
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


# ----------------------------------------------------------------------------------------------------------
# When I March through the Artic, The Possibilities are Infinite! - Quote from Matthew Seno (3/3/26): Pre-UIL