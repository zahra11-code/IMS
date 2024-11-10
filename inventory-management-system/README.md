## Final Project: Inventory Management System (IMS)

### Project Title:

**Inventory Management System (IMS)**

### Objective:

Console-based system that manages inventory for a small business. The system provides admin witha menu to create, update, view, and delete products in the inventory while keeping track of stock levels and handling multiple users with role-based permissions. To signup as a admin you need a verification key which is "111".

### Functionalities:

1. **User Authentication and Role Management**

   - Support two different roles like “Admin” and “User.”
   - Admins can add, edit, delete, view, and restock products,  whereas Users can only view inventory details and purchase 
     items.
   - A basic login system with username and password validation(verification key in case of admin login "111").

2. **Product Management (OOP Concepts)**

   - A `Product` class with attributes like `product_id`, `name`, `category`, `price`, and `stock`.
   - Methods for adding, editing, deleting, viewing(display), restocking, selling products.
   - Product information is stored using dictionaries.

3. **Inventory Operations**

   - Track stock levels: Admin can check which itema need restocking.
   - display_products() method is implemented for view all the products in the inventory.
   - Stock adjustments can be done for existing products (you can change the name, id, category, and price of the products 
     based on the stock requirement which you can check by the method restock_products()).

4. **Error Handling**
   - Proper error handling has been implemented for for invalid inputs, such as incorrect login details or attempts to 
     update non-existent products.
   - Smooth flow of program has been ensured.

### Principles Implemented

- OOP principles
- Data Structures(dictionaries and lists for data storage and manipulation)
- Logic Building

