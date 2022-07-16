import random

import pymongo


def username_checker(z):
    try:
        for i in range(0, len(credentials_list)):
            if credentials_list[i]["username"] == z:
                print("The username is already existed.")
                return False
            else:
                return True
    except Exception as error:
        print(error)
        return False


def register(x, y):
    try:
        if username_checker(x) is True:
            random_id: int = random.randint(0, 1000)
            credentials = {"_id": random_id, "username": x, "password": y, "money": 1000}
            operation = collection.insert_one(credentials)
            print("You have registered successfully.Your id is", operation.inserted_id)
            print("_____________________________________________________")
            return True
        else:
            print("Please try again.")
            return False
    except Exception as error:
        print(error)
        return False


def login(a, b):
    try:
        for i in range(0, len(credentials_list)+1):
            if credentials_list[i]["username"] == a:
                if credentials_list[i]["password"] == b:
                    global id_user
                    id_user = i
                    print(f"You have logged in successfully,{a}.")
                    print("_______________________________________")
                    return True
                else:
                    print("Username or password is wrong.Try again.")
                    return False
            else:
                pass
    except Exception as error:
        print(error)
        return False


def transfer(x, y):
    try:
        for i in range(0, len(credentials_list)):
            print(credentials_list[i]["username"])
            if credentials_list[i]["username"] == x:
                if credentials_list[id_user]["money"] >= y:
                    real_transfer_id = credentials_list[i]["_id"]
                    obj = credentials_list[id_user]["money"]
                    query = {"_id": real_user_id, "username": login_username, "password": login_password}
                    new_value = {"$set": {"money": obj - y}}
                    collection.update_one(query, new_value)
                    credentials_list[id_user]["money"] = obj - y
                    obj1 = credentials_list[i]["money"]
                    credentials_list[i]["money"] = obj1 + y
                    query1 = {"_id": real_transfer_id, "username": x, "password": credentials_list[i]["password"]}
                    new_value1 = {"$set": {"money": obj1 + y}}
                    collection.update_one(query1, new_value1)
                    return True
                else:
                    print(f"You don't have enough money to transfer ${y} to {x}.")
                    return False
            else:
                pass
    except Exception as error:
        print(error)
        return False


def withdraw(a: int):
    try:

        if credentials_list[id_user]["money"] >= a:
            obj2 = credentials_list[id_user]["money"]
            credentials_list[id_user]["money"] = obj2 - a
            query2 = {"_id": real_user_id, "username": login_username, "password": login_password}
            new_value2 = {"$set": {"money": obj2 - a}}
            collection.update_one(query2, new_value2)
            print(f"You have withdrew ${a} successfully.")
            return True
        else:
            print(f"You don't have enough money to withdraw ${a}.")
            return False
    except Exception as erro:
        print(erro)
        return False


def deposit(b):
    try:
        obj2 = credentials_list[id_user]["money"]
        credentials_list[id_user]["money"] = obj2 + b
        query = {"_id": real_user_id, "username": login_username, "password": login_password}
        new_value = {"$set": {"money": obj2 + b}}
        collection.update_one(query, new_value)
        return True
    except Exception as e:
        print(e)
        return False


def name_changer(h):
    try:
        credentials_list[id_user]["username"] = h
        query = {"_id": real_user_id}
        new_value = {"$set": {"username": h}}
        collection.update_one(query, new_value)
        print("You have changed your name successfully.")
        print("_____________________________________")
        return True
    except Exception as er:
        print(er)
        return False


def password_changer(s):
    try:
        credentials_list[id_user]["password"] = s
        query = {"_id": real_user_id, "username": login_username}
        new_value = {"$set": {"password": s}}
        collection.update_one(query, new_value)
        print("You have changed your password successfully.\n"
              "_____________________________________________")
        return True
    except Exception as erro:
        print(erro)
        return False


while True:

    try:
        connection = pymongo.MongoClient("localhost", 27017)
        database = connection["my_db"]
        collection = database["my_collection"]
        print("Connection Success!")
        credentials_list: list = []
        id_user = 0
        dbs = collection.find()
        for d in dbs:
            credentials_list.append(d)
        print(credentials_list)
    except Exception as err:
        print(err)
    finally:
        print("Welcome to mobile banking service.")
        user_input = int(input("Press 1 to register.\n"
                               "Press 2 to login.\n"))
        if user_input == 1:
            user_name = input("Enter your username here:")
            password = int(input("Enter your password here:"))
            confirm_password = int(input("Enter your password again:"))
            if password == confirm_password:
                if register(user_name, password) is True:
                    continue
                else:
                    continue
            else:
                print("Passwords are not the same!")
                continue
        if user_input == 2:
            login_username = input("Enter your login username:")
            login_password = int(input("Enter your login password:"))
            if login(login_username, login_password) is True:
                while True:
                    real_user_id = credentials_list[id_user]["_id"]
                    user_input1 = int(input("Press 1 to Transfer Money.\n"
                                            "Press 2 to Withdraw Money.\n"
                                            "Press 3 to Update.\n"
                                            "Press 0 to log out.\n"))
                    if user_input1 == 0:
                        break
                    elif user_input1 == 1:
                        try:
                            receiver = input("Enter the username of the receiver:")
                            transfer_amount = int(input("Enter the amount to transfer:"))
                            if transfer(receiver, transfer_amount) is True:
                                print(f"You have transferred ${transfer_amount} to {receiver} successfully.")
                                continue
                            else:
                                print("Something went wrong.Try again.")
                        except Exception as error:
                            print(error)
                            continue
                    elif user_input1 == 2:
                        withdraw_amount = int(input("Enter amount to withdraw:"))
                        if withdraw(withdraw_amount) is True:
                            continue
                        else:
                            print("Something went wrong.Try again.")
                            continue
                    elif user_input1 == 3:
                        try:
                            user_input2 = int(input("Press 0 to go back.\n"
                                                    "Press 1 to deposit money.\n"
                                                    "Press 2 to change name.\n"
                                                    "Press 3 to change password.\n"))
                            if user_input2 == 1:
                                deposit_money = int(input("How much money would u like to deposit?\n"
                                                          "Enter here:"))
                                if deposit(deposit_money) is True:
                                    print(f"You have deposited ${deposit_money} successfully.")
                                    continue
                                else:
                                    print("Something went wrong.")
                                    continue
                            elif user_input2 == 2:
                                new_username = input("Enter your new username here:")
                                if name_changer(new_username) is True:
                                    break
                                else:
                                    print("Something went wrong!")
                                    continue
                            elif user_input2 == 3:
                                new_password = int(input("Enter your new password here:"))
                                if password_changer(new_password) is True:
                                    break
                                else:
                                    print("Something not correct!")
                                    continue
                            elif user_input2 == 0:
                                continue
                            else:
                                print("Please enter either 0 or 1 or 2 or 3.")
                                continue
                        except Exception as error1:
                            print(error1)
                            continue
