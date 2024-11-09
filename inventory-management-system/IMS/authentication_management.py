class Authentication:
    def __init__(self):
        self.admin_dict = {}
        self.user_dict = {}
        self.current_user = None
        self.current_role = None

    def signup(self):
        print("Welcome to Inventory Management System!")
        role = input("Do you want to sign up as Admin or User? (A/U): ").upper()
        if role == 'A':
            if input("Enter the admin verification key: ") == '111':
                username = input("Enter admin username: ")
                password = input("Enter admin password: ")
                self.admin_dict[username] = password
                self.current_user = username
                self.current_role = 'admin'
                print("Admin account created successfully!")
            else:
                print("Invalid admin verification key.")
        elif role == 'U':
            username = input("Enter user username: ")
            password = input("Enter user password: ")
            self.user_dict[username] = password
            self.current_user = username
            self.current_role = 'user'
            print("User account created successfully!")
        else:
            print("Invalid role.")

    def login(self):
        
         username = input("Enter your username: ")
         password = input("Enter your password: ")
         if self.current_role == 'admin':
            if username in self.admin_dict and self.admin_dict[username] == password:
                self.current_user = username
                self.current_role = 'admin'
                print("Logged in as Admin")
            else:
                print("Invalid username or password.")
         elif self.current_role == 'user':
            if username in self.user_dict and self.user_dict[username] == password:
                self.current_user = username
                self.current_role = 'user'
                print("Logged in as User")
            else:
                print("Invalid username or password.")


