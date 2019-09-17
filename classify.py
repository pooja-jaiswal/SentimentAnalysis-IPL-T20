"""
Classify data.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from sklearn import svm
from pathlib import Path
from helper import fprint, csv_loader, load_test_data, hashtags

def train(data_list,train_test_flag):
    vectorizer = TfidfVectorizer(min_df=4,max_df=0.8,sublinear_tf=True,use_idf=True,stop_words=stopwords.words('english'))
    data_vector = vectorizer.fit_transform(data_list)
    return data_vector,vectorizer

def classify(test_vector,train_vector,train_labels):
    classifier_linear = svm.SVC(kernel='linear')
    classifier_linear.fit(train_vector, train_labels)
    return classifier_linear.predict(test_vector)

def test(test_data_list,vectorizer):
    return vectorizer.transform(test_data_list)

def print_data(tag, test_data,predicted_labels):
    pos_instance, neg_instance, neutral_instance, index_pos_instance, index_neg_instance, index_neutral_instance = 0,0,0,0,0,0
    for i in range(len(predicted_labels)):
        if predicted_labels[i] == "negative":
            index_neg_instance = i
            neg_instance+=1
        elif predicted_labels[i] == "positive":
            index_pos_instance = i
            pos_instance+=1
        elif predicted_labels[i] == "neutral":
            index_neutral_instance = i 
            neutral_instance+=1
    with open("classify.txt",'a', encoding="utf8") as fp:
        fprint("*********************************"+tag +"**************************************", fp)
        fprint("Positive Number of Tweets for "+tag+" : " + str(pos_instance), fp)
        fprint("Negative Number of Tweets for "+tag+" : "+ str(neg_instance), fp)
        fprint("Neutral Number of Tweets for "+tag+" : "+ str(neutral_instance), fp)

        fprint("Positive Tweets Example for "+tag+" : " + str(test_data[index_pos_instance]).replace("\n",""), fp)
        fprint("Negative Tweets Example for "+tag+" : " + str(test_data[index_neg_instance]).replace("\n",""), fp)
        fprint("Neutral Tweets Example for "+tag+" : " + str(test_data[index_neutral_instance]).replace("\n",""), fp)
    fp.close()

def main():
    print("--------------------------------- Started Classifier ----------------------------------- ")
    train_data, train_label = csv_loader()
    train_vector, vectorizer = train(data_list=train_data, train_test_flag="train")
    open("classify.txt" , "w")
    for each in hashtags:
        test_data = load_test_data(each+".json")
        test_vector = test(test_data_list=test_data, vectorizer=vectorizer)
        predicted_labels = classify(test_vector=test_vector,train_vector=train_vector,train_labels=train_label)
        print_data(each, test_data=test_data,predicted_labels=predicted_labels)
    print("---------------------------------- Finished Classifier -----------------------------------")

if __name__ == main():
    main()