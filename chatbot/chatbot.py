import json 
import numpy as np
import pickle
import random
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
lemmatizer=WordNetLemmatizer()
intents=json.loads(open('intents.json').read())
words=pickle.load(open('words.pkl','rb'))
classes=pickle.load(open('classes.pkl','rb'))
model=load_model(open('chatbot_model.model'))
def clean_up(sentence):
    sentence_word=nltk.word_tokenize(sentence)
    sentence_word=[lemmatizer.lemmatize(word) for word in sentence_word]
    return sentence_word
def bag_of_words(sentence):
    sentence_word=clean_up(sentence)
    bag=[0]*len(words)
    for w in sentence_word:
        for i,word in enumerate(words):
            if (word==w):
                bag[i]=1
    return np.array(bag)
w=bag_of_words(words)
print(w)
def predict_class(sentence):
    bow=bag_of_words(sentence)
    res=model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD=0.25
    results=[(i,r) for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x:x[1],reverse=True)
    return_list=[]
    for r in results:
        return_list.append({'intent':classes[r[0]],'probability':str(r[1])})