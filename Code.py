pizza_list = [
{"Pizza": "Pepperoni", "Price": 13, "GF Free?": True, "Vegan?": False,"Dairy?": False}, 
{"Pizza": "Meat Lovers", "Price": 13, "GF Free?": True, "Vegan?": False,"Dairy?": False}, 
{"Pizza": "Margherita", "Price": 13, "GF Free?": True, "Vegan?": False,"Dairy?": False}, 
{"Pizza": "Vegetarian", "Price": 13, "GF Free?": True, "Vegan?": True,"Dairy?": False}, 
]
sides_list = [
{"Side": "Fries", "Price": 8, "GF Free?": False, "Vegan?": True,"Dairy?": False}, 
{"Side": "Pepperoni Wheels", "Price": 8, "GF Free?": False, "Vegan?": False,"Dairy?": False}, 
{"Side": "Garlic Bread", "Price": 8, "GF Free?": False, "Vegan?": True,"Dairy?": False}, 
]
cart = []

def view_menu(database1,database2): 
    print(f"Pizzas:\n")
    print(f"-------------------")
    for pizzas in pizza_list:
        clean_pizzas = str(pizzas).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
        print(f"{clean_pizzas}\n")
    print(f"Sides:\n")
    print(f"-------------------")
    for side in sides_list:    
        clean_sides = str(side).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace('"',"")
        print(f"{clean_sides}\n")

def add_item(database,database2): 
    product = input(f"What items would you like to add, please input the name of the item in text.\n").lower()
    if product == database["Pizza"].lower():
        cart.append(product)
    elif product == database2["Side"].lower(): 
        cart.append(product)

    else: 
        print()
"""
def remove_item(database): 

def sort(database): 
"""
def view_cart(database): 
    print(f"{cart}\n")
"""
def checkout(database): 
"""

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
                    checkout(pizza_list)
                elif choice == 5:
                    view_cart(pizza_list)
                elif choice == 4:
                    sort(pizza_list)
                elif choice == 3:
                    remove_item(pizza_list)
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