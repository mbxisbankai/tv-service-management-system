from app.crud.subscriptions import *
from app.ui.utils import clear_screen

def subscription_menu():
    while True:
        clear_screen()
        print("\n***Subscriptions Menu***")
        print("0: Back to main menu")
        print("1: View all subscriptions")
        print("2: Get a subscription (ID required)")
        print("3: Get the subscription provider (ID required)")
        print("4: Get the subscriber (ID required)")
        print("5: Update a subscription (ID, Provider Name, Price, Customer ID required)")
        print("6: Renew a subscription (ID, Provider Name, Price, Customer ID required)")
        print("7: Unsubscribe (ID required)")

        choice = input("\nEnter choice: ").strip()

        if choice == "0":
            return
        #get_all_subscriptions()
        elif choice == "1":
            subscriptions = get_all_subscriptions()
            if subscriptions:
                print("\nList of Subscriptions\n")
                for sub in subscriptions:
                    print(sub)
            else:
                print("No subscriptions found.")

        #get_subscription_by_id()
        elif choice == "2":
            sub_id = input("Enter the subscription ID: ").strip()
            if sub_id:
                print("\n")
                print(get_subscription_by_id(sub_id))
            else:
                print(f"No subscription with ID: {sub_id} found")

        #get_provider()
        elif choice == "3":
            sub_id = input("Enter the subscription ID: ").strip()
            if sub_id:
                print("\n")
                print(get_provider(sub_id))
            else:
                print(f"\nPlease enter a valid subscription ID")

        #get_customer()
        elif choice == "4":
            sub_id = input("Enter the subscription ID: ").strip()
            if sub_id:
                print("\n")
                print(get_customer(sub_id))
            else:
                print(f"\nPlease enter a valid subscription ID")

        #update_subscription()
        elif choice == "5":
            sub_id = input("Enter the subscription ID: ").strip()
            p_name = input("Enter the provider name: ").strip()
            sub_price = input("Enter the subscription price: ").strip()
            c_id = input("Enter the customer's ID: ").strip()

            if sub_id and p_name and sub_price and c_id:
                updated_subscription = update_subscription(sub_id, sub_price, p_name, c_id)
                print(f"\nSubscription to '{p_name}' updated successfully: {updated_subscription}")
            else:
                print("Missing or invalid arguments. Please review and try again.")

        #renew_subscription()
        elif choice == "6":
            sub_id = input("Enter the subscription ID: ").strip()
            p_name = input("Enter the provider name: ").strip()
            sub_price = input("Enter the subscription price: ").strip()
            c_id = input("Enter the customer's ID: ").strip()

            if sub_id and p_name and sub_price and c_id:
                renewed_subscription = renew_subscription(sub_id, sub_price, p_name, c_id)
                print(f"\nSubscription to '{p_name}' renewed successfully: {renewed_subscription}")
            else:
                print("Missing or invalid arguments. Please review and try again.")

        #delete_subscription()
        elif choice == "7":
            sub_id = input("\nEnter the subscription ID: ").strip()
            if sub_id:
                print("\nThis action cannot be undone")
                prompt = input("\nContinue(1) or Exit(0): ").strip()
                if prompt == "1":
                    delete_subscription(sub_id)
                    remaining_subscriptions = get_all_subscriptions()
                    print(f"Successfully unsubscribed from subscription with ID: {sub_id}")
                    print("\nRemaining subscriptions")
                    for sub in remaining_subscriptions:
                        print(sub)
                else:
                    return
            else:
                print(f"\nNo subscription with ID: {sub_id} was found")

        else:
            print("Invalid option, please try again.")

    