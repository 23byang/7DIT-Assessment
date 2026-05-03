import random
pizza_list = [
{"Pizza": "Pepperoni Pizza", "Price": 13, "GF Free?": True, "Vegan?": False,"Dairy?": False}, 
{"Pizza": "Meat Lovers Pizza", "Price": 14, "GF Free?": True, "Vegan?": False,"Dairy?": False}, 
{"Pizza": "Margherita Pizza", "Price": 15, "GF Free?": True, "Vegan?": False,"Dairy?": False}, 
{"Pizza": "Vegetarian Pizza", "Price": 13, "GF Free?": True, "Vegan?": True,"Dairy?": False}, 
]
sides_list = [
{"Side": "Fries", "Price": 8, "GF Free?": False, "Vegan?": True,"Dairy?": False}, 
{"Side": "Pepperoni Wheels", "Price": 8, "GF Free?": False, "Vegan?": False,"Dairy?": False}, 
{"Side": "Garlic Bread", "Price": 8, "GF Free?": False, "Vegan?": True,"Dairy?": False}, 
]
cart = []

def view_menu(database1,database2): 
    print(f"\nPizzas:")
    print(f"-------------------")
    for pizzas in database1:
        clean_pizzas = str(pizzas).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
        print(f"{clean_pizzas}\n")
    print(f"\nSides:")
    print(f"-------------------")
    for side in database2:    
        clean_sides = str(side).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
        print(f"{clean_sides}\n")

def add_item(database,database2): 
    product = input(f"\nWhat items would you like to add, please input the name of the item in text.\n").lower()
    found = False
    for item in database:
        if product == item["Pizza"].lower():
            cart.append(item)
            clean_items = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
            print(f"\nAdded {clean_items} to cart!")
            found = True
            break
    if not found:
            for item in database2:
                if product == item["Side"].lower(): 
                    cart.append(item)
                    clean_items = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
                    print(f"\nAdded {clean_items} to cart!")
                    found = True
    if not found:
        print(f"\nSorry, Item is not in the menu.")

def remove_item(database): 
    view_cart(database)
    try:
        removed_number = float(input(f"\nPlease input the item you want to remove using their corresponding cart number. "))
        removed_number = int(removed_number)
        cart.pop(removed_number - 1)
        print(f"Successfully removed item.")
    except ValueError:
        print(f"\nInvalid Option, please input a whole positive integer corresponding to your choice.")
def price_extractor(item):
    if "Price" in item:
        return item["Price"]
