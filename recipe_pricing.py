#-------
lemon_set = 0
recipe = []
#-------
def whattodo():
  global lemon_set
  global each
  print("What would you like to do?")
  when = input("(1) Shop, (2) Change price (3) Change recipe (EXIT) to exit:")
  if when == "1":
    shop()
  if when == "2":
    print("You have decided to change the price of your lemonade!")
    lemon_set = int(input("What would you like to change your price to? - "))
  if when == "3":
    print("You have decided to change your recipe!")
    recipe.append = str(input(f"What would you like to have in your ingredients?"))
    for each in (1,recipe):
      print(f"You have added {recipe}")
    else: 
      print("Please try again")
      when()
#-------
whattodo()
