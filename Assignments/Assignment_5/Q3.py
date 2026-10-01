def check_number(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
number = int(input("Enter a whole number: "))

print(f"{number} is an {check_number(number)} number.")
