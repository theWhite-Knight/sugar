from customer_class import Customer
#-------
numver = 1
customerlist = []
newcustomer= Customer()
#-------
for i in range(5):
    customerlist.append(Customer())
#-------
print(">>>\n"">>>\n")
print(f"The customer's preferred sugar content is {newcustomer.get_customer_attributes()['sugar']}")
print(f"The customer's preferred ice content is {newcustomer.get_customer_attributes()['ice']}")
print(f"The customer's preferred price is {newcustomer.get_customer_attributes()['price']}")
print("\n>>>")
#-------
for k in customerlist:
    for each in ["sugar","ice","price"]:
        print(">>>\n")
        print(f"Customer {numver} has prefrence for {each} is {k.get_customer_attributes()[each]}\n")
    numver += 1