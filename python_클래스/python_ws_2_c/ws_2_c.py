# 아래에 코드를 작성하시오.
class User :
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def show_info(self) :
        return f"Name: {self.name}, Email: {self.email}"
    
class AdminUser(User) :
    def __init__(self, name, email, permissions ):
        super().__init__(name, email)
        self.permissions = permissions
        
    def show_info(self):
        return f"{super().show_info()}, Permissions: {self.permissions}"
    
    
us1 = User("Alice", "alice@example.com")
us2 = User("Bob", "bob@example.com")
us3 = AdminUser("Charlie", "charlie@example.com", "Full Access")
print(us1.show_info())
print(us2.show_info())
print(us3.show_info())

