from flask import render_template, request, jsonify
from app import app
from utils2 import *
from app.forms import RedditForm
from werkzeug.utils import secure_filename
import os


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = RedditForm()
    if form.validate_on_submit():
        path = form.url.data
        predicted_flair, actual_flair = predict(path)
#        path = [path]
#        res, flair = process(list(path))
#        a, b =detect_flair(url,loaded_model)
#        predicted_flair=res[path[0]]#str(a[0])
#        actual_flair = flair#b#predict(url)
        #predicted_flair = 'Policy'#predict(url)
        #flash('Flair for URL requested is {}'.format(predicted_flair))
        #return render_template('predict.html', url=url)
        #flash('Login requested for user {}'.format(
        #    form.url.data))
        return render_template('login.html',  title=predicted_flair, form=form, actual_flair=actual_flair, predicted_flair=predicted_flair)
        #return redirect(url_for('login'))
    return render_template('login.html',  title='FindFlair', form=form)

# automated testing endpoint
# this endpoint will be used for testing performance of the classifier
@app.route('/testing', methods=['GET', 'POST'])
def test():
    json = {}
    if request.method == 'POST':
        for i in request.files:
            file = request.files[i]
            urls = file.read()
            urls = urls.decode("utf-8").split("\n")
            urls = [i.replace("\r","") for i in urls]

#        file = request.files['file']
#        if file:
#            filename = secure_filename(file.filename)
#            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#            f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'r+')
#            urls = [line.rstrip('\n') for line in f.readlines()]
            #res = process(urls)
            #json = res[0]

            #f.close()
            for url in urls:
                a, _ =predict(url)
            #    predicted_flair=str(a[0])
                json[url] = a

            return jsonify(json)
    return "Error in file upload"

@app.route('/text-example', methods=['GET', 'POST']) #GET requests will be blocked
def text_example():
    if request.method == 'POST':
        for i in request.files:
            file = request.files[i]
            urls = file.read()
            urls = urls.decode("utf-8").split("\n")
            urls = [i.replace("\r","") for i in urls]
#        file = request.files['file']
#        if file:
#            filename = secure_filename(file.filename)
#            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#            f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'r+')
#            urls = [line.rstrip('\n') for line in f.readlines()]
            return jsonify(urls)#redirect(url_for('index'))
    return "Error in file upload"
