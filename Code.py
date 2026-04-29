pizza_list = [
{"Pizza": "Pepperoni", "Price ($)": 13, "GF Free?": True, "Vegan?": False,"Dairy?": False}, 
{"Pizza": "Meat Lovers", "Price ($)": 13, "GF Free?": True, "Vegan?": False,"Dairy?": False}, 
{"Pizza": "Margherita", "Price ($)": 13, "GF Free?": True, "Vegan?": False,"Dairy?": False}, 
{"Pizza": "Vegetarian", "Price ($)": 13, "GF Free?": True, "Vegan?": True,"Dairy?": False}, 
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
"""
def sort(database): 
"""
def view_cart(database): 
    tally = 0
    for items in database:
        tally += 1
        clean_cart = str(items).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
        print(f"\n{tally}. {clean_cart}")


def checkout(database): 
    tally = 0
    for items in database:
        tally += 1
        clean_cart = str(items).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
        print(f"\n{tally}. {clean_cart["Pizza"]} - {clean_cart["Price"]}")

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
                    sort(pizza_list)
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