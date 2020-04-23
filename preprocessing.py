# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 23:02:20 2019

@author: Abhishek's PC
"""
from flask import Flask, render_template, request
import pandas as pd
import nltk
import numpy as np
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter
import re
import pickle
import praw
import pprint

#nltk.download('punkt')
#nltk.download('stopwords')
reddit = praw.Reddit(client_id='300HIOocldVcKA', client_secret='PCktLUhpPaRB1RrBCouEDPdpEBU', user_agent='abhishek chopra') # potentially needs configuring, see docs

def preProcessData(dataa):
    stopwords_en = list(set(stopwords.words('english')))
    def split(word): 
        return [char for char in word]   
    punchList = split(punctuation)

    wordTokenList = [word_tokenize(sent) for sent in dataa]
    lowercasingList = [[word.lower() for word in sentence] for sentence in wordTokenList]
    noStopWordList = [[word for word in sentence if word not in stopwords_en] for sentence in lowercasingList]
    noPunchList = [[re.sub(r'([^\s\w]|_)+', '', word) for word in sentence] for sentence in noStopWordList]
    #noPunchList = [[word for word in sentence if word not in punchList] for sentence in noStopWordList]
    PP_data = [[word for word in sentence if word] for sentence in noPunchList]
    return PP_data

def text_extractor(text,text_type):
    title_list=[]
    for i in range(len(text)):
        title_list.append(text[text_type][i])
    return title_list
def joiner(data):
    input_corrected = [" ".join(i) for i in data]
    return input_corrected
def detect_flair(url,loaded_model):

    submission = reddit.submission(url=url)
    topics_dict = {"title":[], "comments":[]}
    topics_dict["title"].append(submission.title)
    submission.comments.replace_more(limit=None)
    comment = ''
    for top_level_comment in submission.comments:
        comment = comment + ' ' + top_level_comment.body
    topics_dict["comments"].append(comment)
    
    topics_data = pd.DataFrame(topics_dict)
    feature_combine = topics_data["title"] + topics_data["comments"]
    topics_data = topics_data.assign(feature_combine = feature_combine)
    feature=text_extractor(topics_data,'feature_combine')
    x=joiner(preProcessData(feature))
    flair = submission.link_flair_text
    return (loaded_model.predict(x), flair)

filename = 'rfr_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))