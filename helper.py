from TwitterAPI import TwitterAPI
from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt
import json
import csv
 
hashtags = ['#CSK', '#KKR', '#RCB', '#DC', '#KXIP', '#MI']
labelled_file_name = 'ipl_manual_lablled_dataset.csv'

def get_twitter_API():
    consumer_key = 'epJYPK1oZcp0Xo7qmetBNxc6L'
    consumer_secret = 'yYPfZg5IaD5fYDYpCtajMtv3LbPmpCuOkSfY6tfCKXNJzs1TLf'
    access_token = '1080608208635527168-rRnlkanJNBVNXCTREXPVKYNMSKY6gH'
    access_token_secret = 'hYdEk53X1W4ehTmdoZa2ivAKLZWPFilaAuVwYxCv08ZvM'
    return TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

def json_loader(tweets, filename):
    fname= filename+'.json'
    p = Path(fname)
    if p.is_file():
        with open(fname, "rb") as file:
            try:
                tweets = json.load(file)
            except EOFError:
                return tweets
    return tweets

def csv_loader():
    data =[]
    label = []
    with open(labelled_file_name, 'r', encoding="utf8") as fp:
        csv_reader = csv.reader(fp)
        for row in csv_reader:
            label.append(row[0])
            data.append(row[1])
    fp.close()
    return data, label

def json_writer(tweets, filename, f):
    fname=filename+'.json'
    fprint("Total Tweets collected for %s : " %filename+ str(len(tweets)), f)
    json.dump(tweets, open(fname, 'w'), indent=1, sort_keys=True)

def load_test_data(fname):
    p = Path(fname)
    tweets_data = []
    if p.is_file():
        with open(fname, "rb") as file:
            tweets = json.load(file)
        for each in tweets:
            tweets_data.append(each['tweet'])
    return tweets_data

def draw_network_graph(graph, users, f):
    labels = {}
    pos=nx.spring_layout(graph)
    plt.figure(figsize=(100, 100))
    nx.draw(graph, pos, with_labels=False, node_size=3000)
    for node in graph.nodes():
        for i in users:
            if i == node:
                labels[node] = i
    nx.draw_networkx_labels(graph,pos, labels=labels, font_size=55, font_color='b')
    plt.savefig(f)
    return graph

def fprint(content, f):
    f.write(content+'\n')
    print(content)
