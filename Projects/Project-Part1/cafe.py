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
#cafe name and customer's name
def greet(name):
    print(f"Welcome to Python Cafe, {name}!")

customerName = input("What is your name?: ")
greet(customerName)

#is_member True is typed yes ; use .lower()

rewardsMember = input("Are you a rewards member? (yes/no): ").lower()
is_member = (rewardsMember == "yes")

#show_menu(menu)- loops through menu with their price
def show_menu(menu):


       
#while True each time, and ask to pick one

    while True:
        choice = input("Choose an option (1-5): ")
    if choice == '1':
        print("1. View menu")
        print("2. Add an item")
        print("3. Remove an item")
        print("4. View my order")
        print("5. Checkout")
    elif choice == '2':
        print("What would you like? ")
        print("How many? ")
        #print added number of item to your order
    elif choice == '3':
        print("Which item should I remove? ")
        #print remove number of item
    elif choice == '4':
        print("---YOUR ORDER---")
        #show list of items ordered with amount total
        #show total items ordered
    elif choice == '5':
        print("Python Cafe RECEIPT")
    else:
        print(choice = input("Choose an option (1-5): "))
        

#show_order(order, menu) - empty, "Your order is empty." otherwise, prints item name, price and item numbers using len()
#calculate_subtotal(order, menu), loops through order, adds prices and returns total. 
#get_discount(subtotal, is_member), returns discount in dollars using discount rules
def get_discount(subtotal, is_member):
    subtotal = float(input("Enter bill subtotal: "))
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
        
    discount_amount = subtotal * discount
    total = subtotal - discount_amount

print("Subtotal: ")
print("Discount: ")
print("Tax: ")
print("Total: ") #subtotal - discount






#print_receipt(name, order, menu, is_member, calls calculate_subtotal() and get_discount(), tax and total and prints receipt. 

    
choice = input("Choose an option (1-5): ")

print("Thanks for visiting, {name}!")
