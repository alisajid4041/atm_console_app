import csv
import os
import pandas as pd
from time import sleep

class User:
    def __init__(self, name, password,balance=None):
        self.name = name
        self.password = password
        self.balance = balance
        self.transactions = []

    @staticmethod
    def add_transaction(name,amount,transaction_type):
        users_df = pd.read_csv('users.csv')
        transaction_df = pd.read_csv('transactions.csv')

        index_user = int(users_df[users_df['user'] == name].index.values)

        before_balance = users_df.loc[index_user,'balance']
        print(f"Your Balance Before: ${before_balance}")

        if transaction_type == 'deposit':
             new_balance = before_balance + amount

             users_df.loc[index_user,'balance'] = new_balance
             users_df.to_csv('users.csv',index=False)


             new_row = [name,before_balance,new_balance,amount,transaction_type,'N/A']

             transaction_df.loc[len(transaction_df)] = new_row

             transaction_df.to_csv('transactions.csv',index=False)


             print(f'The user {name} has deposited ${amount} from their account. Remaining balance:${new_balance}\n')
             return
        elif transaction_type == 'withdrawal':
            if amount > before_balance:
                    print("Insufficient Balance\n")
                    return
            else:
                    new_balance = before_balance - amount

                    users_df.loc[index_user,'balance'] = new_balance
                    new_row = [name,before_balance,new_balance,amount,transaction_type,'N/A']


                    transaction_df.loc[len(transaction_df)] = new_row

                    transaction_df.to_csv('transactions.csv',index=False)
                    users_df.to_csv('users.csv',index=False)

                    print(f'The user {name} has withdrawn ${amount} from their account. Remaining balance:${new_balance}\n')

                    return
        elif transaction_type == 'transfer':
            if amount > before_balance:
                    print("Insufficient Balance\n")
                    return
            else:
                to_username = input("Enter the username to transfer funds to: ")
                if users_df[users_df['user'] == to_username].empty:
                    print("This user does not exist!")
                    return
                else:
                    friend_index = int(users_df[users_df['user']== to_username].index.values)
                    friend_balance = users_df.loc[friend_index,'balance']
                    friend_balance = friend_balance + amount

                    new_balance = before_balance - amount

                    new_row = [name,before_balance,new_balance,amount,transaction_type,to_username]
                    transaction_df.loc[len(transaction_df)] = new_row

                    users_df.loc[index_user,'balance'] = new_balance
                    users_df.loc[friend_index,'balance'] = friend_balance

                    print(f'User: {name} has transferred ${amount} to {to_username}. Your remaining balance is: ${new_balance}\n')

                    users_df.to_csv('users.csv',index=False)
                    transaction_df.to_csv('transactions.csv',index=False)

                    return

    @staticmethod

    def view_personal_transactions(name):
        transactions_df = pd.read_csv('transactions.csv')
        check_df = transactions_df[transactions_df['user']== name]

        if check_df.empty:
            print("The User has not made any transactions!")
        else:
            user_transactions = transactions_df.loc[transactions_df['user'] == name]
            print(user_transactions)
        transactions_df.to_csv('transactions.csv',index=False)

    @staticmethod
    def login(name,password):
        df = pd.read_csv('users.csv')
        if name in df['user'].values and int(password) in df['password'].values:
            print("User Login Successfully!")
            return True
        print("Incorrect User Info!\n")


