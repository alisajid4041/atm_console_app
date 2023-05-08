# atm_console_app
------------
Installation 
------------

To install this app first clone the repostitory.
In bash,run the following command:

>git clone https://github.com/alisajid4041/atm_console_app.git

Next,navigate to the project directory:
> cd atm_console_app

Finally,run the app
>python3 main.py

------------
   USAGE
------------
Once this app is running, users will be prompted with three options.
If you wish to log in as an Admin, press 1.
If you wish to log in as a registered user, Press 2
If you wish to exit the application, Press 3

-------------
  FEATURES
-------------
The app will then guide users based on this intial selection.

Admins will be able to log in using their username and password in the correct format. Each admin can create other admins, create other users, change the passwords of other admins and users. They can view all transactions or specfic transactions of a user.
They can view all registered users and also search for a user. They can delete specfic transactions of a user or delete all transactions records from the database.

Users can only sign in if their account has been created by an admin. They can view their own profile and in their profile they can view their current balance, password, username and transaction history.

Users can perform three types of transactions: Deposit, withdrawal and Transfer
Users can deposit cash into their personal account by confirming their username and the amount they wish to deposit. They can also withdraw a certain amount and transfer an amount to another user in the database.

----------------
PROJECT STRUCTURE
-----------------
The project consists of 4 main files. One main python applicaton code and four csv files containing information.

main.py consists of the main application code.
admins.csv contains the username and password of all the admins registered
users.csv contains the username, password,balance of all the registered users.
transactions.csv contains the username,password,balance before transaction,balance after transactions, type of transaction and if it was a transfer, to whom the amount was transfered to.

---------------
PROJECT DETAILS
---------------

This project was made by Ali Sajid, using python3 on Pycharm and using libraries pandas,os,csv. 
A simple class structure for users,admins and transactions was used with various functions implemented depending on the users requests.
