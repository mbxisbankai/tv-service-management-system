from app.crud.providers import *
from app.ui.utils import *

def provider_menu():
    while True:
        clear_screen()
        print_header("\nProviders Menu")
        print_info("Select an option")
        print_option("[0]: Back to main menu")
        print_option("[1]: View all providers")
        print_option("[2]: Get provider (Name required)")
        print_option("[3]: Get provider's customers (Name required)")
        print_option("[4]: Create provider (Name & tagline required)")
        print_option("[5]: View a provider's active subscriptions (Name required)")
        print_option("[6]: View a provider's inactive subscriptions (Name required)")
        print_option("[7]: Get a provider's total monthly revenue (Name required)")
        print_option("[8]: Update a provider's info (Name required)")
        print_option("[9]: Delete a provider (Name required)")

        choice = input_prompt("Enter choice: ").strip()

        if choice == "0":
            return
        
        #get_all_providers()
        elif choice == "1":
            providers = get_all_providers()
            if providers:
                print_option("\nList of Providers")
                for provider in providers:
                    print_info(provider)
            else:
                print_warning("No providers found")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")
        
        #get_provider_by_name()
        elif choice == "2":
            p_name = input_prompt("Enter the provider's name: ").strip()
            if p_name:
                print("\n")
                print_info(get_provider_by_name(p_name))
            else:
                print_warning("Please enter a valid provider name")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")
        
        #get_customers()
        elif choice == "3":
            p_name = input_prompt("Enter the provider's name: ").strip()
            if p_name:
                print_option(f"\nList of '{p_name}' customers\n")
                customers = get_customers(p_name)
                if customers:
                    for customer in customers:
                        print_info(customer)
                else:
                    print_warning(f"No customers found for '{p_name}'.")
            else:
                print_warning(f"\nPlease enter a valid provider name.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #create_provider()
        elif choice == "4":
            p_name = input_prompt("Enter provider's name: ").strip()
            p_tagline = input_prompt("Enter provider's tagline: ").strip()

            if p_name and p_tagline:
                new_provider = create_provider(p_name, p_tagline)
                print_success(f"\nProvider '{p_name}' created successfully.")
            else:
                print_warning("\nPlease enter a valid provider name and tagline")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #active_subscriptions()
        elif choice == "5":
            p_name = input_prompt("Enter the provider's name: ").strip()
            if p_name:
                active_subs = active_subscriptions(p_name)
                if active_subs:
                    for active_sub in active_subs:
                        print_info(active_sub)
                else:
                    print_warning(f"No active subsctiptions for '{p_name}'.")
            else:
                print_warning("Please enter a valid provider name.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #inactive_subscriptions()
        elif choice == "6":
            p_name = input_prompt("Enter the provider's name: ").strip()
            if p_name:
                inactive_subs = inactive_subscriptions(p_name)
                if inactive_subs:
                    for inactive_sub in inactive_subs:
                        print_info(inactive_sub)
                else:
                    print_warning(f"No inactive subsctiptions for '{p_name}'.")
            else:
                print_warning("Please enter a valid provider name.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #total_revenue()
        elif choice == "7":
            p_name = input_prompt("Enter the provider's name: ").strip()
            if p_name:
                total = total_revenue(p_name)
                if total:
                    print_info(f"'{p_name}' made {total} in subscriptions.")
                else:
                    print_warning(f"\nNo revenue for '{p_name}'.")
            else:
                print_warning(f"\nNo revenue for '{p_name}'.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #update_provider()
        elif choice == "8":
            p_id = input_prompt("Enter the provider's ID: ").strip()
            p_name = input_prompt("Enter the provider's name: ").strip()
            p_tagline = input_prompt("Enter the provider's tagline: ").strip()

            if p_id and p_name and p_tagline:
                updated_provider = update_provider(p_id, p_name, p_tagline)
                print_success(f"\nProvider '{p_name}' updated successfully: {updated_provider}")
            else:
                print_warning("Please enter the valid ID, name and tagline for the provider.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #delete_provider()
        elif choice == "9":
            p_name = input_prompt("Enter the provider's name: ").strip()

            if p_name:
                print("\nThis action cannot be undone.")
                prompt = input_prompt("Continue(1) or Exit(0): ").strip()
                if prompt == "1":
                    delete_provider(p_name)
                    remaining_providers = get_all_providers()
                    print_option("\nRemaining providers")
                    for provider in remaining_providers:
                        print_info(provider)
                else:
                    return
            else:
                print_warning("Please enter a valid provider name")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")
        else:
            print_error("Invalid option, please try again")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")
