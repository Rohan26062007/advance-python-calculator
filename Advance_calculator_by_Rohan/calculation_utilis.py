# Calculator Utility Functions
def get_number(number):
    while True:
        try:
            return float(input(number))
        except ValueError:
            print("Invalid input,Please enter a number.")


def get_integer(number):
    while True:
        try:
            return int(input(number))
        except ValueError:
            print("Invalid input,Please enter an integer.")


def display_menu():
    print("\n==> WELCOME TO ADVANCE PYTHON CALCULATOR <==")
    print()
    print("Select an operation")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiplication (*)")
    print("4. Decimal Division (/)")
    print("5. Floor Division (//)")
    print("6. Remainder (%)")
    print("7. Power (x^y)")
    print("8. Factorial (n!)")
    print("9. GCD and LCM")
    print("10. Exit")

