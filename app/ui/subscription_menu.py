from app.crud.subscriptions import *
from app.ui.utils import *

def subscription_menu():
    while True:
        clear_screen()
        print_header("Subscriptions Menu")
        print_info("Select an option")
        print_option("[0]: Back to main menu")
        print_option("[1]: View all subscriptions")
        print_option("[2]: Get a subscription [bold](Subscription ID required)[/bold]")
        print_option("[3]: Get the subscription provider [bold](Subscription ID required)[/bold]")
        print_option("[4]: Get the subscribers [bold](Subscription ID required)[/bold]")
        print_option("[5]: Update a subscription [bold](Subscription ID, Provider Name, Price, Customer ID required)[/bold]")
        print_option("[6]: Renew a subscription [bold](Subscription ID, Provider Name, Price, Customer ID required)[/bold]")
        print_option("[7]: Unsubscribe [bold](Subscription ID required)[/bold]")

        choice = input_prompt("\nEnter choice: ").strip()

        if choice == "0":
            return
        #get_all_subscriptions()
        elif choice == "1":
            subscriptions = get_all_subscriptions()
            if subscriptions:
                display_subscriptions(subscriptions)
            else:
                print_warning("No subscriptions found.")
            input_prompt("\nPress Enter to return to the menu ↵")

        #get_subscription_by_id()
        elif choice == "2":
            sub_id = input_prompt("Enter the subscription ID: ").strip()
            subscription = get_subscription_by_id(sub_id)
            if subscription:
                print("\n")
                print_info(subscription)
            else:
                print_warning(f"No subscription with ID: {sub_id} found")
            input_prompt("\nPress Enter to return to the menu ↵")

        #get_provider()
        elif choice == "3":
            sub_id = input_prompt("Enter the subscription ID: ").strip()
            provider = get_provider(sub_id)
            if provider:
                print("\n")
                print_info(provider)
            else:
                print_warning(f"\nPlease enter a valid subscription ID")
            input_prompt("\nPress Enter to return to the menu ↵")

        #get_customer()
        elif choice == "4":
            sub_id = input_prompt("Enter the subscription ID: ").strip()
            customer = get_customer(sub_id)
            if customer:
                print("\n")
                print_info(customer)
            else:
                print_warning(f"\nPlease enter a valid subscription ID")
            input_prompt("\nPress Enter to return to the menu ↵")

        #update_subscription()
        elif choice == "5":
            sub_id = input_prompt("Enter the subscription ID: ").strip()
            p_name = input_prompt("Enter the provider name: ").strip()
            sub_price = input_prompt("Enter the subscription price: ").strip()
            c_id = input_prompt("Enter the customer's ID: ").strip()
            updated_subscription = update_subscription(sub_id, sub_price, p_name, c_id)

            if updated_subscription:
                print_success(f"\nSubscription to '{p_name}' updated successfully: {updated_subscription}")
            else:
                print_error("Failed to update. Make sure all IDs are valid.")
            input_prompt("\nPress Enter to return to the menu ↵")

        #renew_subscription()
        elif choice == "6":
            sub_id = input_prompt("Enter the subscription ID: ").strip()
            p_name = input_prompt("Enter the provider name: ").strip()
            sub_price = input_prompt("Enter the subscription price: ").strip()
            c_id = input_prompt("Enter the customer's ID: ").strip()
            renewed_subscription = renew_subscription(sub_id, sub_price, p_name, c_id)

            if renewed_subscription:
                print_success(f"\nSubscription to '{p_name}' renewed successfully: {renewed_subscription}")
            else:
                print_error("Failed to update. Make sure all IDs are valid.")
            input_prompt("\nPress Enter to return to the menu ↵")

        #delete_subscription()
        elif choice == "7":
            sub_id = input_prompt("\nEnter the subscription ID: ").strip()
            subscription = get_subscription_by_id(sub_id)
            if subscription:
                print_warning("\nThis action cannot be undone")
                prompt = input_prompt("\nContinue(1) or Exit(0): ").strip()
                if prompt == "1":
                    delete_subscription(sub_id)
                    remaining_subscriptions = get_all_subscriptions()
                    print_success(f"Successfully unsubscribed from subscription with ID: {sub_id}")
                    print_option("\nRemaining subscriptions")
                    display_subscriptions(remaining_subscriptions)
                else:
                    return
            else:
                print_warning(f"\nNo subscription with ID: {sub_id} was found")
            input_prompt("\nPress Enter to return to the menu ↵")

        else:
            print_error("Invalid option, please try again.")
            input_prompt("\nPress Enter to return to the menu ↵")

    