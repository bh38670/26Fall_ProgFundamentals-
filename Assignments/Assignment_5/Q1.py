#write a function with one parameter
def greet_user(name):
    print(f"Helo, {name}! Welcome aboard.")
    
#ask user for their name 
user_name = input("What is your name?: ")

#call function with that variable
greet_user(user_name)
