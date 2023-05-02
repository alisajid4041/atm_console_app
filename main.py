class Transactions:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def delete_transaction(self, transaction):
        self.transactions.remove(transaction)

    def get_transactions(self, user=None):
        if user:
            return [t for t in self.transactions if t['user'] == user]
        else:
            return self.transactions


class User:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.balance = 0
        self.transactions = Transactions()

    def login(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        self.balance += amount
        self.transactions.add_transaction({'type': 'deposit', 'amount': amount, 'user': self})

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.add_transaction({'type': 'withdraw', 'amount': amount, 'user': self})

    def transfer(self, amount, to_user):
        if self.balance >= amount:
            self.balance -= amount
            to_user.balance += amount
            self.transactions.add_transaction({'type': 'transfer', 'amount': amount, 'user': self, 'to_user': to_user})

    def get_transactions(self):
        return self.transactions.get_transactions(user=self)


class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.users = []
        self.admins = []
        self.transactions = Transactions()

    def login(self, password):
        return self.password == password

    def add_user(self, user):
        self.users.append(user)

    def update_user(self, user):
        pass

    def delete_user(self, user):
        self.users.remove(user)

    def view_users(self):
        return self.users

    def search_users(self, name):
        return [u for u in self.users if u.name == name]

    def add_admin(self, admin):
        self.admins.append(admin)

    def update_admin(self, admin):
        pass

    def delete_admin(self, admin):
        self.admins.remove(admin)

    def view_admins(self):
        return self.admins

    def set_withdrawal_limit(self, limit):
        pass

    def set_transfer_limit(self, limit):
        pass

    def get_transactions(self, user=None):
        return self.transactions.get_transactions(user=user)

    def delete_transaction(self, transaction):
        self.transactions.delete_transaction(transaction)

    def change_password(self, new_password):
        self.password = new_password


# Example usage:

admin = Admin('Admin', 'admin_password')
user1 = User('John', '1234')
user2 = User('Jane', '5678')

admin.add_user(user1)
admin.add_user(user2)

user1.deposit(1000)
user1.transfer(500, user2)

print(user1.balance)  # Output: 500
print(user2.balance)  # Output: 500

print(user1.get_transactions())  # Output: [{'type': 'deposit', 'amount': 1000, 'user': <__main__.User object at 0x7fdd4ec127c0>}, {'type': 'transfer', 'amount': 500, 'user': <__main__.User object at
