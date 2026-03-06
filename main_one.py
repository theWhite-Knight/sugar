# ~ The Lemonade Stand Game ~


# This is basically a Dictionary for terms or code you don't know, or just a general explanation of how the code works.
# All the terms were double checked to make sure they are correct.


# >>>
# >>>
# >>>


# NOTE: "Abs" - stands for "Absolute Value" which is a mathematical function that returns the non-negative value of a number. 
# In the context of the customer preference calculation, it is used to determine how far the lemon or sugar ratio is from a balanced 0.5, which helps to calculate how many 
# customers prefer sweet, sour, cold, or balanced lemonade based on the recipe.
# -----
# Except KeyboardInterrupt - is used to allow the user to exit the game gracefully by pressing Ctrl + C. When this happens, 
# it will print "Exiting..." and then terminate the program using sys.exit(). It gets rid of the SyntaxError that would normally occur when a user tries to exit the game by pressing Ctrl + C, 
# and allows for a cleaner exit experience, and doesn't look like there are errors in the code.
# -----
# Except ValueError - is used to catch cases where the user inputs something that cannot be converted to a number (like letters or symbols) 
# when setting the lemonade price or adding ingredients to the recipe. When this happens, it will print "Please enter a valid number!" and prompt the user to try again, 
# preventing the program from crashing due to invalid input.
# -----
# The Sour + Sweet ratio is calculated to determine customer preferences. If the lemonade is too sour (high lemon ratio) or too sweet (high sugar ratio), 
# it will affect how many customers are willing to buy the lemonade and how much they are willing to pay.
# The game encourages players to find a balance in their recipe to maximize sales.
# -----
# Random.uniform - is used to add variability to customer willingness to pay, making the game more dynamic and less predictable. Basically, its just a better 
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
# .Strip() - is used to remove any leading or trailing whitespace from the user's input when they type "exit" to leave the shop. 
# This ensures that even if the user accidentally adds extra spaces before or after "exit"
# -----
# .Lower() - is used to convert the user's input to lowercase when they type "exit" to leave the shop. This allows the program to recognize "EXIT", "Exit", "eXit", etc. as valid commands to exit the shop, 
# making it more user-friendly and flexible in accepting input.
# -----
# InInstance() - is used to check if the lemonade price (LemonSet) is a valid number (either an integer or a float) and greater than 0 before allowing the player to start the sales day.
# This validation ensures that the player has set a proper price for their lemonade, which is essential for the game to function correctly. 
# If the price is not valid, the game will prompt the player to try again, preventing potential errors during the sales process.
# -----
# The game loop - ( - Main_Game() - ) is structured to allow the player to manage their lemonade stand over multiple days. Each day, the player can choose to shop for ingredients, change their recipe, adjust their pricing, 
# or start the sales day. The loop continues until the player has completed 7 days of business, at which point they can choose to roll credits or exit the game.
# This structure provides a clear progression and allows for strategic decision-making as the player tries to maximize their profits and survive in the lemonade business.
# -----
# The customer preference calculation and sales processing are key components of the game that determine how successful the player's lemonade stand is each day. 
# If the player creates a recipe that is too sour or too sweet, they may lose potential customers. 
# Finding the right balance in the recipe is crucial for attracting a wider range of customers and maximizing sales. 
# The randomness in customer willingness to pay adds an element of unpredictability, making the game more engaging and challenging. 
# -----
# [Item.capitalize()] - is used to ensure that the ingredient names in the recipe are consistently formatted with a capital first letter (e.g., "Lemons" instead of "lemons").
# This helps maintain a clean and professional appearance in the game's output when displaying the recipe and ingredients, 
# and also ensures that the ingredient names match the keys used in the ingredients dictionary for accurate tracking and updates.
# -----
# [Recipe_items.append - (item.capitalize())] is used to build a list of the ingredients and their amounts in the current recipe. This list is then stored in the Usage dictionary under the key "recipe".
# This allows the game to keep track of the current recipe configuration, which is important for calculating customer preferences and processing sales based on the ingredients used in the lemonade.
# -----
# Math.ceil - (sell_to_customers) is used to round up the number of cups sold to the nearest whole number. 
# Since you can't sell a fraction of a cup of lemonade, this ensures that the sales are represented as whole units, which is more realistic and makes the game easier to understand for players.
# -----
# .count("Ice") // 2 - is used to calculate how much ice is used per cup of lemonade sold. In this case, it assumes that half an ice cube is used for each cup sold.
# This is a simple way to track the usage of ice in the sales process, ensuring that the player's inventory is updated correctly as they sell lemonade to customers.
# -----
# max(0, ingredients["Lemons"] - (recipe["Lemons"] // 10)) - is used to update the inventory of lemons after selling lemonade. 
# It subtracts a portion of the lemons used in the recipe from the player's inventory,
# while ensuring that the inventory does not go negative. The // 10 is a simple way to represent the amount of lemons used per cup of lemonade sold, 
# and max(0, ...) ensures that if the player runs out of lemons, it won't go into negative numbers, which could cause errors in the game.
# -----
# .get("Lemons", 0) - is used to safely access the number of lemons in the recipe dictionary. If the "Lemons" key does not exist in the recipe, it will return 0 instead of causing a KeyError.
# This allows the game to handle cases where the player has not added any lemons to their recipe without crashing, and
# it ensures that the customer preference calculation can still proceed even if certain ingredients are missing from the recipe.
# -----
# Datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S') - is used to display the current date and time in a specific format (day-month-year hours:minutes:seconds) 
# when a new day begins in the game.This adds a nice touch of realism to the game, 
# allowing players to see the passage of time as they manage their lemonade stand over multiple days. It also enhances the 
# immersive experience by providing a real-time element to the gameplay.
# ------
# .strftime('%Y-%m-%d %H:%M:%S') - is an alternative date format (year-month-day hours:minutes:seconds) that can be used to display the current date and time.
# The choice of date format is a matter of preference, and both formats are commonly used. In this game, the '%d-%m-%Y' format is used to display the date in a more 
# traditional day-first format, which may be more familiar to some players.
# ------
# .now() - is a method from the datetime module that returns the current local date and time. In this game, it is used to display the real-world date and time when a new day begins in the game.