def sort(database,database2): 
    running = True
    temp_list = [*database,*database2]
    temp_list2 = database
    temp_list3 = database2
    while running:
        try:
            choice = int(input(f"Would you like to sort the Whole Menu (1), Pizza Menu (2) or the Sides Menu (3)"))
            if choice == 1:
                running = False
                subchoice = int(input(f"Would you like to sort the selected menu type by price (1), or whether or not the item is GF Free (2), Vegan (3) or Dairy (4)"))
                if subchoice == 1:
                    temp_list.sort(key = price_extractor)
                    print(f"\nSorted Menu:")
                    for item in temp_list:
                        clean_item = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
                        print(clean_item)
                if subchoice == 2:
                    for item in database:
                        if ["GF Free"] == True:
                            clean_item = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
                            print(clean_item)
                if subchoice == 3:
                    for item in database:
                        if ["Vegan"] == True:
                            clean_item = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
                            print(clean_item)
                if subchoice == 4:
                    dairy_choice = input(f"Do you want to see items containing dairy (True/False):")
                    for item in database:
                        if ["Dairy"] == dairy_choice:
                            clean_item = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
                            print(clean_item)
            elif choice == 2:
                running = False
                subchoice = int(input(f"Would you like to sort the selected menu type by price (1), or whether or not the item is GF Free (2), Vegan (3) or Dairy (4)"))
                if subchoice == 1:
                    temp_list2.sort(key = price_extractor)
                    for item in temp_list2:
                        clean_item = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
                        print(f"\nSorted Menu:")
                        print(clean_item)  
                if subchoice == 2:
                    for item in database:
                        if ["GF Free"] == True:
                            clean_item = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
                            print(clean_item)
                if subchoice == 3:
                    for item in database:
                        if ["Vegan"] == True:
                            clean_item = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
                            print(clean_item)
                if subchoice == 4:
                    dairy_choice = input(f"Do you want to see items containing dairy (True/False):")
                    for item in database:
                        if ["Dairy"] == dairy_choice:
                            clean_item = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
                            print(clean_item)
                subchoice = int(input(f"Would you like to sort the selected menu type by price (1), or whether or not the item is GF Free (2), Vegan (3) or Dairy (4)"))
            elif choice == 3:
                running = False
                subchoice = int(input(f"Would you like to sort the selected menu type by price (1), or whether or not the item is GF Free (2), Vegan (3) or Dairy (4)"))
                if subchoice == 1:
                    temp_list3.sort(key = price_extractor)
                    for item in temp_list3:
                        clean_item = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
                        print(f"\nSorted Menu:")
                        print(clean_item)
                if subchoice == 2:
                    for item in database2:
                        if ["GF Free"] == True:
                            clean_item = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
                            print(clean_item)
                if subchoice == 3:
                    for item in database2:
                        if ["Vegan"] == True:
                            clean_item = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
                            print(clean_item)
                if subchoice == 4:
                    dairy_choice = input(f"Do you want to see items containing dairy (True/False):")
                    for item in database2:
                        if ["Dairy"] == dairy_choice:
                            clean_item = str(item).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
                            print(clean_item)
                subchoice = int(input(f"Would you like to sort the selected menu type by price (1), or whether or not the item is GF Free (2), Vegan (3) or Dairy (4)"))                
        except ValueError:
            print(f"Invalid Input, please input one of the provided options")
def view_cart(database): 
    tally = 0
    for items in database:
        tally += 1
        clean_cart = str(items).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
        print(f"\n{tally}. {clean_cart}")


def checkout(database): 
    tally = 0
    total = 0
    for items in database:
        tally += 1
        if "Pizza" in items:
            name = items["Pizza"]
        else:
            name = items["Side"]
        price = items["Price"]
        clean_name = str(name).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
        clean_price = str(price).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
        print(f"\n{tally}. {clean_name} - ${clean_price}")
        total += int(price)
    print(f"\n-------------------")
    print(f"\n Total Price : {total}")
    running = True
    while running:
        try:
            choice = input(f"Would you like to finalise your purchase? (Yes/No)").lower()
            if choice == "yes":
                print(f"Your order number is {random.randint(1,100)}.")
                running = False
            elif choice == "no":
                running = False
            else:
                print(f'Invalid Choice, please input ("Yes" or "No")')

        except ValueError:
            print(f'Invalid Choice, please input ("Yes" or "No")')

def menu_display():
    print(f"\n Welcome to the pizza place!")
    print(f"1. View the Menu ")
    print(f"2. Add item to cart")
    print(f"3. Remove item from cart")
    print(f"4. Sort Menu ")
    print(f"5. View cart")
    print(f"6. Checkout")
    print(f"7. Exit Program")
    
def menu_function():
    while True:
        menu_display()
        while True:
            try:
                choice = float(input(f"What is your choice? "))
                choice = int(choice)
                if choice == 7:
                    print(f"Exiting program.\n")
                    exit()
                elif choice == 6:  
                    checkout(cart)
                elif choice == 5:
                    view_cart(cart)
                elif choice == 4:
                    sort(pizza_list,sides_list)
                elif choice == 3:
                    remove_item(cart)
                elif choice == 2:
                    add_item(pizza_list,sides_list)
                elif choice == 1:
                    view_menu(pizza_list,sides_list)
                else: 
                    print(f"Invalid choice.")
                    continue
                break
            except ValueError:
                print(f"Invalid choice, please input the corresponding number to your choice (1-7)")
                continue
menu_function()