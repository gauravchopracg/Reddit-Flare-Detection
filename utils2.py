import praw
import pickle

reddit = praw.Reddit(client_id='8COttBbmIJSb3w',
                     client_secret='-zZqO_s0SQ-kfgyk3Dt9Y8JUXAM',
                     username='himanshu_garg_',
                     password='qwertyqwerty',
                     user_agent='himanshu_garg_')

# loading model and vectorizer
loaded_model = pickle.load(open('SGDC.pickle','rb'))
vectorizer = pickle.load(open('SGDC_vector.pickle','rb'))

def predict(name):
    try:
        subreddit = reddit.submission(url=name)
        actual_flair = subreddit.link_flair_text
        predicted_flair = loaded_model.predict(vectorizer.transform([subreddit.title]))
        return (predicted_flair[0], actual_flair)
    except:
        return 'Check URL...', 'Check URL....'