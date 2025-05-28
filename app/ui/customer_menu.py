from app.crud.customers import *

def customer_menu():
    while True:
        print("\n***Customers Menu***")
        print("Select an option")
        print("0: Back to main menu")
        print("1: View all customers")
        print("2: Get a customer (ID required)")
        print("3: Get customer's subscriptions (ID required)")
        print("4: Get customer's providers (ID required)")
        print("5: Create customer (Name required)")
        print("6: Update customer (ID & name required)")
        print("7: Delete customer (ID required)")
        print("8: Add a subscription (ID, Provider Name & Price required)")

        choice = input("\nEnter choice: ").strip()

        #get_all_customers()
        if choice == "0":
            return
        elif choice == "1":
            customers = get_all_customers()
            if customers:
                print("\nList of Customers:")
                for customer in customers:
                    print(customer)
            else:
                print("No customers found.")
        
        #get_customer_by_id()
        elif choice == "2":
            c_id = input("Enter the customer's ID: ").strip()
            if c_id:
                print("\n")
                print(get_customer_by_id(c_id))
            else:
                print(f"No customer with ID: {c_id} found")

        #get_subscriptions()
        elif choice == "3":
            c_id = input("Enter the customer's ID: ").strip()
            if c_id:
                subscriptions = get_subscriptions(c_id)
                print("\n")
                for subscription in subscriptions:
                    print(subscription)
            else:
                print(f"No subscriptions found for customer with ID: {c_id}")

        #get_providers()
        elif choice == "4":
            c_id = input("Enter the customer's ID: ").strip()
            if c_id:
                providers = get_providers(c_id)
                print("\n")
                for provider in providers:
                    print(provider)
            else:
                print(f"No providers found for customer with ID: {c_id}")

        #create_customer()
        elif choice == "5":
            c_name = input("Enter the customer's name: ").strip()
            if c_name:
                new_customer = create_customer(c_name)
                print(f"Customer '{c_name}' created successfully: {new_customer}")
            else:
                print("Please enter a valid name.")

        #update_customer()
        elif choice == "6":
            c_id = input("\nEnter the customer's ID: ").strip()
            c_name = input("\nEnter the customer's new name: ").strip()
            if c_id and c_id:
                updated_customer = update_customer(c_id, c_name)
                print(f"\nCustomer '{c_name}' updated successfully: {updated_customer}")
            else:
                print("Please enter a valid ID and name.")

        #delete_customer()
        elif choice == "7":
            c_id = input("Enter the customer's ID: ").strip()
            if c_id:
                print("\nThis action cannot be undone")
                prompt = input("\nContinue(1) or Exit(0): ")
                if prompt == "1":
                    delete_customer(c_id)
                    remaining_customers = get_all_customers()
                    print("\nRemaining Customers")
                    for customer in remaining_customers:
                        print(customer)
                else:
                    return
            else:
                print(f"No customer with ID: {c_id} was found")

        elif choice == "8":
            c_id = input("Enter the customer's ID: ").strip()
            p_name = input("Enter the provider's name: ").strip()
            sub_price = input("Enter the subscription price: ").strip()

            if c_id and p_name and sub_price:
                new_subscription = add_subscription(c_id, p_name, sub_price)
                print(f"Subscription for customer with ID: {c_id} created successfully\n")
                print(f"Subscription: {new_subscription}")
        else:
            print("Invalid option, please try again.")
