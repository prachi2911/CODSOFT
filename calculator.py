from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def show_menu():
    print(Fore.CYAN + Style.BRIGHT + "\n==============================")
    print(Fore.CYAN + Style.BRIGHT + "   Simple Calculator")
    print(Fore.CYAN + Style.BRIGHT + "==============================")
    print(Fore.YELLOW + Style.BRIGHT + "Select operation:")
    print(Fore.YELLOW + "1. Addition (+)")
    print(Fore.YELLOW + "2. Subtraction (-)")
    print(Fore.YELLOW + "3. Multiplication (*)")
    print(Fore.YELLOW + "4. Division (/)")

def main():
    show_menu()
    
    try:
        choice = input(Fore.CYAN + "\nEnter your choice (1/2/3/4): ")

        if choice not in ['1', '2', '3', '4']:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 4.")
            return

        num1 = float(input(Fore.YELLOW + "Enter the first number: "))
        num2 = float(input(Fore.YELLOW + "Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'
        
        print(Fore.GREEN + Style.BRIGHT + f"\nResult: {Fore.CYAN + str(num1)} {operation} {Fore.CYAN + str(num2)} = {Fore.WHITE + str(result)}")

    except ValueError:
        print(Fore.RED + "Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
