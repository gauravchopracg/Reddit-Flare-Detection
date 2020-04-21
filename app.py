# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 23:02:20 2019

@author: Abhishek's PC
"""
from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
import pickle
from preprocessing import *
from forms import RedditForm

filename = 'rfr_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
app=Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
bootstrap = Bootstrap(app)


#@app.route('/', methods=['POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = RedditForm()
    if form.validate_on_submit():
        url = form.url.data
        a=detect_flair(url,loaded_model)
        predicted_flair=str(a[0])
        actual_flair = 'Politics'#predict(url)
        #predicted_flair = 'Policy'#predict(url)
        #flash('Flair for URL requested is {}'.format(predicted_flair))
        #return render_template('predict.html', url=url)
        #flash('Login requested for user {}'.format(
        #    form.url.data))
        return render_template('login.html',  title=predicted_flair, form=form, actual_flair=actual_flair, predicted_flair=predicted_flair)
        #return redirect(url_for('login'))
    return render_template('login.html',  title='FindFlair', form=form)


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