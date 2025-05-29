from app.crud.providers import *
from app.ui.utils import *

def provider_menu():
    while True:
        clear_screen()
        print("\n***Providers Menu***")
        print("Select an option")
        print("0: Back to main menu")
        print("1: View all providers")
        print("2: Get provider (Name required)")
        print("3: Get provider's customers (Name required)")
        print("4: Create provider (Name & tagline required)")
        print("5: View a provider's active subscriptions (Name required)")
        print("6: View a provider's inactive subscriptions (Name required)")
        print("7: Get a provider's total monthly revenue (Name required)")
        print("8: Update a provider's info (Name required)")
        print("9: Delete a provider (Name required)")

        choice = input("Enter choice: ").strip()

        if choice == "0":
            return
        
        #get_all_providers()
        elif choice == "1":
            providers = get_all_providers()
            if providers:
                print("\nList of Providers")
                for provider in providers:
                    print(provider)
            else:
                print("No providers found")
            input("\nPress Enter to return to the menu...")
        
        #get_provider_by_name()
        elif choice == "2":
            p_name = input("Enter the provider's name: ").strip()
            if p_name:
                print("\n")
                print(get_provider_by_name(p_name))
            else:
                print("Please enter a valid provider name")
            input("\nPress Enter to return to the menu...")
        
        #get_customers()
        elif choice == "3":
            p_name = input("Enter the provider's name: ").strip()
            if p_name:
                print(f"\nList of '{p_name}' customers\n")
                customers = get_customers(p_name)
                if customers:
                    for customer in customers:
                        print(customer)
                else:
                    print(f"No customers found for '{p_name}'.")
            else:
                print(f"\nPlease enter a valid provider name.")
            input("\nPress Enter to return to the menu...")

        #create_provider()
        elif choice == "4":
            p_name = input("Enter provider's name: ").strip()
            p_tagline = input("Enter provider's tagline: ").strip()

            if p_name and p_tagline:
                new_provider = create_provider(p_name, p_tagline)
                print(f"\nProvider '{p_name}' created successfully.")
            else:
                print("\nPlease enter a valid provider name and tagline")
            input("\nPress Enter to return to the menu...")

        #active_subscriptions()
        elif choice == "5":
            p_name = input("Enter the provider's name: ").strip()
            if p_name:
                active_subs = active_subscriptions(p_name)
                if active_subs:
                    for active_sub in active_subs:
                        print(active_sub)
                else:
                    print(f"No active subsctiptions for '{p_name}'.")
            else:
                print("Please enter a valid provider name.")
            input("\nPress Enter to return to the menu...")

        #inactive_subscriptions()
        elif choice == "6":
            p_name = input("Enter the provider's name: ").strip()
            if p_name:
                inactive_subs = inactive_subscriptions(p_name)
                if inactive_subs:
                    for inactive_sub in inactive_subs:
                        print(inactive_sub)
                else:
                    print(f"No inactive subsctiptions for '{p_name}'.")
            else:
                print("Please enter a valid provider name.")
            input("\nPress Enter to return to the menu...")

        #total_revenue()
        elif choice == "7":
            p_name = input("Enter the provider's name: ").strip()
            if p_name:
                total = total_revenue(p_name)
                if total:
                    print(f"'{p_name}' made {total} in subscriptions.")
                else:
                    print(f"\nNo revenue for '{p_name}'.")
            else:
                print(f"\nNo revenue for '{p_name}'.")
            input("\nPress Enter to return to the menu...")

        #update_provider()
        elif choice == "8":
            p_id = input("Enter the provider's ID: ").strip()
            p_name = input("Enter the provider's name: ").strip()
            p_tagline = input("Enter the provider's tagline: ").strip()

            if p_id and p_name and p_tagline:
                updated_provider = update_provider(p_id, p_name, p_tagline)
                print(f"\nProvider '{p_name}' updated successfully: {updated_provider}")
            else:
                print("Please enter the valid ID, name and tagline for the provider.")
            input("\nPress Enter to return to the menu...")

        #delete_provider()
        elif choice == "9":
            p_name = input("Enter the provider's name: ").strip()

            if p_name:
                print("\nThis action cannot be undone.")
                prompt = input("Continue(1) or Exit(0): ").strip()
                if prompt:
                    delete_provider(p_name)
                    remaining_providers = get_all_providers()
                    print("\nRemaining providers")
                    for provider in remaining_providers:
                        print(provider)
                else:
                    return
            else:
                print("Please enter a valid provider name")
            input("\nPress Enter to return to the menu...")
        else:
            print("Invalid option, please try again")
            input("\nPress Enter to return to the menu...")
