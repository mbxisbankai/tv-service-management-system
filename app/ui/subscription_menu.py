from app.crud.subscriptions import *
from app.ui.utils import *

def subscription_menu():
    while True:
        clear_screen()
        print_header("\nSubscriptions Menu")
        print_info("Select an option")
        print_option("[0]: Back to main menu")
        print_option("[1]: View all subscriptions")
        print_option("[2]: Get a subscription (ID required)")
        print_option("[3]: Get the subscription provider (ID required)")
        print_option("[4]: Get the subscriber (ID required)")
        print_option("[5]: Update a subscription (ID, Provider Name, Price, Customer ID required)")
        print_option("[6]: Renew a subscription (ID, Provider Name, Price, Customer ID required)")
        print_option("[7]: Unsubscribe (ID required)")

        choice = input_prompt("\nEnter choice: ").strip()

        if choice == "0":
            return
        #get_all_subscriptions()
        elif choice == "1":
            subscriptions = get_all_subscriptions()
            if subscriptions:
                print_option("\nList of Subscriptions\n")
                for sub in subscriptions:
                    print_info(sub)
            else:
                print_warning("No subscriptions found.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #get_subscription_by_id()
        elif choice == "2":
            sub_id = input_prompt("Enter the subscription ID: ").strip()
            if sub_id:
                print("\n")
                print_info(get_subscription_by_id(sub_id))
            else:
                print_warning(f"No subscription with ID: {sub_id} found")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #get_provider()
        elif choice == "3":
            sub_id = input_prompt("Enter the subscription ID: ").strip()
            if sub_id:
                print("\n")
                print_info(get_provider(sub_id))
            else:
                print_warning(f"\nPlease enter a valid subscription ID")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #get_customer()
        elif choice == "4":
            sub_id = input_prompt("Enter the subscription ID: ").strip()
            if sub_id:
                print("\n")
                print_info(get_customer(sub_id))
            else:
                print_warning(f"\nPlease enter a valid subscription ID")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #update_subscription()
        elif choice == "5":
            sub_id = input_prompt("Enter the subscription ID: ").strip()
            p_name = input_prompt("Enter the provider name: ").strip()
            sub_price = input_prompt("Enter the subscription price: ").strip()
            c_id = input_prompt("Enter the customer's ID: ").strip()

            if sub_id and p_name and sub_price and c_id:
                updated_subscription = update_subscription(sub_id, sub_price, p_name, c_id)
                print_success(f"\nSubscription to '{p_name}' updated successfully: {updated_subscription}")
            else:
                print_error("Missing or invalid arguments. Please try again.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #renew_subscription()
        elif choice == "6":
            sub_id = input_prompt("Enter the subscription ID: ").strip()
            p_name = input_prompt("Enter the provider name: ").strip()
            sub_price = input_prompt("Enter the subscription price: ").strip()
            c_id = input_prompt("Enter the customer's ID: ").strip()

            if sub_id and p_name and sub_price and c_id:
                renewed_subscription = renew_subscription(sub_id, sub_price, p_name, c_id)
                print_success(f"\nSubscription to '{p_name}' renewed successfully: {renewed_subscription}")
            else:
                print_error("Missing or invalid arguments. Please try again.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #delete_subscription()
        elif choice == "7":
            sub_id = input_prompt("\nEnter the subscription ID: ").strip()
            if sub_id:
                print_warning("\nThis action cannot be undone")
                prompt = input_prompt("\nContinue(1) or Exit(0): ").strip()
                if prompt == "1":
                    delete_subscription(sub_id)
                    remaining_subscriptions = get_all_subscriptions()
                    print_success(f"Successfully unsubscribed from subscription with ID: {sub_id}")
                    print_option("\nRemaining subscriptions")
                    for sub in remaining_subscriptions:
                        print_info(sub)
                else:
                    return
            else:
                print_warning(f"\nNo subscription with ID: {sub_id} was found")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        else:
            print_error("Invalid option, please try again.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

    