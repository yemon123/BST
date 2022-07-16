#from django.shortcuts import render
#from django.http import HttpResponse

import pymongo
import json

try:
    connection = pymongo.MongoClient("localhost",27017)
    database = connection["db"]
    collection = database['collect']
 
   
    print("SUccess")
except Exception as err:
    print(err)
# Create your views here.

try:
        data1 = collection.find_one()
        for d in data1.items():
            print(d)
        print(data1)
except Exception as error:
        print(error)
    