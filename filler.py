from welcomeToShop import shop
def enterShop():
    enter = input("Would you like to enter the shop? :\n")
    if enter.lower() == "y":
        print("Entering shop...")
        shop()
        while True:
            exit_code = 0
            print(f"\nYou have {ingredients}.")
            print(">>>")
            print(f"You have {money} dollars.")
            money, exit_code = shop()
            if exit_code == -1:
                break
                
        
    #-------
    if play.lower() == "n":
        print("Cancelling...")
    #-------
    if money <= 0:
        print("You lost!")
        print("------------------")
        print("GAME OVER!")
        sys.exit()