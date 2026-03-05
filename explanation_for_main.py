# ~ The Lemonade Stand Game ~
# This is basically a Dictionary for terms or code you don't know, or just a general explanation of how the code works.
# All the terms were double checked to make sure they are correct.
# >>>
# NOTE: "Abs" - stands for "Absolute Value" which is a mathematical function that returns the non-negative value of a number. 
# In the context of the customer preference calculation, it is used to determine how far the lemon or sugar ratio is from a balanced 0.5, which helps to calculate how many 
# customers prefer sweet, sour, or balanced lemonade based on the recipe.
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
# Datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S') - is used to display the current date and time in a specific format (day-month-year hours:minutes:seconds) when a new day begins in the game.
# This adds a nice touch of realism to the game, allowing players to see the passage of time as they manage their lemonade stand over multiple days. It also enhances the 
# immersive experience by providing a real-time element to the gameplay.
# ------
# .strftime('%Y-%m-%d %H:%M:%S') - is an alternative date format (year-month-day hours:minutes:seconds) that can be used to display the current date and time.
# The choice of date format is a matter of preference, and both formats are commonly used. In this game, the '%d-%m-%Y' format is used to display the date in a more traditional day-first format, 
# which may be more familiar to some players.
# ------
# .now() - is a method from the datetime module that returns the current local date and time. In this game, it is used to display the real-world date and time when a new day begins in the game.
# >>>
# print("ENDOFLINE    - Gives a lot of Money")
# print("ADMIN_ABUSE  - Gives 100 ingredients of Lemons, Sugar, Ice, and Cups + Money")
# print("AreWeSerious?! - Times the Player income by 1.2x")