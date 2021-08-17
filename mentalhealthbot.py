# Importing Required Libraries
import pickle
import numpy as np
import nltk
import json
import random
from nltk.stem import WordNetLemmatizer
from tkinter import *

# Importing the created model
from tensorflow.keras.models import load_model
botmodel = load_model('mentalhealthbot_model.h5')

# Retrieving the intents, words and classes

intents = json.loads(open('mentalhealthCanada.json').read())
vocabulary = pickle.load(open('vocabulary.pkl', 'rb'))
categories = pickle.load(open('categories.pkl', 'rb'))

# Returning the bag of words array = '0' or '1' for each word in the bag of words that exists in the sentence

def preprocessing(sentence):

    # Tokenizing the pattern
    sentences = nltk.word_tokenize(sentence)

    # Lemmatizing each word - creating short forms (lemma) for words
    lemma = WordNetLemmatizer()
    sentences = [lemma.lemmatize(word.lower()) for word in sentences]
    return sentences

# Returning the bag of words array = '0' or '1' for each word in the bag of words that exists in the sentence

def bagofwords(sentence, words, details=True):

    # Tokenizing the pattern
    sentences = preprocessing(sentence)

    # Bag of words - matrix of N words which is the vocabulary matrix
    bagofwords = [0]*len(words)
    for s in sentences:
        for i,w in enumerate(words):
            if w == s:

                # # Assigning 1 if the current word exists in the vocabulary position
                bagofwords[i] = 1
                if details:
                    print("found in bag: %s" % w)
    return(np.array(bagofwords))

# Defining the prediction classes

def prediction(sentence, model):

    # Filtering out predictions below a threshold of 0.25
    predict = bagofwords(sentence, vocabulary,details=False)
    res = model.predict(np.array([predict]))[0]
    error_threshold = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > error_threshold]

    # Sorting the results by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": categories[r[0]], "probability": str(r[1])})
    return return_list

# Defining the responses

def response(ints, intents_json):
    tag = ints[0]['intent']
    intents_list = intents_json['intents']
    for i in intents_list:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

# Defining chatbot responses based on users input queries

def chatbot_response(msg):
    ints = prediction(msg, botmodel)
    res = response(ints, intents)
    return res

# Chatbot GUI code adapted from Analytics Vidhya
# https://www.analyticsvidhya.com/blog/2021/06/learn-to-develop-a-simple-chatbot-using-python-and-deep-learning/.

# Creating GUI for the Mental Health Chatbot using tkinter

def send():
    message = input_box.get("1.0",'end-1c').strip()
    input_box.delete("0.0",END)

    if message != '':
        chat.config(state=NORMAL)
        chat.insert(END, "You: " + message + '\n\n')
        chat.config(foreground="#442265", font=("Verdana", 12), wrap='word')
    
        res = chatbot_response(message)
        chat.insert(END, "MHAC: " + res + '\n\n')
            
        chat.config(state=DISABLED)
        chat.yview(END)

base = Tk()
base.title("Mental Health Awareness Canada")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

# Creating the Display Window
chat = Text(base, bd=0, bg="#FBFCFC", height="8", width="50", font="Arial",)

chat.config(state=DISABLED)

# Binding a Scrollbar to the Display Window
scrollbar = Scrollbar(base, command=chat.yview, cursor="heart")
chat['yscrollcommand'] = scrollbar.set

# Creating a 'Send' Button for users to send messages
send_button = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#F06292", activebackground="#F06292",fg='#ffffff',
                    command= send )

# Creating the input box for users to enter messages
input_box = Text(base, bd=0, bg="white",width="29", height="5", font="Arial", wrap='word')

# Placing all the components for the Chatbot GUI

input_box.place(x=6, y=440, height=50, width=250)
scrollbar.place(x=376,y=6, height=386)
chat.place(x=6,y=6, height=425, width=370)
send_button.place(x=245, y=440, height=50)
base.mainloop()
