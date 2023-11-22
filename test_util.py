import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import contractions
import re
from nltk.tokenize import word_tokenize
import pandas as pd
import snscrape.modules.twitter as sntwitter

# Using TwitterSearchScraper to scrape data and append tweets to list


def load_files():
    try:
        with open("saved_model/SVM.sav", "rb") as file:
            ei_classifier = pickle.load(file)
    except FileNotFoundError:
        print("Model not found!")

    try:
        with open("vectorizer.pkl", "rb") as file:
            vectorizer = pickle.load(file)
    except FileNotFoundError:
        print("Tokenizer not found!")

    return ei_classifier, ns_classifier, ft_classifier, jp_classifier, vectorizer
    
def preprocessing(text):
    stopword_list = stopwords.words("english")
    lemmatizer = WordNetLemmatizer()
    
    text = contractions.fix(text)
    text = text.lower()
    text = re.sub(r'@([a-zA-Z0-9_]{1,50})', '', text)
    text = re.sub(r'#([a-zA-Z0-9_]{1,50})', '', text)
    text = re.sub(r'http[s]?://\S+', '', text)
    text = re.sub(r'[^A-Za-z0-9]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = " ".join([word for word in text.split() if not len(word) <3])
    text = word_tokenize(text)
    text = [word for word in text if not word in stopword_list]
    text = [lemmatizer.lemmatize(word) for word in text]
    text = " ".join(text)
    return text

def get_prediction(username):
    ei_classifier, vectorizer = load_files()
    tweet=username
    text   = preprocessing(text)
    text   = vectorizer.transform([text])
    
    prediction = ""
    e_or_i = "E" if ei_classifier.predict(text)[0] == 1 else "I"
    prediction = e_or_i + n_or_s + f_or_t + j_or_p
   
    print(dec, prediction, tweets)
    return dec, prediction, tweets


name = input()
get_prediction(name)