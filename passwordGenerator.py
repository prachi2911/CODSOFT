import random
import string
from colorama import init, Fore, Style

init(autoreset=True)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print(Fore.CYAN + Style.BRIGHT + "==============================")
    print(Fore.CYAN + Style.BRIGHT + "   Password Generator")
    print(Fore.CYAN + Style.BRIGHT + "==============================")

    try:
        length = int(input(Fore.YELLOW + "Enter the desired length of the password: "))
        if length < 1:
            print(Fore.RED + "Length must be a positive integer.")
            return
        
        password = generate_password(length)
        print(Fore.GREEN + Style.BRIGHT + f"\nGenerated Password: {Fore.WHITE + password}")
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")

if __name__ == "__main__":
    main()