# >>>
# >>>
# >>>

# Cheat Codes:

# Don't work yet

# - ("ENDOFLINE    - Gives a lot of Money")
# - ("ADMIN_ABUSE  - Gives 100 ingredients of Lemons, Sugar, Ice, and Cups + Money")
# - ("AreWeSerious?! - Times the Player income by 1.2x")


# ANOUNCEMENT: The Game is now FULLY WORKING, and just need to patch a couple of bugs you can do to crash the code.



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
    "balanced": 0,
    "cold": 0
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

# ------

    # NOTE: The next section is all Customer Preference Calculation and Sales Processing. It calculates how many customers prefer sweet, sour, or balanced lemonade based on the recipe,
    # and then processes sales based on the price and customer preferences, while also updating the player's money and inventory accordingly.



def calculate_customer_preference():
    global customer_preferences
    
    lemons = recipe.get("Lemons", 0)
    sugar = recipe.get("Sugar", 0)
    Ice = recipe.get("Ice", 0)

    # Basic validation

    if lemons == 0 or sugar == 0 or Ice == 0:
        print("\n WARNING: Your recipe must include Lemons, Sugar, and Ice!")
        return 0

    total = lemons + sugar + Ice

    if total == 0:
        return 0

    lemon_ratio = lemons / total
    sugar_ratio = sugar / total
    ice_ratio = Ice / total

    # Reset preferences
    
    customer_preferences["sweet"] = 0
    customer_preferences["sour"] = 0
    customer_preferences["balanced"] = 0
    customer_preferences["cold"] = 0

    # Sweet / Sour / Balanced logic based on lemon and sugar ratios. The more sour the lemonade (higher lemon ratio), the more customers will prefer sour lemonade.
    # The more sweet the lemonade (higher sugar ratio), the more customers will prefer sweet lemonade.
    #  A balanced recipe will attract a more even distribution of customer preferences. 
    # The exact numbers are determined by the ratios and some randomness to make it more fun and less robotic.

    if lemon_ratio > 0.7:
        customer_preferences["sweet"] = int(10 * sugar_ratio)
        customer_preferences["sour"] = int(30 * lemon_ratio)
        customer_preferences["balanced"] = int(10 * (1 - abs(lemon_ratio - 0.5)))
        print(f"\n Customer Preference: VERY SOUR ({lemons} lemons, {sugar} sugar)")

    elif lemon_ratio > 0.5:
        customer_preferences["sweet"] = int(20 * sugar_ratio)
        customer_preferences["sour"] = int(25 * lemon_ratio)
        customer_preferences["balanced"] = int(15 * (1 - abs(lemon_ratio - 0.5)))
        print(f"\n Customer Preference: SOUR ({lemons} lemons, {sugar} sugar)")

    elif sugar_ratio > 0.7:
        customer_preferences["sweet"] = int(30 * sugar_ratio)
        customer_preferences["sour"] = int(10 * lemon_ratio)
        customer_preferences["balanced"] = int(10 * (1 - abs(sugar_ratio - 0.5)))
        print(f"\n Customer Preference: VERY SWEET ({lemons} lemons, {sugar} sugar)")

    elif sugar_ratio > 0.5:
        customer_preferences["sweet"] = int(25 * sugar_ratio)
        customer_preferences["sour"] = int(20 * lemon_ratio)
        customer_preferences["balanced"] = int(15 * (1 - abs(sugar_ratio - 0.5)))
        print(f"\n Customer Preference: SWEET ({lemons} lemons, {sugar} sugar)")

    else:
        customer_preferences["sweet"] = 20
        customer_preferences["sour"] = 20
        customer_preferences["balanced"] = 20
        print(f"\n Customer Preference: BALANCED ({lemons} lemons, {sugar} sugar)")

    # Cold preference (ICE ONLY)

    customer_preferences["cold"] = int(20 * ice_ratio)

    # Round to whole customers

    customer_preferences["sweet"] = math.ceil(customer_preferences["sweet"])
    customer_preferences["sour"] = math.ceil(customer_preferences["sour"])
    customer_preferences["cold"] = math.ceil(customer_preferences["cold"])
    customer_preferences["balanced"] = math.ceil(customer_preferences["balanced"])

    # Total customers and percentages
    total_customers = (
        customer_preferences["sweet"]
        + customer_preferences["sour"]
        + customer_preferences["balanced"]
        + customer_preferences["cold"]
    )

    customer_preferences["total"] = total_customers

    if total_customers > 0:
        customer_preferences["sweet_percent"] = (customer_preferences["sweet"] / total_customers) * 100
        customer_preferences["sour_percent"] = (customer_preferences["sour"] / total_customers) * 100
        customer_preferences["balanced_percent"] = (customer_preferences["balanced"] / total_customers) * 100
        customer_preferences["cold_percent"] = (customer_preferences["cold"] / total_customers) * 100
    else:
        customer_preferences["sweet_percent"] = 0
        customer_preferences["sour_percent"] = 0
        customer_preferences["balanced_percent"] = 0
        customer_preferences["cold_percent"] = 0

    # Total potential customers based on recipe quality

    return min(50, (lemons + sugar + Ice) * 2)

