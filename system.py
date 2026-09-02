Accounts = []
import random

def open_account():
    account_title = input("Account title: ")
    cnic = input("Cnic no: ")
    contact = input("Contact no: ")
    initial_deposit = int(input("Initial Deposit: "))
    account_number = random.randint(10000,99999)
    account = {'title' : account_title,
               'cnic' : cnic,
               'contact' : contact,
               'balance' : initial_deposit,
               'account_number' : account_number}
    Accounts.append(account)
    print("Your Account Opened!")
    print(f"Your Account title is {account['title']} and Account number is {account['account_number']}")

def cash_deposit(acc_num, amount):
    if amount > 0:
        for acc in Accounts:
            if acc['account_number'] == acc_num:
                acc['balance'] += amount
                print("Amount deposited Successfully")
                break
        else:
            print("Invalid Account Number!")
    else:
        print("Invalid Amount!")

def check_balance(acc_num):
    for acc in Accounts:
            if acc['account_number'] == acc_num:
                print(f"Your Account holding the balance of Rs: {acc['balance']}")
                break
    else:
        print("Invalid Account Number!")

def cash_withdrawal(acc_num, amount):
    for acc in Accounts:
            if (acc['account_number'] == acc_num) and (acc['balance'] >= amount):
                acc['balance'] -= amount
                print(f"Here is your Amount of Rs: {amount}")
                break
    else:
        print("Invalid Account Number / or Insufficient Balance")

def close_account(acc_num):
    for i,acc in enumerate(Accounts):
            if acc['account_number'] == acc_num:
                print(f"Here is your amount {acc['balance']}")
                acc['balance'] = 0
                del Accounts[i]
                print("Your Acccount closed successfully")
                break
    else:
        print("Invalid Account Number!")

def transfer_amount(from_account, amount, to_account):
    for from_acc in Accounts:
        if from_acc['account_number'] == from_account:
            for to_acc in Accounts:
                if to_acc['account_number'] == to_account:
                    print("Amount Transferred!")
                    break
                else:
                    print("Invalid Amount reciever Account")
            else:
                print("Invalid Amount sender Account")

                