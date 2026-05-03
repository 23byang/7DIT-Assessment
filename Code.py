"""This Program acts as a user interface for a pizza shop."""
import random 
pizza_list = [
    {"Pizza": "Pepperoni Pizza", "Price": 13, "GF Free": True, "Vegan": False, "Dairy": True}, 
    {"Pizza": "Meat Lovers Pizza", "Price": 14, "GF Free": True, "Vegan": False, "Dairy": True}, 
    {"Pizza": "Margherita Pizza", "Price": 15, "GF Free": True, "Vegan": False, "Dairy": True}, 
    {"Pizza": "Vegetarian Pizza", "Price": 13, "GF Free": True, "Vegan": True, "Dairy": True}, 
]
sides_list = [
    {"Side": "Fries", "Price": 8, "GF Free": False, "Vegan": True, "Dairy": False}, 
    {"Side": "Pepperoni Wheels", "Price": 8, "GF Free": False, "Vegan": False, "Dairy": False}, 
    {"Side": "Garlic Bread", "Price": 8, "GF Free": False, "Vegan": True, "Dairy": True}, 
    {"Side": "Chicken Fingers", "Price": 8, "GF Free": True, "Vegan": False, "Dairy": False}, 
]
"""Dictionaries in Lists for my data."""
cart = []


def view_menu(database1, database2): 
    """ This function prints the entire menu so that the user can decide on what to order."""
    print("\nPizzas:")
    print("-------------------")
    for pizzas in database1:
        clean_pizzas = str(pizzas).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
        print(f"{clean_pizzas}\n")
    print("\nSides:")
    print("-------------------")
    for side in database2:
        clean_sides = str(side).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
        print(f"{clean_sides}\n")


def add_item(database, database2):
    """This function allows the user to add items from the menu to their cart."""
    product = input("\nWhat items would you like to add, please input the name of the item in text.\n").lower()
    found = False
    for item in database:
        if product == item["Pizza"].lower():
            cart.append(item)
            clean_items = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
            print(f"\nAdded {clean_items} to cart!")
            found = True
            break
    if not found:
        for item in database2:
            if product == item["Side"].lower(): 
                cart.append(item)
                clean_items = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                print(f"\nAdded {clean_items} to cart!")
                found = True
    if not found:
        print("\nSorry, item is not in the menu.")


def remove_item(database):
    """This function allows users to remove items from their cart."""
    tally = 0
    for items in database:
        tally += 1
    view_cart(database)
    if database == []:
        print("Cart Empty, returning to main menu.")
    else:
        try:
            removed_number = float(input("\nPlease input the item you want to remove using their corresponding cart number. "))
            removed_number = int(removed_number)
            if removed_number not in range(1, tally + 1):
                print("\nInvalid Option, please input a whole positive integer corresponding to your choice.")
            else:
                cart.pop(removed_number - 1)
                print("Successfully removed item.")
        except ValueError:
            print("\nInvalid Option, please input a whole positive integer corresponding to your choice.")


def price_extractor(item):
    """This function allows the sort function to work by extracting the price value from the different items, allowing the program to then sort the items."""
    if "Price" in item:
        return item["Price"]
