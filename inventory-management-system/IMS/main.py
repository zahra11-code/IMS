from authentication_management import Authentication
from products import Products


# Main function
if __name__ == '__main__':
    auth = Authentication()
    auth.signup()
    login_choice = input("Would you like to login? If yes type 'y' and if no type 'q for quit'!").upper()
    if login_choice == "Y":
     auth.login()

     products = Products(auth)  # Pass the auth object to Products
     while True:
       if auth.current_role == 'admin':
            print("\nAdmin Menu:")
            print("1. Add Products")
            print("2. Edit Product")
            print("3. Delete Product")
            print("4. Display Products")
            print("5. Items need restocking")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                products.add_products()
            elif choice == '2':
                product_id = input("Enter product ID to edit: ")
                products.edit_product(product_id)
            elif choice == '3':
                product_id = input("Enter product ID to delete: ")
                products.delete_product(product_id)
            elif choice == '4':
                products.display_products()
            elif choice == '5':
                products.restock_products
            elif choice == '6':
                break
            else:
                print("Invalid choice.")
       elif auth.current_role == 'user':
            products.display_products()
            break

    elif(login_choice == "Q"):
        print("Thankyou!")



