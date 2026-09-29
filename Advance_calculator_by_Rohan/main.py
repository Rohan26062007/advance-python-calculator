# Main Program
from basic_operations import add, subtract, multiply
from division_operations import decimal_division, floor_division, remainder
from special_operations import power, factorial, gcd, lcm
from calculation_utilis import get_number, get_integer, display_menu


while True:
    display_menu()
    choice = input("Enter choice (1-10): ").strip()

    if choice=='10':
        print("Thank you for using Advance Python Calculator")
        print("                                   ~made by ROHAN BHOI")
        break

    if choice=='8':
        n = get_integer("Enter a number: ")
        print("The factorial is", factorial(n))
        continue

    if choice == '9':
        num1 = get_integer("Enter first number: ")
        num2 = get_integer("Enter second number: ")
        if num1==0 and num2==0:
            print("GCD and LCM are not defined for 0 and 0.")
        else:
            print("The GCD of given two numbers is", gcd(num1,num2))
            print("The LCM of given two numbers is", lcm(num1,num2))
        continue

    if choice in ('1','2','3','4','5','6','7'):
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice=='1':
            print("Result:", add(num1,num2))

        elif choice=='2':
            print("Result:", subtract(num1,num2))

        elif choice=='3':
            print("Result:", multiply(num1,num2))

        elif choice=='4':
            print("Result:", decimal_division(num1,num2))

        elif choice=='5':
            print("Result:", floor_division(num1,num2))

        elif choice=='6':
            print("Result:", remainder(num1,num2))

        elif choice=='7':
            print("Result:", power(num1,num2))

    else:
        print("Invalid choice,Please enter a number between 1 and 10.")
