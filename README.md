<h1 align="center"> Mental Health Awareness Canada </h1>


<p align="center">
  <img src= "https://user-images.githubusercontent.com/76941265/128641349-5385754f-8252-4e83-acdb-e243b811d507.png" width="300" height="250">
</p>

Mental health issues are often not discussed due to the stigma behind them and this results in many people hesitating to seek help for their mental illnesses. Although the Canadian Government has funded several mental health resources for the general public, very few people utilize these platforms. The main reason for this is the lack of awareness regarding mental health concerns and the resources available in Canada. For my research on mental health awareness, I have developed a descriptive mental health Chatbot application called 'Mental Health Awareness Canada.' This Chatbot interface incorporates Natural Language Processing (NLP) and Deep Learning Techniques to provide users with a more interactive and friendly conversation when discussing mental health issues. It also provides reliable support information taken from the official [Government of Canada](https://www.canada.ca/en/public-health/topics/mental-health-wellness.html) website.

[![Windows](https://svgshare.com/i/ZhY.svg)](https://www.microsoft.com/en-in/windows)  [![PyPI](https://img.shields.io/pypi/v/four)](https://pypi.org/project/pypi-install/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tensorflow)](https://www.python.org/downloads/release/python-380/) ![GitHub repo size](https://img.shields.io/github/repo-size/desireedmello/mentalhealthchatbotCanada) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange)](https://jupyter.org/try)

---

## Repository details

'Mental Health Awareness Canada' is available in .ipynb for Jupyter Notebook and .py Pycharm IDE (Works on both Community and Professional Pycharm IDE)

For Jupter Notebook consider the following files

1. chatbot_training.ipynb      
2. mentalhealthbot.ipynb
3. intents.json                
4. words.pkl   
5. classes.pkl             
6. chatbot_model.h5                   

For Pycharm IDE consider the following files

1. chatbot_training.py
2. mentalhealthbot.py
3. intents.json
4. words.pkl
5. classes.pkl
6. chatbot_model.h5

---

## Breakdown of the repository files:

- chatbot_training.ipynb / chatbot_training.py - Consists of the code required for training the model.
- mentalhealthbot.ipynb / mentalhealthbot.py - Consists of the code required for designing the model's GUI.
- intents.json - Dataset needed for training the model.
- words.pkl and classes.pkl - Stores the responses of the model.
- chatbot_model.h5 - The Chatbot model created by chatbot_training and used in mentalhealthbot.

---

## Installation

The following packages are required for running the Chatbot:

1. [nltk](https://pypi.org/project/nltk/)
   - nltk.download('punkt')
   - nltk.download('wordnet')
2.  [numpy](https://pypi.org/project/numpy/)
3.  [tensorflow](https://pypi.org/project/tensorflow/)

---

## Usage

First execute chatbot_training.ipynb / chatbot_training.py code to train the model and then execute mentalhealthbot.ipynb / mentalhealthbot.py code to run the application.

![Media1](https://user-images.githubusercontent.com/76941265/128907253-eac01a8b-88d8-4a84-be88-dad171644b34.gif)

'Mental Health Awareness Canada' will responds to queries typed in by the user regarding mental health issues and resources available in Canada.

---

## Support

If you have any questions you can email me at dmellod@lakeheadu.ca or desiree2dmello@gmail.com

---

## Road-map

- [x] Added mental health issues into 'Mental Health Awareness Canada'
- [ ] Need to add more resources funded by the Canadian Government
- [ ] Incorporate sentiment analysis on user responses

---

## Contributing

- In case you encounter any issues please report them [here](https://github.com/desireedmello/mentalhealthchatbotCanada/issues)

---

## References

1.  F. Chollet, ”The Sequential model," Keras, 12 April 2020.  [Online]. Available: https://keras.io/guides/sequential_model/. [Accessed 16 July 2021].
2.  Data Flair, ”Python Chatbot Project – Learn to build your first chatbot using NLTK & Keras." [Online]. Available: https://data-flair.training/blogs/python-chatbot-project/. [Accessed 16 July 2021].


## Project Status

The project is still open for further improvements.