def sort(database, database2):
    """This function allows the user to sort the menu by various conditions, such as price, and dietary specifications."""
    temp_value = True
    temp_value2 = True
    temp_value3 = True
    temp_list = [*database, *database2]
    temp_list2 = database
    temp_list3 = database2
    while temp_value:
        try:
            choice = float(input("Would you like to sort the Whole Menu (1), Pizza Menu (2) or the Sides Menu (3)"))
            choice = int(choice)
            if choice == 1:
                temp_value = False
                while temp_value2:
                    subchoice = float(input("Would you like to sort the selected menu type by price (1), or whether or not the item has a GF Free option (2), Vegan option(3) or has Dairy (4):"))
                    subchoice = int(subchoice)
                    if subchoice == 1:
                        temp_list.sort(key=price_extractor)
                        print("\nSorted Menu:")
                        for item in temp_list:
                            clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                            print(clean_item)
                            temp_value2 = False
                    if subchoice == 2:
                        for item in database:
                            if item["GF Free"] is True:
                                clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                                print(clean_item)
                                temp_value2 = False
                        for item in database2:
                            if item["GF Free"] is True:
                                clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                                print(clean_item)
                                temp_value2 = False
                    if subchoice == 3:
                        for item in database:
                            if item["Vegan"] is True:
                                clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                                print(clean_item)
                                temp_value2 = False
                        for item in database2:
                            if item["Vegan"] is True:
                                clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                                print(clean_item)
                                temp_value2 = False
                    if subchoice == 4:
                        temp_value2 = False
                        while temp_value3:
                            dairy_choice = float(input("Do you want to see items containing dairy (1) or items that do not have dairy (2):"))
                            dairy_choice = int(dairy_choice)
                            if dairy_choice == 1:
                                user_dairy_choice = True
                                temp_value3 = False
                            elif dairy_choice == 2:
                                user_dairy_choice = False
                                temp_value3 = False
                            else:
                                print("Please choose one of the options provided (1 & 2).")
                            for item in database:
                                if item["Dairy"] == user_dairy_choice:
                                    clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                                    print(clean_item)
                            if dairy_choice == 1:
                                user_dairy_choice = True
                                temp_value3 = False
                            elif dairy_choice == 2:
                                user_dairy_choice = False
                                temp_value3 = False
                            for item in database2:
                                if item["Dairy"] == user_dairy_choice:
                                    clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                                    print(clean_item)
            elif choice == 2:
                temp_value = False
                while temp_value2:
                    subchoice = float(input("Would you like to sort the selected menu type by price (1), or whether or not the item has a GF Free option (2), Vegan option(3) or has Dairy (4):"))
                    subchoice = int(subchoice)
                    if subchoice == 1:
                        temp_list2.sort(key=price_extractor)
                        print("\nSorted Menu:")
                        for item in temp_list2:
                            clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                            print(clean_item)
                            temp_value2 = False
                    if subchoice == 2:
                        for item in database:
                            if item["GF Free"] is True:
                                clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                                print(clean_item)
                                temp_value2 = False
                    if subchoice == 3:
                        for item in database:
                            if item["Vegan"] is True:
                                clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                                print(clean_item)
                                temp_value2 = False
                                temp_value2 = False
                    if subchoice == 4:
                        temp_value2 = False
                        while temp_value3:
                            dairy_choice = float(input("Do you want to see items containing dairy (1) or items that do not have dairy (2):"))
                            dairy_choice = int(dairy_choice)
                            if dairy_choice == 1:
                                user_dairy_choice = True
                                temp_value3 = False
                            elif dairy_choice == 2:
                                user_dairy_choice = False
                                temp_value3 = False
                            else:
                                print("Please choose one of the options provided (1 & 2).")
                            for item in database:
                                if item["Dairy"] == user_dairy_choice:
                                    clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                                    print(clean_item)
            elif choice == 3:
                temp_value = False
                while temp_value2:
                    subchoice = float(input("Would you like to sort the selected menu type by price (1), or whether or not the item has a GF Free option (2), Vegan option(3) or has Dairy (4):"))
                    subchoice = int(subchoice)
                    if subchoice == 1:
                        temp_list3.sort(key=price_extractor)
                        print("\nSorted Menu:")
                        for item in temp_list3:
                            clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                            print(clean_item)
                            temp_value2 = False
                    if subchoice == 2:
                        for item in database2:
                            if item["GF Free"] is True:
                                clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                                temp_value2 = False
                    if subchoice == 3:
                        for item in database2:
                            if item["Vegan"] is True:
                                clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                                print(clean_item)
                                temp_value2 = False
                    if subchoice == 4:
                        temp_value2 = False
                        while temp_value3:
                            dairy_choice = float(input("Do you want to see items containing dairy (1) or items that do not have dairy (2):"))
                            dairy_choice = int(dairy_choice)
                            if dairy_choice == 1:
                                user_dairy_choice = True
                                temp_value3 = False
                            elif dairy_choice == 2:
                                user_dairy_choice = False
                                temp_value3 = False
                            else:
                                print("Please choose one of the options provided (1 & 2).")
                            for item in database2:
                                if item["Dairy"] == user_dairy_choice:
                                    clean_item = str(item).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
                                    print(clean_item)
        except ValueError:
            print("Invalid Input, please input one of the provided options")


def view_cart(database): 
    """This functions displays the cart so that the user may reflect on what they have already added. It uses a tally system as to assign items various cart numbers."""
    tally = 0
    for items in database:
        tally += 1
        clean_cart = str(items).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
        print(f"\n{tally}. {clean_cart}")


def checkout(database):
    """This function brings the user to the checkout page, showing them the whole order as well as the price, with a option to finalise purchase or go back to shopping."""
    tally = 0
    total = 0
    for items in database:
        tally += 1
        if "Pizza" in items:
            name = items["Pizza"]
        else:
            name = items["Side"]
        price = items["Price"]
        clean_name = str(name).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
        clean_price = str(price).replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("'", "").replace('"', "")
        print(f"\n{tally}. {clean_name} - ${clean_price}")
        total += int(price)
    print("\n-------------------")
    print(f"\n Total Price : ${total}")
    running = True
    while running:
        try:
            choice = input("Would you like to finalise your purchase? (Yes/No)").lower()
            if choice == "yes":
                print(f"Your order number is {random.randint(1,100)}.")
                running = False
            elif choice == "no":
                running = False
            else:
                print('Invalid Choice, please input ("Yes" or "No")')
        except ValueError:
            print('Invalid Choice, please input ("Yes" or "No")')

def menu_display():
    """This function displays the main menu, and does the visual part of the job."""
    print("\n Welcome to the pizza place!")
    print("1. View the Menu ")
    print("2. Add item to cart")
    print("3. Remove item from cart")
    print("4. Sort Menu ")
    print("5. View cart")
    print("6. Checkout")
    print("7. Exit Program")


def menu_function():
    """This function does the non-visual part of the main menu system, cycling through different inputs until it finds what the user has inputted, where it then runs the appropriate actions."""
    while True:
        menu_display()
        while True:
            try:
                choice = float(input("What is your choice? "))
                choice = int(choice)
                if choice == 7:
                    print("Exiting program.\n")
                    exit()
                elif choice == 6:
                    checkout(cart)
                elif choice == 5:
                    view_cart(cart)
                elif choice == 4:
                    sort(pizza_list, sides_list)
                elif choice == 3:
                    remove_item(cart)
                elif choice == 2:
                    add_item(pizza_list, sides_list)
                elif choice == 1:
                    view_menu(pizza_list, sides_list)
                else: 
                    print("Invalid choice.")
                    continue
                break
            except ValueError:
                print("Invalid choice, please input the corresponding number to your choice (1-7)")
                continue


menu_function()
