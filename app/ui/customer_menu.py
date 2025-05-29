from app.crud.customers import *
from app.ui.utils import *

def customer_menu():
    while True:
        clear_screen()
        print_header("Customers Menu")
        print_info("Select an option")
        print_option("[0]: Back to main menu")
        print_option("[1]: View all customers")
        print_option("[2]: Get a customer (ID required)")
        print_option("[3]: Get customer's subscriptions (ID required)")
        print_option("[4]: Get customer's providers (ID required)")
        print_option("[5]: Create customer (Name required)")
        print_option("[6]: Update customer (ID & name required)")
        print_option("[7]: Delete customer (ID required)")
        print_option("[8]: Add a subscription (ID, Provider Name & Price required)")

        choice = input_prompt("\nEnter choice: ").strip()

        #get_all_customers()
        if choice == "0":
            return
        elif choice == "1":
            customers = get_all_customers()
            if customers:
                print_option("\nList of Customers:")
                for customer in customers:
                    print_info(customer)
            else:
                print_warning("No customers found.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")
        
        #get_customer_by_id()
        elif choice == "2":
            c_id = input_prompt("Enter the customer's ID: ").strip()
            customer = get_customer_by_id(c_id)
            if customer:
                print("\n")
                print_info(get_customer_by_id(c_id))
            else:
                print_warning(f"No customer with ID: {c_id} found")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #get_subscriptions()
        elif choice == "3":
            c_id = input_prompt("Enter the customer's ID: ").strip()
            if c_id:
                subscriptions = get_subscriptions(c_id)
                print("\n")
                if subscriptions:
                    for subscription in subscriptions:
                        print_info(subscription)
                else:
                    print_warning(f"No subscriptions found for customer with ID: {c_id}")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #get_providers()
        elif choice == "4":
            c_id = input_prompt("Enter the customer's ID: ").strip()
            if c_id:
                providers = get_providers(c_id)
                if providers:
                    print("\n")
                    for provider in providers:
                        print_info(provider)
                else:
                    print_warning(f"No providers found for customer with ID: {c_id}")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #create_customer()
        elif choice == "5":
            c_name = input_prompt("Enter the customer's name: ").strip()
            if c_name:
                new_customer = create_customer(c_name)
                print_success(f"Customer '{c_name}' created successfully: {new_customer}")
            else:
                print_warning("Please enter a valid name.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #update_customer()
        elif choice == "6":
            c_id = input_prompt("\nEnter the customer's ID: ").strip()
            c_name = input_prompt("\nEnter the customer's new name: ").strip()
            if c_id and c_name:
                updated_customer = update_customer(c_id, c_name)
                print_success(f"\nCustomer '{c_name}' updated successfully: {updated_customer}")
            else:
                print_warning("Please enter a valid ID and name.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

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
                        for customer in remaining_customers:
                            print_info(customer)
                    else:
                        return
                else:
                    print_warning(f"No customer with ID: {c_id} was found")
            else:
                print_warning("Please enter a valid customer ID")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

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
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")
        else:
            print_error("Invalid option, please try again.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")
