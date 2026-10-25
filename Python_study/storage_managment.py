inventory = {"Milk Tea":
             {"price": 15,
              "quantity": 20},
              "Coffee": {
                  "price": 18,
                  "quantity": 15
              },
              "Lemon Tea": {
                  "price": 12,
                  "quantity": 10
              }
              }
def add_product():
   product_name = input("Product name: ")
   price = float(input("Price: "))
   quantity = int(input("Quantity: "))

   inventory[product_name] = {"price": price, "quantity": quantity}

   print("Product added successfully!")
   print(inventory)

#Stock in
def stock_in():
    product_name = input("Product name to stock in:")

    if product_name not in inventory:
       print("Product not found!")
       return
    
    amount = int(input("Quantity to add: "))

    if amount <= 0:
        print("Quantity must be greater than 0!")
    else:
        inventory[product_name]["quantity"]+= amount
        print("Stock updated successfully!")
        print("New quantity:", inventory[product_name]["quantity"])

#Stock Out
def stock_out():
    product_name = input("Product name to stock out:")

    if product_name not in inventory:
       print("Product not found!")
       return
    
    amount = int(input("Quantity to remove: "))

    if amount <= 0:
        print("Quantity must be greater than 0!")
    elif amount > inventory[product_name]["quantity"]:
        print("Insufficient stock!")
        
    else:
        inventory[product_name]["quantity"] -= amount
        print("Stock removed successfully!")
        print("New quantity:", inventory[product_name]["quantity"])

#Check Stock
def check_stock():
    product_name = input("Product name to check stock:")

    if product_name not in inventory:
       print("Product not found!")
    else:
        print("Product:", product_name)
        print("Price:", inventory[product_name]["price"])
        print("Quantity:", inventory[product_name]["quantity"])

#Low Stock Alert
def Low_Stock_Alert():
    for product_name in inventory:
        if inventory[product_name]["quantity"] <= 5:
            print("Low Stock Alert! Product:", product_name, "Quantity:", inventory[product_name]["quantity"])

#View Inventory
def View_Inventory():
    for product_name in inventory:
        print("Product:", product_name)
        print("Price:", inventory[product_name]["price"])
        print("Quantity:", inventory[product_name]["quantity"])

#Menu System
while True:
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. Check Stock")
    print("5. Low Stock Alert")
    print("6. View Inventory")
    print("7. Exit")
    choice = input("Please select an option:")
    if choice == "1":
        add_product()
    elif choice == "2":
        stock_in()
    elif choice == "3":
        stock_out()
    elif choice == "4":
         check_stock()
    elif choice == "5":
         Low_Stock_Alert()
    elif choice == "6":
         View_Inventory()
    elif choice == "7":
         print("Exiting the program.")
         break
    else:
         print("Invalid option!")