class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0
        

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print(" Username: " + self.username)
        print(" Email: " + self.email)
        print(" Location: " + self.location)
        

    def greet_user(self):
        print(f"\nWelcome back {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

john = User('john', 'biden', 'j_bid', 'j_bid@example.com', 'arizona')
john.describe_user()
john.greet_user()

donald = User('donald', 'trump', 'd_trxmp', 'dt@example.com', 'florida')
donald.describe_user()
donald.greet_user()

print("\nMaking 3 login attempts...")
john.increment_login_attempts()
john.increment_login_attempts()
john.increment_login_attempts()
print(" Login attempts: " + str(john.login_attempts))

print("Reset login attempts...")
john.reset_login_attempts()
print(" Login attempts: " + str(john.login_attempts))







