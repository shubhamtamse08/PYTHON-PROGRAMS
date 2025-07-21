def deposit(accounts, ch, amt):
    accounts[ch] += amt
    print("Rs {} credited to your account".format(amt))


def withdraw(accounts, ch, amt):
    if accounts[ch] >= amt:
        accounts[ch] -= amt
        print("Rs {} withdrawn from your account".format(amt))
    else:
        print("Insufficient balance")


def transfer(accounts, ch):
    to_acc = int(input("Enter the account number to transfer to: "))
    if to_acc not in accounts:
        print("------NO ACCOUNT FOUND------")
        return

    amt = int(input("Enter the amount to transfer: "))
    if amt > accounts[ch]:
        print("Insufficient balance")
    else:
        accounts[ch] -= amt
        accounts[to_acc] += amt
        print("Rs {} transferred to account {}".format(amt, to_acc))


def menu(accounts, ch):
    while True:
        print("\nWelcome to Account Number {}".format(ch))
        print("Please enter your choice:")
        print("1. CHECK BALANCE")
        print("2. DEPOSIT")
        print("3. WITHDRAW")
        print("4. TRANSFER")
        print("5. LOGOUT")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Balance is Rs", accounts[ch])

        elif choice == 2:
            amt = int(input("Enter amount to deposit: "))
            deposit(accounts, ch, amt)

        elif choice == 3:
            amt = int(input("Enter amount to withdraw: "))
            withdraw(accounts, ch, amt)

        elif choice == 4:
            transfer(accounts, ch)

        elif choice == 5:
            print("Logging out...\n")
            break

        else:
            print("Invalid choice. Please try again.")

accounts = {101: 1000, 102: 2000, 103: 3000}


while True:
    print("-------BANK MANAGEMENT SYSTEM-------")
    ch = int(input("Enter Account Number (or 0 to Exit): "))

    if ch == 0:
        print("Exiting system. Goodbye!")
        break
    elif ch in accounts:
        menu(accounts, ch)
    else:
        print("Invalid Account Number.\n")
