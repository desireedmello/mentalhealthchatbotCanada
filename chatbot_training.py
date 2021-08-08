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
words=[]
classes = []
documents = []

# List of characters to ignore
ignore_characters = ['?', '!']

# Opening and Loading the Dataset
data_file = open('intents.json').read()
intents = json.loads(data_file)

# Updating the words, classes and documents lists
for intent in intents['intents']:
    for pattern in intent['patterns']:

        # Tokenizing each word from pattern into the word list
        w = nltk.word_tokenize(pattern)
        words.extend(w)

        # Adding documents into the collection (corpus)
        documents.append((w, intent['tag']))

        # Adding unique tags into the classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Text pre-processing (lower case, remove non-alphanumeric characters and lemmatize text)
lemmatizer = WordNetLemmatizer()
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_characters]
words = sorted(list(set(words)))

# Sorting the classes list
classes = sorted(list(set(classes)))

# Documents list is a combination between intents and patterns
print (len(documents), "documents")

# Classes list is the intents
print (len(classes), "classes", classes)

# Words list is all the unique words
print (len(words), "unique lemmatized words", words)

# Converting the words and classes lists from objects into byte-stream and storing in respective pickle files
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

# Creating a list for the training data
training = []

# Creating an empty array to store the outputs
output_empty = [0] * len(classes)

# Training set will consist of bag of words for each text sentence
for doc in documents:
    # Creating the bag of words list
    bag = []

    # Creating a list of tokenized words for the pattern
    pattern_words = doc[0]

    # Lemmatizing each word - Creating base lemma words in an attempt to represent relative words
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]

    # Creating the bag of words array with 1, if word match is found in the current pattern
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # Output will be '0' for each tag and '1' will be for current tag (for each pattern)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# Shuffling the features and turning them into a numpy array
random.shuffle(training)
training = np.array(training)

# Creating the training and testing lists. X is the patterns, Y is the intents
train_x = list(training[:,0])
train_y = list(training[:,1])
print("Training data created")


# Creating the model - 3 layers. First layer contains 128 neurons, second layer contains 64 neurons
# and third output layer contains number of neurons that are equal to number of intents for predicting the output intent with softmax
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compiling the model. Using stochastic gradient descent with Nesterov accelerated gradient provides good results for the model
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Fitting and saving the model for future use
hist = model.fit(np.array(train_x), np.array(train_y), epochs=600, batch_size=8, verbose=1)
model.save('chatbot_model.h5', hist)

print("Model created")
