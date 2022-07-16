
def list_to_dict_converter(v):
    mydict = {v[i]: v[i+1] for i in range(0, len(v), 2)}
    return mydict


def list_to_dict_converter1(v):
    mydict = {v[i]: int(v[i+1]) for i in range(0, len(v), 2)}
    print(mydict)
    return mydict


def authentication(u, p):
    try:
        confidential_dict[u] = p
        print(f"You have logged in successfully,{u}")
        return True
    except KeyError:
        print("Username or password is wrong.")
        return False


def transfer(receiver, transfer_amount):
    try:
        if receiver != login_username:
            if money_amount_dict[login_username] >= transfer_amount:
                obj: int = money_amount_dict[login_username]
                money_amount_dict[login_username] = obj - transfer_amount
                obj1: int = money_amount_dict[receiver]
                money_amount_dict[receiver] = obj1 + transfer_amount
                print(f"You have transferred ${transfer_amount} successfully.\n")
                return True
            else:
                print(f"You dont have enough money to transfer ${transfer_amount} to {receiver}.")
        else:
            print("You can't transfer to yourself.")
            return False
    except KeyError:
        print("Please enter a valid username.")
        return False


def withdraw(amount):
    try:
        if amount > money_amount_dict[login_username]:
            print(f"You don't have enough money to withdraw ${amount}.")
            return False
        elif amount <= money_amount_dict[login_username]:
            obj2 = money_amount_dict[login_username]
            money_amount_dict[login_username] = obj2 - amount
            print(f"You have successfully withdrew ${amount}.")
            return True
        else:
            print("Something went wrong.Try again.")
            return False
    except ValueError:
        print("Please enter a valid amount.")
        return False


def deposit(amount):
    try:
        obj6 = money_amount_dict[login_username]
        money_amount_dict[login_username] = obj6 + amount
        print(f"You have deposited ${amount} successfully.")
        return True
    except ValueError:
        print("Please enter a valid amount.")
        return False


def name_changer():
    new_username = input("Please enter your new username here: ")
    confidential_dict[new_username] = confidential_dict.pop(login_username)
    money_amount_dict[new_username] = money_amount_dict.pop(login_username)
    return True


def password_changer():
    new_password = input("Enter your new password: ")
    confirm_new_password = input("Enter your new password again: ")
    if new_password == confirm_new_password:
        confidential_dict[login_username] = new_password
        print("You have changed your password successfully.")
        return True
    else:
        return False


def data_saver():
    list1 = []
    list2 = []
    file_pointer2 = open("confidential.txt", "w")
    file_pointer3 = open("money_amount.txt", "w")
    for key, value in confidential_dict.items():
        list1.append(key)
        list1.append(value)
    for key1, value1 in money_amount_dict.items():
        list2.append(key1)
        list2.append(str(value1))
    for i in list1:
        file_pointer2.write(f"{i}\n")
    for j in list2:
        file_pointer3.write(f"{j}\n")
    file_pointer2.close()
    file_pointer3.close()


while True:
    try:

        confidential_file = open("confidential.txt", "r")
        money_amount = open("money_amount.txt", "r")
        content = confidential_file.read()
        content1 = money_amount.read()
        real_list = content.splitlines()
        real_list1 = content1.splitlines()
        confidential_dict: dict = list_to_dict_converter(real_list)
        money_amount_dict: dict = list_to_dict_converter1(real_list1)
        confidential_file.close()
        money_amount.close()
    except IOError:
        pass
    finally:
        print("Welcome to the online banking system.")
        userinput = int(input("Press 1 to register or 2 to login: "))
        if userinput == 1:
            file_pointer = open("confidential.txt", "a")
            file_pointer1 = open("money_amount.txt", "a")
            username: str = input("Enter your username here: ")
            password: str = input("Enter your password here: ")
            confirm_password: str = input("Enter your password again here: ")
            if password == confirm_password:
                try:
                    obj4: str = confidential_dict[username]
                    print("Username is already in use. Try again.")
                    continue
                except KeyError or NameError:
                    file_pointer.write(f"{username}\n{password}\n")
                    file_pointer1.write(f"{username}\n1000\n")
                    file_pointer.close()
                    file_pointer1.close()
                    print("You have registered your account successfully.\n"
                          "----------------------------------------------")
                    continue
            elif password != confirm_password:
                print("Your passwords are not the same.Try again.\n")
                continue
            else:
                print("Something went wrong.")
                continue
        elif userinput == 2:
            print("\n--------------------------\n"
                  "Welcome to the login page.")
            login_username: str = input("Enter your login username here: ")
            login_password: str = input("Enter your login password here: ")
            if authentication(login_username, login_password) is True:
                while True:

                    userinput1 = int(input("Press 1 to Transfer Money.\n"
                                           "Press 2 to Withdraw Money.\n"
                                           "Press 3 to Update.\n"
                                           "Press 0 to go back.\n"))
                    if userinput1 == 0:
                        continue
                    elif userinput1 == 1:
                        userinput2 = input("Enter the receiver username: ")
                        userinput3 = int(input("Enter the transfer amount: "))
                        if transfer(userinput2, userinput3) is True:
                            data_saver()
                            continue
                        else:
                            continue
                    elif userinput1 == 2:
                        withdraw_amount = int(input("Enter your withdraw amount: "))
                        if withdraw(withdraw_amount) is True:
                            data_saver()
                            continue
                        else:
                            continue
                    elif userinput1 == 3:
                        userinput4 = int(input("Press 1 to deposit money.\n"
                                               "Press 2 to change name.\n"
                                               "Press 3 to password change.\n"))
                        if userinput4 == 1:
                            deposit_amount = int(input("Enter a deposit amount: "))
                            if deposit(deposit_amount) is True:
                                data_saver()
                                continue
                            else:
                                continue
                        elif userinput4 == 2:
                            if name_changer() is True:
                                data_saver()
                                break
                            else:
                                break
                        elif userinput4 == 3:
                            if password_changer() is True:
                                data_saver()
                                break
                            else:
                                break
                        else:
                            print("Please enter either 1 or 2 or 3.")
                            continue
                    else:
                        print("Please enter either 1 or 2 or 3.")
            else:
                print("Username or password is wrong.")
                continue
        else:
            print("Please enter either 1 or 2.")
            continue
