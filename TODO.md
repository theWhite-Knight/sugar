# Fix Plan for main_one.py

## Issues to Fix:
1. Import `todo` function from ToDoList.py
2. Import `set_globals` and `S` functions from welcomeToShop.py
3. Fix syntax error in recipe input (line ~122): `if item.lower() not in ("Lemons" or "Ice" or "Sugar" or "Cups")` should use `not in` with a tuple
4. Add customer preference system based on:
   - Lemons = sourness
   - Sugar = sweetness
   - Customer preference varies based on lemon/sugar ratio

## Implementation Steps:
1. Add imports at the top of main_one.py
2. Fix the recipe input syntax
3. Add customer_preference function that calculates preference based on recipe
4. Update the "Start the day" logic to use customer preference

