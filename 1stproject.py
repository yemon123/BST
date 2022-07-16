credentials: dict = {}
balance: dict = {}


def register(x, y):
    try:
        obj4: str = credentials[x]
        print("Username is already in use. Try again.")
        return False
    except KeyError:
        credentials[x] = y
        balance[x] = 1000
        print("You have registered your account successfully.\n"
              "You will be returned to our homepage.\n\n")
        return True


def login(a, b):
    try:
        if b == credentials[a]:
            print("Authentication is successful.\nWelcome to your account,", a)
            return True
        else:
            print("Username or password is wrong. Please try again.")
            return False
    except KeyError:
        print("Username or password is wrong. Please try again.")
        return False


def transfer(receiver, transfer_amount):
    try:
        obj: int = balance[login_username]
        balance[login_username] = obj - transfer_amount
        obj1: int = balance[receiver]
        balance[receiver] = obj1 + transfer_amount
        print("You have transferred ${} successfully.\n".format(transfer_amount))
        return True
    except KeyError:
        print("Please enter a valid username.")
        return False
    except receiver == login_username:
        print("You can't transfer to yourself. Try again.")
        return False


def withdraw(z):
    try:
        obj2: int = balance[login_username]
        if z > obj2:
            print("You don't have enough money. Please enter a valid amount.")

        else:
            balance[login_username] = obj2 - z
            print("You have withdraw successfully.")
            return True
    except ValueError:
        print("Please enter a valid amount.")
        return False


def deposit(x):
    try:
        obj3: int = balance[login_username]
        balance[login_username] = obj3 + x
        print("You have deposited ${} successfully.".format(x))
        return True
    except ValueError:
        print("Please enter a valid amount to deposit.")
        return False


def username_changer(x):
    credentials[x] = credentials.pop(login_username)
    balance[x] = balance.pop(login_username)
    print("You have changed your username successfully.")
    return True


def password_changer(x):
    credentials[login_username] = x
    print("You have changed your password successfully.")
    return True


while True:
    print("Welcome to our mobile banking system.")
    step1 = int(input("Press 1 to register or press 2 to login."))

    if step1 == 1:
        username = input("Enter your username here for registration:")
        psw = input("Enter your password here for registration:")
        psw_confirm = input("Please enter your password again:")
        if psw == psw_confirm:
            if register(username, psw) is True:
                continue
            else:
                continue

        else:
            print("Your input passwords are not the same. Try again!")
            continue

    elif step1 == 2:
        while True:
            print("Please enter your credentials to login.")
            login_username = input("Username: ")
            login_password = input("Password: ")

            while login(login_username, login_password) is True:
                print(credentials)  # To check whether the operation works
                print(balance)      # To check whether the operation works
                user_input = int(input("Press 1 to transfer.\n"
                                       "Press 2 to withdraw.\n"
                                       "Press 3 to update.\n"
                                       "Press 0 to logout.\n"
                                       ))
                if user_input == 1:
                    while True:
                        transfer_to = input("Enter the username of the receiver: ")
                        amount = int(input("Enter the transfer amount: "))

                        if transfer(transfer_to, amount) is True:
                            break
                        else:
                            continue

                elif user_input == 2:
                    while True:
                        withdraw_amount = int(input("Please enter the withdraw amount: "))

                        if withdraw(withdraw_amount) is True:
                            break
                        else:
                            continue

                elif user_input == 3:
                    while True:
                        update_input = int(input("Press 1 to deposit/update money.\n"
                                                 "Press 2 to change name.\n"
                                                 "Press 3 to change password.\n"))
                        if update_input == 1:
                            deposit_money = int(input("How much money would u like to deposit?\nEnter here: "))
                            if deposit(deposit_money) is True:
                                break
                            else:
                                continue

                        elif update_input == 2:
                            new_username: str = input("Please enter your new username: ")
                            if username_changer(new_username) is True:
                                break
                            else:
                                continue

                        elif update_input == 3:
                            new_password: str = input("Please enter your new password here: ")
                            if password_changer(new_password) is True:
                                break
                            else:
                                continue
                elif user_input == 0:
                    print("Bye Bye!!!\n\n")
                    break
    else:
        print("Please enter either 1 or 2.")
