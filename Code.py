pizza_list = [
{"Pizza": "Pepperoni", "Price": 13, "GF Free?": True, "Vegan?": False,"Dairy?": False}, 
{"Pizza": "Meat Lovers", "Price": 13, "GF Free?": True, "Vegan?": False,"Dairy?": False}, 
{"Pizza": "Margherita", "Price": 13, "GF Free?": True, "Vegan?": False,"Dairy?": False}, 
{"Pizza": "Vegetarian", "Price": 13, "GF Free?": True, "Vegan?": True,"Dairy?": False}, 
]
cart = []
def view_menu(database): 
    print(pizza_list)
def add_item(database): 

def remove_item(database): 

def sort(database): 

def view_cart(database): 
    print(cart)
def checkout(database): 

def exit(): 

def menu_display():
    print(f"\n Welcome to the pizza place!")
    print(f"1. View the Menu ")
    print(f"2. Add item to cart")
    print(f"3. Remove item from cart")
    print(f"4. Sort Menu ")
    print(f"5. View cart")
    print(f"6. Checkout")
    print(f"7. Exit Program")
    
def menu_function()
    while True:
        menu_display()
        while True:
            try:
                choice = int(input(f"What is your choice? "))
                if choice == 7:
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
                    add_item(pizza_list)
                elif choice == 1:
                    view_menu(pizza_list)
                else: 
                    print(f"Invalid choice.")
                    continue
                break
            except ValueError:
                print(f"Invalid choice, please input the corresponding number to your choice (1-6)")
                continue