from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'home.html')


def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')


def deletion(request):
    return render(request,'deletion.html')


def searching(request):
    return render(request,'searching.html')


class Node:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.left = None
        self.right = None


def minvalue(root):
    current = root
    while current.left is not None:
        current = current.left
    return current


def less_than(ob1, ob2):
    if ob1 != ob2:
        list2 = [ob1, ob2]
        list2.sort()
        print(list2)
        if list2[0] == ob1 and list2[1] == ob2:
            return True
        elif list2[0] == ob2 and list2[1] == ob1:
            return False
        else:
            print("Something went wrong.")
    else:
        print("They are the same.")

def inorder(root):
    if root is not None:
        inorder(root.left)
        list0.append(root.username)
        inorder(root.right)
    else:
        pass


def data_insertion(root, username, password):
    if root is None:
        return Node(username, password)
    elif username == root.username:
        print("The data is already in use.")
        pass
    elif less_than(username, root.username) is True:
        root.left = data_insertion(root.left, username, password)
    elif less_than(username, root.username) is False:
        root.right = data_insertion(root.right, username, password)
    else:
        print("Something went wrong.")
        pass
    return root


def delete(root, username):
    if root is not None:
        if username == root.username:
            if root.left is None:
                temp = root.right
                root.right = None
                return temp
            elif root.right is None:
                temp = root.left
                root.left = None
                return temp
            elif root.left and root.right is None and username != root.username:
                print("There's no such data.")
                return root
            elif root.left and root.right is None:
                root = None

                return root
            else:
                temp = minvalue(root.right)
                root.username = temp.username
                root.right = delete(root.right, temp.username)

        elif less_than(username, root.username) is True:
            root.left = delete(root.left, username)
        elif less_than(username, root.username) is False:
            root.right = delete(root.right, username)
        return root


    else:
        print("No data is in root.")
        return root


def searcher(root,username):
    if root is None:
        print("There's no such data.")
        return False

    elif root is not None:
        if username == root.username:
            print("There's a username called", username + ".")
            return True
        elif less_than(username, root.username) is True:
            if searcher(root.left, username) is True:
                return True
            else:
                return False
        elif less_than(username, root.username) is False:
            if searcher(root.right, username) is True:
                return True
            else:
                return False
        else:
            return False



def searching1(request):
    seausername = request.POST['username']
    if rootsearching(seausername) is True:
        print("Successfully searched.")
        return HttpResponse(f"Success! There's an account called {seausername}.")
    else:
        print("Searching Failed.")
        return HttpResponse(f"Failed! There's no account called {seausername}.")


def authentication(username, password):
    for h in range(0, len(list3)):
        if username[0] == list3[h].username[0]:
            if rootauthentication(list3[h], username, password) is True:
                return True
            else:
                return False
        elif username[0] != list3[h].username[0] and h == len(list3) - 1:
            return False
        else:
            pass


def rootauthentication(root, username, password):
    if root is None:
        print("There's no such data.")
        return False

    elif root is not None:
        if username == root.username:
            if password == root.password:
                print("Pass True.")
                return True
            else:
                print("Pass false.")
                return False
        elif less_than(username, root.username) is True:
            if rootauthentication(root.left, username, password) is True:
                return True
            else:
                return False
        elif less_than(username, root.username) is False:
            if rootauthentication(root.right, username, password) is True:
                return True
            else:
                return False
        else:
            return False


def add(request):
    try:
        uusername = request.POST['username']
        upassword = request.POST['password']
        uconfirm_password = request.POST['confirm_password']
        if upassword == uconfirm_password:
            if len(list3) == 0:
                list3.append(Node(uusername, upassword))
                return HttpResponse('Registered Successfully!!')
            elif len(list3) >= 1:
                for s in range(0, len(list3)):
                    if uusername[0] == list3[s].username[0]:
                        global list0
                        list0 = []
                        inorder(list3[s])
                        print(list0)
                        for i in list0:
                            print(str(i), uusername)
                            if uusername != str(i) and i == list0[-1]:
                                list3[s] = data_insertion(list3[s], uusername, upassword)
                                return HttpResponse('Registered Successfully!!')
                            elif uusername == i:
                                return HttpResponse('Username is not available.Try again.')
                            else:
                                pass
                                print("One")

                    elif uusername[0] != list3[s].username[0] and s == len(list3)-1:
                        list3.append(Node(uusername, upassword))
                        return HttpResponse('Registered Successfully.!')
                    else:
                        print("Here loop.")
                        pass
            else:
                return HttpResponse('Something went wrong.')
        else:
            print("Passwords are not the same.")
            return HttpResponse('Passwords are not the same.')

    except Exception as error:
        return HttpResponse(f"{error}")


def rootfordeletion(username):
    if len(list3) >= 1:
        for h in range(0, len(list3)):
            if username[0] == list3[h].username[0]:
                list3[h] = delete(list3[h], username)
                if list3[h] is None:
                    list3.pop(h)
                    print("Root cleared.")
                    print(list3)
                    return True
                else:
                    return True
            elif username[0] != list3[h].username[0] and h == len(list3) - 1:
                print("There's no such data.")
                return False
            else:
                pass
    else:
        print("There's no data registered.")
        return False



def rootsearching(username):
    if len(list3) >= 1:
        for h in range(0, len(list3)):
            if username[0] == list3[h].username[0]:
                if searcher(list3[h], username) is True:
                    return True
                else:
                    return False
            elif username[0] != list3[h].username[0] and h == len(list3) - 1:
                print("There's no such data.")
                return False
            else:
                pass
    else:
        print("There's no data registered.")
        return False


def loginchecker(request):
    info1 = request.POST['username']
    info2 = request.POST['password']
    if authentication(info1, info2) is True:
        return HttpResponse("Login Success!!")
    else:
        return HttpResponse('Username or password is wrong.Try again.')


def deletion1(request):
    delusername = request.POST['username']
    if rootfordeletion(delusername) is True:
        return HttpResponse(f"Successfully deleted {delusername}.")
    else:
        return HttpResponse("Fail Deletion!!")


list3 = []
list0 = []
