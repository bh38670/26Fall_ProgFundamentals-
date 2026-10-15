cafe_name = "Python Café"
tax_rate = 0.08
#dictionary
menu = {
    "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25,
}

order = []

#\n will add a space after the question
#cafe name and customer's name
def greet(name):
    print(f"Welcome to {cafe_name}, {name}!")

customerName = input("What is your name?: ")
greet(customerName)

#is_member True is typed yes ; use .lower()
rewardsMember = input("Are you a rewards member? (yes/no): ").lower()
is_member = (rewardsMember == "yes")
#is_member = True
#if is_member:
#    print("Is a member")

#show_menu(menu)- loops through menu with their price
def show_menu(menu):
    print("---MENU---")
    for item, price in menu.items():
        print(f"{item.title()}: ${price:.2f}")

#show_order(order, menu) - empty, "Your order is empty." otherwise, prints item name, price and item numbers using len()
def show_order(order, menu):
    if len(order) == 0:
        print("Your order is empty.")
    else:
        print("---YOUR ORDER---")
        for item in order:
            print(f"{item.title()}: ${menu[item]:.2}")
        print(f"Total items ordered: {len(order)}")

#calculate_subtotal(order, menu), loops through order, adds prices and returns total. 
def calculate_subtotal(order, menu):
    total = 0
    for item in order:
        if item in menu:
            total += menu[item]
    return total

def print_receipt(name, order, menu, is_member):
    print(f"---{cafe_name} RECEIPT---")
    print(f"Customer: {name}")
       
#list menu for user to choose from
user_options = [
       "1. View menu",
       "2. Add an item",
       "3. Remove an item",
       "4. View my order",
       "5. Checkout",
]
for options in user_options:
    print(options)
    
#while True each time, and ask to pick one
while True:
    choice = input("Choose an option (1-5): ")
    
    if choice == '1':
        show_menu(menu)
        
    elif choice == '2':
        menu_item = input("What would you like? ").lower()
        if menu_item in menu:
          total_items = int(input("How many? "))
          if total_items > 0:
              for i in range(total_items):
                  order.append(menu_item)
              print(f"Added {total_items} {menu_item} to your order.")
          else:
                print("Please add an item")
        else:
                print("Item is not on the menu. Please try again.")
            
#print remove number of item       
    elif choice == '3':
        remove_item = input("Which item should I remove? ").lower()
        
        if remove_item in order:
            order.remove(remove_item)
            print(f"Removed one {remove_item}")
        else:
            print("That item is not in your order.")
       
    elif choice == '4':
        show_order(order, menu)
        
    elif choice == '5':
        if len(order) == 0:
            print("Your order is empty. Please add an item.")
        else:
            print_receipt(customerName, order, menu, is_member)
            break
    else:
        print(choice = input("Choose an option (1-5): "))

#get_discount(subtotal, is_member), returns discount in dollars using discount rules
def get_discount(subtotal, is_member):
    is_member = True
    discount = 0
    
    if is_member:
        if subtotal >= 20:
            discount = subtotal * .15
        elif 10 <= subtotal >= 20:
            discount = subtotal * .10
    elif subtotal >= 25:
        discount = subtotal * 0.05
    else:
        discount = 0
    return discount
        
    #discount_amount = subtotal * discount
    #total = subtotal - discount_amount
subtotal = calculate_subtotal(order, menu)
discount = get_discount(subtotal, is_member)
tax = (subtotal - discount) * tax_rate
total = (subtotal - discount) + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}") #subtotal - discount

#print_receipt(name, order, menu, is_member, calls calculate_subtotal() and get_discount(), tax and total and prints receipt. 

    
choice = input("Choose an option (1-5): ")

print("Thanks for visiting, {name}!")
