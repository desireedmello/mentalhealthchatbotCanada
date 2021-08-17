# Importing Required Libraries
import json
import pickle
import random
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
import nltk
from nltk.stem import WordNetLemmatizer

# Making lists to store words, classes and documents

vocabulary_list = []
categories_list = []
document_list = []

# List of characters to ignore
characters = ['?', '!']

# Opening and Loading the Dataset
dataset = open('mentalhealthCanada.json').read()
intents = json.loads(dataset)

# Updating the vocabulary, categories and documents lists
for intent in intents['intents']:
    for pattern in intent['patterns']:

        # Tokenizing each word from pattern into the vocabulary list
        w = nltk.word_tokenize(pattern)
        vocabulary_list.extend(w)

        # Adding documents into the collection (corpus)
        document_list.append((w, intent['tag']))

        # Adding unique tags into the categories list
        if intent['tag'] not in categories_list:
            categories_list.append(intent['tag'])

# Text pre-processing (lower case, remove non-alphanumeric characters and lemmatize text)
lemma = WordNetLemmatizer()
vocabulary = [lemma.lemmatize(w.lower()) for w in vocabulary_list if w not in characters]
vocabulary = sorted(list(set(vocabulary)))

# Sorting the categories list
categories = sorted(list(set(categories_list)))

# Documents list is a combination between intents and patterns
print(len(document_list), "documents")

# Categories list is the intents
print(len(categories), "classes", categories)

# Vocabulary list is all the unique words
print(len(vocabulary), "Unique lemmatized words", vocabulary)

# Converting the vocabulary and categories lists from objects into byte-stream and storing in respective pickle files
pickle.dump(vocabulary,open('vocabulary.pkl','wb'))
pickle.dump(categories, open('categories.pkl', 'wb'))

# Creating a list for the training data
traininglist = []

# Creating an empty array to store the outputs
output_empty = [0] * len(categories)

# Training set will consist of bag of words for each text sentence
for doc in document_list:
    # Creating the bag of words list
    bagofwords = []

    # Creating a list of tokenized words for the pattern
    pattern_words = doc[0]

    # Lemmatizing each word - Creating base lemma words in an attempt to represent relative words
    pattern_words = [lemma.lemmatize(word.lower()) for word in pattern_words]

    # Creating the bag of words array with 1, if word match is found in the current pattern
    for w in vocabulary:
        bagofwords.append(1) if w in pattern_words else bagofwords.append(0)

    # Output will be '0' for each tag and '1' will be for current tag (for each pattern)
    output_row = list(output_empty)
    output_row[categories.index(doc[1])] = 1
    traininglist.append([bagofwords, output_row])

# Shuffling the training data and transforming the list into a numpy array
random.shuffle(traininglist)
training = np.array(traininglist)

# Creating the training and testing lists. X is the patterns, Y is the intents
X_train = list(training[:,0])
Y_train = list(training[:,1])
print("Training data created")

# Sequential model code adapted from 'Keras' documentation
# https://keras.io/guides/sequential_model/

# Creating the Chatbot model - 3 layers. First layer contains 128 neurons, second layer contains 64 neurons
# and third output layer contains number of neurons that are equal to number of intents for predicting the output intent with softmax

botmodel = Sequential()
botmodel.add(Dense(128, input_shape=(len(X_train[0]),), activation='relu'))
botmodel.add(Dropout(0.5))
botmodel.add(Dense(64, activation='relu'))
botmodel.add(Dropout(0.5))
botmodel.add(Dense(len(Y_train[0]), activation='softmax'))

# Compiling the Chatbot model.
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
botmodel.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Fitting and saving Chatbot the model for future use
createmodel = botmodel.fit(np.array(X_train), np.array(Y_train), epochs=1000, batch_size=8, verbose=1)
botmodel.save('mentalhealthbot_model.h5', createmodel)
print("Model created")

# Model Summary
botmodel.summary()