# ------

def sell_to_customers(price, potential_customers):
    global money, ingredients, recipe, customer_preferences

    if ingredients["Ice"] <= 0:
        print("\n WARNING: You need ice to sell lemonade!")
        return 0
    
    if ingredients["Cups"] <= 0:
        print("\n WARNING: You need cups to sell lemonade!")
        return 0
    
    if ingredients["Lemons"] <= 0:
        print("\n WARNING: You need lemons to sell lemonade!")
        return 0
    
    if ingredients["Sugar"] <= 0:
        print("\n WARNING: You need sugar to sell lemonade!")
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
                ingredients["Ice"] = max(0, ingredients["Ice"] - (recipe["Ice"] // 2))

                # Stop if we run out mid‑sales

                if (
                    ingredients["Cups"] <= 0
                    or ingredients["Ice"] <= 0
                    or ingredients["Lemons"] <= 0
                    or ingredients["Sugar"] <= 0
                ):
                    return sold
                
    return sold



# -----



def game():
    ask_user = True
    global day
    global money
    global ingredients
    global recipe
    global Usage

    while day < 7:
        print("New Day...")
        

        # Prints the Actual Time of Day In Real Life

        print(f"The time of day is: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
        
        print(">>>")
        print(">>>\n")

        print("The Time in-game is 8:00 AM. Time to set up your stand and get ready for the day!")

        try:

            while ask_user == True:
                LemonSet = float(input("What would you like to set your Lemonade price to?\n   (Note: You can change this later, and add decimals to the hundreths place, For example 2.99)\nNOTE: Don't add a Dollar Sign $\n"))
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


            print(f"You have ${money:.2f} Money. \nYour Inventory contains of {ingredients}. \nYou are on Day {day}. \nYour Base Recipe consists of {Usage}.\n(You can change your Recipe in the Menu)")
            print(f"Your Lemonade is currently priced at ${LemonSet:.2f} per cup of Lemonade.\n(You can change your Price in the Menu)")

            print("\nNOTE: You cannot start the sales day if your Lemonade Price equals 0, and if your Recipe doesn't have Lemons, Ice, and Sugar with a set amount of each")
            print("NOTE: After selling, you will have to scroll up to see your full sales results, customer preferences, and remaining inventory\n")
            print(">>>")
            print(">>>")
            print("-----------------------------------------------------------------------------------------------------------------")

            try:
                what = input("What would you like to do? (1) Shop, (2) change recipe, (3) Change pricing, (4) Start the day.\n")

            except KeyboardInterrupt:
                print("\nExiting...")
                sys.exit()
            #-------

            # --- Cheat Codes --- #

            if what.lower().strip() == "ENDOFLINE":
                money += 1000
                print("Cheat code activated: ENDOFLINE - You gained $1000!")
                continue

            if what.lower().strip() == "ADMIN_ABUSE":
                money += 500
                ingredients["Lemons"] += 100
                ingredients["Sugar"] += 100
                ingredients["Cups"] += 100
                ingredients["Ice"] += 100
                print("Cheat code activated: ADMIN_ABUSE - You gained $500 and 100 of each ingredient!")
                continue

            if what.lower().strip() == "AreWeSerious?!":
                money *= 1.2
                print("Cheat code activated: AreWeSerious?! - Your Money is now Multiplied by 1.2x!")
                continue

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
                    print("Entering shop...")

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

            elif what == "2":
                print("--------------------------------------------------")
                print("You chose to change your recipe") # Recipe
                
                print("\n Recipe Guide:")
                print(">>>")
                print(">>>\n")
                print("  - Lemons add SOURNESS (customers who like sour will pay more)")
                print("  - Sugar adds SWEETNESS (customers who like sweet will pay more)")
                print("  - Ice adds COLDNESS (customers who like cold will pay more)")
                print("  - Balanced recipes (with a good mix of Lemons, Sugar, and Ice) will attract more customers overall")
                print("  - Balance is key! Too much of either may reduce customers.")
                print("  - Ice, Lemons, and Sugar are ALL REQUIRED to sell lemonade\n")
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
                print("You chose to change your lemonade price")

                try:
                    LemonSet = float(input("What would you like to set your lemonade price to?\n "))

                    if LemonSet > 0.01:
                        print(f"You set your lemonade price to ${LemonSet:.2f}!")

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

                    if recipe["Lemons"] == 0 and recipe["Sugar"] == 0 and recipe["Ice"] == 0:
                        print(" You need to set up your recipe first! Go to option 2.")
                        return
                    
                    # Check if we have ingredients to sell

                    if ingredients["Cups"] == 0:
                        print(" You need cups to sell lemonade! Visit the shop.")
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
                        print(f"\n You sold {sold:.2f} cups of lemonade!")
                        print(f" You earned ${sold * LemonSet:.2f}")
                        print(f" Current money: ${money:.2f}")
                        print(f" Remaining ingredients: {ingredients}")
                        print("------------------------------------------------------------------------------------------------------------------")
                        print(f"{customer_preferences['sweet']:.1f} customers preferred sweet lemonade ({customer_preferences['sweet_percent']:.2f}%)")
                        print(f"{customer_preferences['sour']:.1f} customers preferred sour lemonade ({customer_preferences['sour_percent']:.2f}%)")
                        print(f"{customer_preferences['cold']:.1f} customers preferred cold lemonade ({customer_preferences['cold_percent']:.2f}%)")
                        print(f"{customer_preferences['balanced']:.1f} customers preferred balanced lemonade ({customer_preferences['balanced_percent']:.2f}%)")
                        print("------------------------------------------------------------------------------------------------------------------")
                        
                    else:
                        print("\n No customers bought your lemonade! Check your recipe.")
                    
                    day += 1
                    print(f"\nDay {day} begins!")

                #-------

                startday()



    
    if day >= 7:
        print("--------------------------------------------------")
        print(" ----- End Of Week Sale Results ----- ")
        print("Congrats, You have survived 7 Days of Buisness")

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
            time.sleep(2)
            print("Thanks for Playing!")
            print(f"Final Money: ${money:.2f}")
            print(f"Final Day: {day}")
            print(f"Final Recipe: {recipe}")
            print(f"Final Ingredients: {ingredients}")
            print(f"Final Lemonade Price: ${LemonSet:.2f}")
            print("Exiting...")
            time.sleep(2)
            sys.exit()
            
        
        if credit_roll.lower().strip() in ("no", "n"):
            print("Okay, Thanks for Playing!")
            time.sleep(0.75)
            print(f"Final Money: ${money:.2f}")
            print(f"Final Day: {day}")
            print(f"Final Recipe: {recipe}")
            print(f"Final Ingredients: {ingredients}")
            print(f"Final Lemonade Price: ${LemonSet:.2f}")
            time.sleep(2)
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

