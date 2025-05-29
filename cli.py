from app.ui.main_menu import main_menu
from app.ui.customer_menu import *
from app.ui.provider_menu import *
from app.ui.subscription_menu import *
from app.ui.utils import *

def main():
    while True:
        main_menu()
        choice = input_prompt("Enter your choice: ").strip()

        if choice == '0':
            print_success("[underline]*** Goodbye! ***[/underline]")
            break
        elif choice == '1':
            customer_menu()
        elif choice == '2':
            provider_menu()
        elif choice == '3':
            subscription_menu()
        else:
            print_error("Invalid choice, try again.")


if __name__ == "__main__":
    main()
