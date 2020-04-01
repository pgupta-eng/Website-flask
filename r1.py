
from flask import Flask, render_template# flask provides the libraries to host the website, render templates allows us to access html tags
import urllib.request as pain #allows us to access thingspeak get the data in the dictionary
from urllib.request import urlopen #internal communication to opens the website(thingspeak)
import requests #shows a unique user key(get and post)
from io import StringIO #python's internal library
import csv #extension of excel sheet, convert list in csv
from flask import Flask, render_template
import numpy as np #(numerical python) it makes easier process for mathematical operations
import json #it is used to pass the jason, opens json file
import random 

#URL making
n=7200    #number of elements you want to get. eg n=2, will give last 2 elements
temp_url='https://api.thingspeak.com/channels/984645/feeds.csv?api_key=DRPTJ68XDJ4KQ6Q2&results=2'    # IMPORTANT: CHANGE THE number 790730 and api_key ACCORDING TO YOUR DATABASE
add='results='
t=str(n)
addf=add+t
main_url=temp_url+addf
#print(main_url)

while(1):
#URL open and get data
 with pain.urlopen(main_url) as url: # fetch the data from thingspeak
    s=str(url.read(),encoding="utf-8")
    r=list(s.split(","))
 print("The data in form of list is",r)
 def l():
    last_item = int(r[-1]) # using list slicing the list is passed to the website
    return(last_item)
 def hum():
    hum_value = int(r[-3])
    return(hum_value)
 
 p = hum()
 q = l()
 print(type(p))
 print(type(q))

 app = Flask(__name__)
 latitude = 32
 longitude = 45
 print(q)
 def x():
    if q<30:
 	    stri = "Product is fresh"
    else:
 	    stri = "Product is spoilt"
    return(stri)
 r = x()
        

 @app.route('/')
 def home():
     return render_template("index.html", longitude=45, latitude=32,p=p,r=r, q=q)
 


 if __name__=='__main__' :
     app.run()
