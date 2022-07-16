
from django.shortcuts import render
from django.http import HttpResponse
import pymongo



def home(request):


        connection = pymongo.MongoClient("localhost",27017)
        database = connection["db"]
        collection = database['collect']
        data = collection.find_one()
        print(data)
        id, name, age, hobby = data["_id"], data["name"], data["age"], data["hobby"]
        return render(request, "results.html", {"id": id, "name": name, "age": age, "hobby": hobby})

def home1(request):
    
        return render(request, "results.html")


# Create your views here.


def about(request):
    return render(request, "about.html", {'data': "This is data."})

def add(request):
        uemail = request.POST['email']
        upassword = request.POST["password"]
        umoney = request.POST["money"]
        return render(request, "results1.html", {'email':uemail, 'password':upassword, 'money':umoney})


