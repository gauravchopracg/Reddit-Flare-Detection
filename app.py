# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 23:02:20 2019

@author: Abhishek's PC
"""
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import pickle
from preprocessing import *

filename = 'rfr_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
app=Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
     if request.method=='POST':
        link=request.form["email_name"]
        a=detect_flair(link,loaded_model)
        str_a=str(a[0])
        print(str_a)
        return render_template("success.html",str_a= str_a,link=link)
if __name__=='__main__':
    app.debug=True
    app.run()