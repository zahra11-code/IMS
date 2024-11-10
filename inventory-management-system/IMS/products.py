from authentication_management import Authentication
class Products:
    def __init__(self, auth):  # Pass the Authentication object
        self.products = [{"id" : 11, "name": "brick", "category": "construction", "price": 76, "stock": 100},
        {"id": 12, "name": "hammer", "category": "tool", "price": 987, "stock": 50},
        {"id" : 13, "name": "cement", "category": "construction", "price": 1100, "stock": 20}]
        self.auth = auth  # Store the Authentication object
        self.sale : dict[str: int] = {}

    def add_products(self):
        if self.auth.current_role == 'admin':  # Access current_role through auth
            num_products = int(input("Enter the number of products to add: "))
            for _ in range(num_products):
                product_id = input("Enter product ID: ")
                product_name = input("Enter product name: ")
                product_category = input("Enter product category: ")
                product_price = float(input("Enter product price: "))
                product_stock = int(input("Enter initial stock quantity: "))
                self.products.append({"id": product_id, "name": product_name, "category": product_category, "price": product_price, "stock": product_stock})
                print("Product added successfully!")

        else:
            print("You do not have permission to add products.")

    # ... (other methods - edit_product, delete_product) ...
    def edit_product(self, product_id):
     if self.auth.current_role == 'admin':
        for product in self.products:
            if product['id'] == product_id:
                print(f"Editing product: {product['name']}")
                new_name = input("Enter new name (leave blank to keep current): ")
                new_category = input("Enter new category (leave blank to keep current): ")
                new_price = input("Enter new price (leave blank to keep current): ")
                new_stock = input("Enter new stock (leave blank to keep current): ")

                if new_name:
                    product['name'] = new_name
                if new_category:
                    product['category'] = new_category
                if new_price:
                    product['price'] = float(new_price)
                if new_stock:
                    product['stock'] = int(new_stock)

                print("Product updated successfully!")
                return

        print("Product not found.")
     else:
        print("You do not have permission to edit products.")

    def delete_product(self, product_id):
     if self.auth.current_role == 'admin':
        for i, product in enumerate(self.products):
            if product['id'] == product_id:
                del self.products[i]
                print("Product deleted successfully!")
                return

        print("Product not found.")
     else:
        print("You do not have permission to delete products.")


    def display_products(self):
        if self.auth.current_role == 'admin':  # Access current_role through auth
            print("Product List:")
            for product in self.products:
                print(f"ID: {product['id']}, Name: {product['name']}, Category: {product['category']}, Price: {product['price']}, Stock: {product['stock']}")
                if product['stock'] <= 10:
                    print(f"Warning: Product {product['name']} is low on stock!")
        elif self.auth.current_role == 'user':  # Access current_role through auth
            print("Product List:")
            for product in self.products:
                print(f"Name: {product['name']}, Category: {product['category']}, Price: {product['price']}")

    def restock_products(self):
        low_stock_products = []
        for product in self.products:
            if product["stock"] <= 10:
                low_stock_products.append(product["name"])
        if low_stock_products:
            print("Products need restocking: ")
            for restock in low_stock_products:
                print(f"{restock}") 
        else:
            print("No items need restocking!")  
    def sale_product(self):
     if self.auth.current_role == "user":
        current_session_sales = {}  # Initialize a temporary dictionary
        purchase = input("Enter the name of the Product you want to buy? ")
        product_found = False
        for product in self.products:
            if purchase == product["name"]:
                product_found = True
                quantity = int(input(f"How many sets of {purchase} you want to buy?"))
                if quantity <= product["stock"]:
                    print(f"You have purchased {quantity} sets of {purchase}")
                    product["stock"] = product["stock"] - quantity
                    self.sale[purchase] = quantity
                    current_session_sales[purchase] = quantity  # Add to temporary dict
                elif quantity > product["stock"]:
                    print(f"There are not this many items of {purchase} for sale at the moment")
                    break
        if not product_found:
            print(f"There is no such item for sale at the moment!")      
