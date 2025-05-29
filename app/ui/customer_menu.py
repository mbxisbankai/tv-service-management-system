from app.crud.customers import *
from app.ui.utils import *

def customer_menu():
    while True:
        clear_screen()
        print_header("Customers Menu")
        print_info("Select an option")
        print_option("[0]: Back to main menu")
        print_option("[1]: View all customers")
        print_option("[2]: Get a customer [bold](Customer ID required)[/bold]")
        print_option("[3]: Get customer's subscriptions [bold](Customer ID required)[/bold]")
        print_option("[4]: Get customer's providers [bold](Customer ID required)[/bold]")
        print_option("[5]: Create customer [bold](Customer name required)[/bold]")
        print_option("[6]: Update customer [bold](Customer's ID & name required)[/bold]")
        print_option("[7]: Delete customer [bold](Customer ID required)[/bold]")
        print_option("[8]: Add a subscription [bold](Customer ID, Provider Name & Price required)[/bold]")

        choice = input_prompt("\nEnter choice: ").strip()

        #get_all_customers()
        if choice == "0":
            return
        elif choice == "1":
            customers = get_all_customers()
            if customers:
                display_customers(customers)
            else:
                print_warning("No customers found.")
            input_prompt("\nPress Enter to return to the menu ↵")
        
        #get_customer_by_id()
        elif choice == "2":
            c_id = input_prompt("Enter the customer's ID: ").strip()
            customer = get_customer_by_id(c_id)
            if customer:
                print("\n")
                print_info(get_customer_by_id(c_id))
            else:
                print_warning(f"No customer with ID: {c_id} found")
            input_prompt("\nPress Enter to return to the menu ↵")

        #get_subscriptions()
        elif choice == "3":
            c_id = input_prompt("Enter the customer's ID: ").strip()
            if c_id:
                subscriptions = get_subscriptions(c_id)
                print("\n")
                if subscriptions:
                    display_subscriptions(subscriptions)
                else:
                    print_warning(f"No subscriptions found for customer with ID: {c_id}")
            input_prompt("\nPress Enter to return to the menu ↵")

        #get_providers()
        elif choice == "4":
            c_id = input_prompt("Enter the customer's ID: ").strip()
            if c_id:
                providers = get_providers(c_id)
                if providers:
                    print("\n")
                    display_providers(providers)
                else:
                    print_warning(f"No providers found for customer with ID: {c_id}")
            input_prompt("\nPress Enter to return to the menu ↵")

        #create_customer()
        elif choice == "5":
            c_name = input_prompt("Enter the customer's name: ").strip()
            if c_name:
                new_customer = create_customer(c_name)
                print_success(f"Customer '{c_name}' created successfully: {new_customer}")
            else:
                print_warning("Please enter a valid name.")
            input_prompt("\nPress Enter to return to the menu ↵")

        #update_customer()
        elif choice == "6":
            c_id = input_prompt("\nEnter the customer's ID: ").strip()
            c_name = input_prompt("\nEnter the customer's new name: ").strip()
            if c_id and c_name:
                updated_customer = update_customer(c_id, c_name)
                print_success(f"\nCustomer '{c_name}' updated successfully: {updated_customer}")
            else:
                print_warning("Please enter a valid ID and name.")
            input_prompt("\nPress Enter to return to the menu ↵")

        #delete_customer()
        elif choice == "7":
            c_id = input_prompt("Enter the customer's ID: ").strip()
            if c_id:
                customer = get_customer_by_id(c_id)
                if customer:
                    print_warning("\nThis action cannot be undone")
                    prompt = input_prompt("\nContinue(1) or Exit(0): ")
                    if prompt == "1":
                        delete_customer(c_id)
                        remaining_customers = get_all_customers()
                        print_option("\nRemaining Customers")
                        display_customers(remaining_customers)
                    else:
                        return
                else:
                    print_warning(f"No customer with ID: {c_id} was found")
            else:
                print_warning("Please enter a valid customer ID")
            input_prompt("\nPress Enter to return to the menu ↵")

        elif choice == "8":
            c_id = input_prompt("Enter the customer's ID: ").strip()
            p_name = input_prompt("Enter the provider's name: ").strip()
            sub_price = input_prompt("Enter the subscription price: ").strip()

            if c_id and p_name and sub_price:
                new_subscription = add_subscription(c_id, p_name, sub_price)
                print_success(f"Subscription for customer with ID: {c_id} created successfully\n")
                print_info(f"Subscription: {new_subscription}")
            else:
                print_warning("Please enter a valid customer ID, provider name and subscription price.")
            input_prompt("\nPress Enter to return to the menu ↵")
        else:
            print_error("Invalid option, please try again.")
            input_prompt("\nPress Enter to return to the menu ↵")
