Usage = {}



def price(money):
  lemonset = input("What would your price like to be?\n")
  if lemonset <= -1:
    print("Please try again!")
    price(money)