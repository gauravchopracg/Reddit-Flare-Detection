# Reddit-Flare-Detection
This repository contains the details and documents on how to build a Reddit Flare Detection Machine Learning Web Application.It can be found here and to test the performance of classifier prepare a .txt file which contains a link of a r/india post in every line and send an automated POST request. Response of the request should be a json file in which key is the link to the value should be predicted flare. Evaluate predictions by using appropriate metric. Details of testing performance of your classifier can be found here.

**The task has been divided into 5 parts:**
# Part I - Reddit Data Collection
It includes the process of how to collect data from Reddit, which tool to use and how much data to collect. Details can be found in this notebook.

# Part II - Exploratory Data Analysis (EDA)
This part of project is dedicated on understanding the data, building intuition about it and performing analysis on it. In this part we further perform data cleaning and try to extract useful features from it. 

# Part III - Building a Flare Detector
By utilizing data processed from above steps. We try to build a classifier which can predict the flare of r/india posts. Each post is tagged wich topics like Politics, AskIndia, Science/Technology etc. The dataset is divided into train and validation.

# Building a Web Application
In this step, we picked the filed
