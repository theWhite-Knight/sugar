import sys


def o(money,ingredients,shop):
    play = input("Would you like to enter the shop? - ")

    if play == "Yes" or "yes" or "Y" or "y" or "ok" or "Ok":
        print("Entering shop...")
        exit_code = 0
        while True:
            print(f"\nYou have {ingredients}.")
            print(">>>")
            print(f"You have {money} dollars.")
            money, exit_code = shop(ingredients,money)
            if exit_code == -1:
                break

    if play == "no" or "No" or "n" or "N":
        print("Cancelling...")


    if money <= 0:
        print("You lost!")
        print("------------------")
        print("GAME OVER!")
        sys.exit()