class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @staticmethod
    def create_user(name, password,balance=0):
        users_df = pd.read_csv('users.csv')
        user = User(name, password,balance)


        new_row = [user.name, user.password,user.balance]

        check_df = users_df[users_df['user']== name]

        if check_df.empty:
            users_df.loc[len(users_df)] = new_row
            users_df.to_csv('users.csv',index=False)

            print(f"New User {name} has been created!\n")
        else:
            print("Username already in use! Enter a different one: ")
            return

    @staticmethod
    def update_user(name, password):

        User.password = password

        users_df = pd.read_csv('users.csv')
        index_user = int(users_df[users_df['user']==name].index.values)

        users_df.loc[index_user,'password'] = password
        print('Password Updated!')
        users_df.to_csv('users.csv',index=False)


    @staticmethod
    def delete_user(name):
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            users = list(reader)
        with open('users.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for user in users:
                if user[0] != name:
                    writer.writerow(user)
                    print(f"The user {name} has been deleted!\n")
        del name


    @staticmethod
    def view_users():
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            for user in reader:
                print(user)

    @staticmethod
    def search_user(name):
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            for user in reader:
                if user[0] == name:
                    print(user)
                    return True

            print(f"User {name} not found")

    @staticmethod
    def view_all_transactions():
        with open('transactions.csv', mode='r') as file:
            reader = csv.reader(file)
            for transaction in reader:
                print(transaction)

    @staticmethod
    def delete_transactions():
        open('transactions.csv', mode='w').close()

    @staticmethod
    def create_admin(name, password):
        admin = Admin(name, password)
        admin_df = pd.read_csv('admins.csv')

        new_row = [admin.name,admin.password]

        check_df = admin_df[admin_df['username'] == name]

        if check_df.empty:
            admin_df.loc[len(admin_df)] = new_row
            admin_df.to_csv('admins.csv',index=False)
            print(f'New Admin {name} has been created!\n\n')
        else:
            print("Admin Username already in use!")
            return


    @staticmethod
    def update_admin(name,password):

        Admin.password = password
        admins_df = pd.read_csv('admins.csv')

        index_admin = int(admins_df[admins_df['username']== name].index.values)


        admins_df.loc[index_admin,'password'] = password
        print('Admin Password Updated!')
        admins_df.to_csv('admins.csv',index=False)


    @staticmethod
    def delete_admin(name):
        with open('admins.csv', mode='r') as file:
            reader = csv.reader(file)
            admins = list(reader)
        with open('admins.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for admin in admins:
                if admin[0] != name:
                    writer.writerow(admin)

    @staticmethod
    def view_admins():
        with open('admins.csv', mode='r') as file:
            reader = csv.reader(file)
            for admin in reader:
                print(admin)

    @staticmethod
    def check_admin(name, password):
        with open('admins.csv', mode='r') as file:
            reader = csv.reader(file)
            for admin in reader:
                if admin[0] == name and admin[1] == password:
                    print("Admin Successfully Logged in!")
                    return True
        print("Admin Details Incorrect")
        return False

class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type

def clear():
    return os.system('clear')

def menu():
    print("\n\n--------ATM--------\n\n")
    while True:
        user_option = input(print("|| Press 1 for Admin || Press 2 for User ||\n      || Press 3 to Exit! ||\n"))
        match user_option:
            case '1':
                clear()
                admin_panel()


            case '2':
                clear()
                username, password = input("Enter your Username and Password: ").split()
                if User.login(username, password):
                 user_panel(username)
            case '3':
                clear()
                print("Thank you for your time!\n")



def admin_panel():
    clear()
    admin_name, admin_pass = input(print("Enter Admin Username and Password: ")).split()
    if Admin.check_admin(admin_name, admin_pass):
            clear()
            while True:
                admin_choice = input(
                    " || Press 1 to View all Admins || Press 2 to Delete an Admin ||\n || Press 3 to Update an Admin || Press 4 to Create an Admin || \n || Press 5 for Admins' User Panel || Press 6 for Transaction Panel || Press 7 to log out ||\n")
                match admin_choice:
                     case '1':
                       Admin.view_admins()
                     case '2':
                       admin_name_delete,admin_pass_delete = input("Enter the name and password of the admin to delete: ").split()
                       if Admin.check_admin(admin_name_delete,admin_pass_delete):
                        Admin.delete_admin(admin_name_delete)
                        print(f"Admin {admin_name_delete} has been deleted \n")
                       else:
                        print("No such Admin exists in the Database\n")

                     case '3':
                         admin_update_name = input("Enter the name of the admin to be updated: ")
                         admin_update_pass = input("Enter the new password to be added: ")
                         Admin.update_admin(admin_update_name, admin_update_pass)

                     case '4':
                         admin_create_name, admin_create_password = input("Enter the new Admins Name and Password: ").split()
                         Admin.create_admin(admin_create_name,admin_create_password)
                     case '5':
                          admins_user_panel()

                     case '6':
                          transactions_panel('admin')
                     case '7':
                         break

def admins_user_panel():
    while True:
        admin_user_choice = input(
            " || Press 1 to Create a User || Press 2 to Delete a User||\n || Press 3 to Update a User || Press 4 to View the Users || \n || Press 5 to return ||\n")
        match admin_user_choice:
            case '1':
                user_name, user_password = input("Enter the new Users' name and password: ").split()
                Admin.create_user(user_name, user_password)
            case '2':
                user_name = input("Enter the username to be deleted: ")
                Admin.delete_user(user_name)
            case '3':
                user_name, user_password = input("Enter the username and password to be updated: ").split()
                Admin.update_admin(user_name, user_password)
            case '4':
                user_search_choice = input("Do you want to view all users or a specific user? [Press 1 for All users or 2 for Specific User] \n")
                if user_search_choice == '1':
                    Admin.view_users()
                elif user_search_choice == '2':
                    username = input("Enter the username to be searched: ")
                    Admin.search_user(username)
                else:
                    print("Incorrect Input! Try Again!")
                    return
            case '5':
                return
def user_panel(username):
                 while True:
                  user_choice = input("|| Press 1 to view your details || Press 2 to View/Make Transactions || Press 3 to Change your password ||\n|| Press 4 to Log Out ||\n")
                  if user_choice == '1':
                    Admin.search_user(username)
                  elif user_choice == '2':
                    transactions_panel('user')
                  elif user_choice == '3':
                    user_password_change = input("Enter the new password to be changed: ")
                    Admin.update_user(username,user_password_change)
                  elif user_choice == '4':
                    return
def transactions_panel(check):
    match check:
        case 'admin':
            admin_transaction_choice = input("|| Press 1 to view all transactions || Press 2 to delete all transactions || Press 3 to view specific transactions ||\n|| Press 4 to return ||")
            if admin_transaction_choice == '1':
                Admin.view_all_transactions()
            elif admin_transaction_choice == '2':
                Admin.delete_transactions()
            elif admin_transaction_choice == '3':
                username = input("Enter the username whose transactions you wish to search: ")
                print(username.User.view_transactions())
            elif admin_transaction_choice == '4':
                return

        case 'user':
            user_transaction_choice = input("|| Press 1 to deposit money || Press 2 to withdraw money || Press 3 to Transfer Funds to another user || Press 4 to view transactions || Press 5 to return ||\n")
            if user_transaction_choice == '1':
                deposit = int(input("Enter the amount to be deposited: "))
                username_deposit = input("Enter your username to confirm: ")
                User.add_transaction(username_deposit,deposit,'deposit')
                return
            elif user_transaction_choice == '2':
                withdrawal = int(input("Enter the amount to be withdrawn: "))
                username_withdrawal = input("Enter your username again to confirm: ")
                User.add_transaction(username_withdrawal,withdrawal,'withdrawal')
                return
            elif user_transaction_choice == '3':
                transfer = int(input("Enter the amount you wish to transfer: "))
                from_username = input("Enter your username to confirm: ")
                User.add_transaction(from_username,transfer,'transfer')
                return
            elif user_transaction_choice == '4':
                username = input("Enter your username to confirm: ")
                User.view_personal_transactions(username)
                return
            elif user_transaction_choice == '5':
                return



menu()