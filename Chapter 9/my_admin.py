from admin import Admin

john = Admin('john', 'biden', 'j_bid', 'j_bid@example.com','arizona')
john.describe_user()

john_privileges = [
    'can reset passwords',
    'can suspend accounts',
    'can moderate discussions',
    ]
john.privileges.privileges = john_privileges

print("\nThe admin " + john.username + " has these privileges: ")
john.privileges.show_privileges()


