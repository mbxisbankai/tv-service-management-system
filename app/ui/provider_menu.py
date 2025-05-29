from app.crud.providers import *
from app.ui.utils import *

def provider_menu():
    while True:
        clear_screen()
        print_header("Providers Menu")
        print_info("Select an option")
        print_option("[0]: Back to main menu")
        print_option("[1]: View all providers")
        print_option("[2]: Get provider (Provider name required)")
        print_option("[3]: Get provider's customers (Provider name required)")
        print_option("[4]: Create provider (Provider's name & tagline required)")
        print_option("[5]: View a provider's active subscriptions (Provider's name required)")
        print_option("[6]: View a provider's inactive subscriptions (Provider's name required)")
        print_option("[7]: Get a provider's total monthly revenue (Provider's name required)")
        print_option("[8]: Update a provider's info (Provider's name required)")
        print_option("[9]: Delete a provider (Provider's name required)")

        choice = input_prompt("Enter choice: ").strip()

        if choice == "0":
            return
        
        #get_all_providers()
        elif choice == "1":
            providers = get_all_providers()
            if providers:
                display_providers(providers)
            else:
                print_warning("No providers found")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")
        
        #get_provider_by_name()
        elif choice == "2":
            p_name = input_prompt("Enter the provider's name: ").strip()
            provider = get_provider_by_name(p_name)
            if provider:
                print("\n")
                print_info(provider)
            else:
                print_warning(f"No provider named '{p_name} found.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")
        
        #get_customers()
        elif choice == "3":
            p_name = input_prompt("Enter the provider's name: ").strip()
            if p_name:
                print_option(f"\nList of '{p_name}' customers\n")
                customers = get_customers(p_name)
                if customers:
                    display_customers(customers)
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
                    display_subscriptions(active_subs)
                else:
                    print_warning(f"No active subscriptions for '{p_name}'.")
            else:
                print_warning("Please enter a valid provider name.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #inactive_subscriptions()
        elif choice == "6":
            p_name = input_prompt("Enter the provider's name: ").strip()
            if p_name:
                inactive_subs = inactive_subscriptions(p_name)
                if inactive_subs:
                    display_subscriptions(inactive_subs)
                else:
                    print_warning(f"No inactive subscriptions for '{p_name}'.")
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
                print_warning("Please enter a valid provider name.")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")

        #update_provider()
        elif choice == "8":
            p_id = input_prompt("Enter the provider's ID: ").strip()
            p_name = input_prompt("Enter the provider's name: ").strip()
            p_tagline = input_prompt("Enter the provider's tagline: ").strip()
            updated_provider = update_provider(p_id, p_name, p_tagline)

            if update_provider:
                print_success(f"\nProvider '{p_name}' updated successfully: {updated_provider}")
            else:
                print_warning("Update failed — check if the provider ID is correct.")
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
                    display_providers(remaining_providers)
                else:
                    return
            else:
                print_warning("Please enter a valid provider name")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")
        else:
            print_error("Invalid option, please try again")
            input_prompt("\nPress Enter to return to the menu[blink] | [/blink]")
