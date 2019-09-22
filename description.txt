--------------------------------------------------------------------------------------------------------------------------------------------
General Description
--------------------------------------------------------------------------------------------------------------------------------------------
This project is based on tweet data collected from IPL T20 2019 matches which is currently ongoing. IPL is an Indian premier league T20 cricket tournament held every year.

I have collected latest tweets of this (2019) IPL matches with a set of hashtags mentioned below:
['#CSK', '#KKR', '#RCB', '#DC', '#KXIP', '#MI'] : These are the teams like Chennai Super Kings(CSK), Kolkata Night riders(KKR), Royal Challengers Bangalore(RCB), Mumbai Indians(MI), Kings XI Punjab(KXIP).

--------------------------------------------------------------------------------------------------------------------------------------------
requirements.txt
--------------------------------------------------------------------------------------------------------------------------------------------
>pip install -r requirements.txt
--------------------------------------------------------------------------------------------------------------------------------------------
collect.py
--------------------------------------------------------------------------------------------------------------------------------------------
This python file basically is for collecting the tweets dataset with all other attribute mentioned below:

1. screen_name: Screen name of the person who is tweeting.
2. userId: Unique user id of the person who is tweeting. It is provided by the tweeter API.
3. since_id: It is the date too since when the tweets were tweeted.
4. tweet: Actual tweet content.
5. description: Description of the tweets.
6. username: Username of the person who is tweeting.

All the collected tweets are saved in their respective teams name JSON files in a readable format as #CSK.json, #DC.json, #KKR.json, #KXIP.json, #MI.json, #RCB.json.

--------------------------------------------------------------------------------------------------------------------------------------------
cluster.py
--------------------------------------------------------------------------------------------------------------------------------------------
In this actually, I am passing my previously collected data from collect.py to cluster. I select only users who have twitted on more than one teams only and made a graph for them. Also, here I have removed all those users who follow or tweeted only for a single team. Then I am doing further analysis using Grivan Newman to identify clusters.

The graphs are saved in different .png files as clusters.png, cluster_1.png, cluster_2.png

--------------------------------------------------------------------------------------------------------------------------------------------
classify.py
--------------------------------------------------------------------------------------------------------------------------------------------
Here I am doing the sentiment analysis of the tweets. I have downloaded the dataset of previous years IPL matches tweet and labeled the data manually into 3 categories described below:
1. positive: All the tweets under this category are those tweets which seem to be a positive comment on the team.
2. negative: All the tweets under this category are those tweets which seem to be a negative comment on the team.
3. neutral: All the tweets under this category are those tweets which seem to be a neutral comment on the team.

The labeled dataset is stored in "ipl_manual_lablled_dataset.csv" file. Please note that we have less number of negative tweets in our labeled data. Then, I trained the model using a support vector machine (SVM) after converting all the words into word-vector using TfidfVectorizer. 
Once the training is done, I used that model to classify the latest tweets (from IPL match 2019) into positive, negative and neutral sentiments.

--------------------------------------------------------------------------------------------------------------------------------------------
summary.py
--------------------------------------------------------------------------------------------------------------------------------------------
It summarizes the complete logs into one file summary.txt. So, all the logs from above *.py are collected and summarizes it into summary.txt. 

--------------------------------------------------------------------------------------------------------------------------------------------
IMPORTANT NOTE:
--------------------------------------------------------------------------------------------------------------------------------------------
Please run the collect.py file several times so that more tweets are collected and stored. In one run it is able to collect up to 100 
tweets only
