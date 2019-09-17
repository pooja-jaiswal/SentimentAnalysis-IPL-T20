"""
Collect data.
"""
import os
from helper import get_twitter_API, json_loader, json_writer, hashtags, fprint

def get_tweets(twitter,hashtags,tweets,since_id):
    while True:
        try:
            responses = twitter.request('search/tweets',{'q':hashtags,'count':100,'lang':'en','max_id':since_id})
            for response in responses:
                tweets.append(response)
            return tweets
        except:
            break

def process_data(tweet):
    return [{'screen_name': each['user']['screen_name'], 'userid':each['user']['id'],
            'description':each['user']['description'], 'tweet':each['text'], 
            'username': each['user']['name'], 'since_id' : each['id']} for each in tweet]

def main():
    twitter = get_twitter_API()
    open('collect.txt', 'w')
    f = open('collect.txt', 'a')
    fprint('Collecting tweets........................', f)
    fprint('Started collecting tweets From Twitter Based on hashtags', f)
    min_id=0
    for tags in hashtags:
        tweets, tweets_from_file, since_id, users = [], [], [], []
        count = 0
        fprint("Collecting data for : "+tags,f)
        tweets_from_file = json_loader(tweets_from_file,tags)
        if tweets_from_file:
            for i in tweets_from_file:
                since_id.append(i['since_id'])
                if i['screen_name'] not in users:
                    users.append(i['screen_name'])
                    count+=1
            min_id = min(since_id)
        tweets = get_tweets(twitter,tags,tweets, min_id)
        tweets = process_data(tweets)
        for z in range(len(tweets)):
            if tweets[z]['screen_name'] not in users:
                users.append(tweets[z]['screen_name'])
                count+=1
        fprint("Total No. of Users who tweets for this hashtag : " + str(count), f)
        for i in tweets:
            tweets_from_file.append(i)
        json_writer(tweets_from_file, tags, f)
    print('Tweets saved to each hashtags file \n')
    f.close()

if __name__ == "__main__":
    print("--------------------------------- Started Collect -----------------------------------")
    for i in range(4):
        main()
    print("---------------------------------- Finished Collect -----------------------------------")
