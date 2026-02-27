

Usage = {}

def price(money):
    global Usage
    recipe_items = []
    print("Enter your recipe items (type 'done' when finished):\n")
    while True:
        item = input("What would you like to add to your recipe? (Type STOP to Stop)\n")
        if item.lower() == 'STOP':
            break
        recipe_items.append(item)
        print(f"Added: {item}")
    
    Usage["recipe"] = recipe_items
    print(f"Your Item was added to you Recipe: {Usage}")
