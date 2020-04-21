from flask import render_template
from app import app
from preprocessing import *
from app.forms import RedditForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = RedditForm()
    if form.validate_on_submit():
        url = form.url.data
        a, b =detect_flair(url,loaded_model)
        predicted_flair=str(a[0])
        actual_flair = b#predict(url)
        #predicted_flair = 'Policy'#predict(url)
        #flash('Flair for URL requested is {}'.format(predicted_flair))
        #return render_template('predict.html', url=url)
        #flash('Login requested for user {}'.format(
        #    form.url.data))
        return render_template('login.html',  title=predicted_flair, form=form, actual_flair=actual_flair, predicted_flair=predicted_flair)
        #return redirect(url_for('login'))
    return render_template('login.html',  title='FindFlair', form=form)