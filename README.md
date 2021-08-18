<h1 align="center"> Mental Health Awareness Canada </h1>


<p align="center">
  <img src= "https://user-images.githubusercontent.com/76941265/128641349-5385754f-8252-4e83-acdb-e243b811d507.png" width="300" height="250">
</p>

Mental health issues are often not discussed due to the stigma behind them and this results in many people hesitating to seek help for their mental illnesses. Although the Canadian Government has funded several mental health resources for the general public, very few people utilize these platforms. The main reason for this is the lack of awareness regarding mental health concerns and the resources available in Canada. For my research on mental health awareness, I have developed a descriptive mental health Chatbot application called 'Mental Health Awareness Canada.' This Chatbot incorporates Natural Language Processing (NLP) and Deep Learning Techniques to provide users with a more interactive and friendly conversation when discussing mental health issues. The application also provides reliable support information taken from the official [Government of Canada](https://www.canada.ca/en/public-health/topics/mental-health-wellness.html) website.

[![Windows](https://svgshare.com/i/ZhY.svg)](https://www.microsoft.com/en-in/windows)  [![PyPI](https://img.shields.io/pypi/v/four)](https://pypi.org/project/pypi-install/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tensorflow)](https://www.python.org/downloads/release/python-380/) ![GitHub repo size](https://img.shields.io/github/repo-size/desireedmello/mentalhealthchatbotCanada) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange)](https://jupyter.org/try)

---

## Table of Contents

- [Repository Details](https://github.com/desireedmello/mentalhealthchatbotCanada/blob/main/README.md#repository-details)
- [Breakdown of the Repository Files](https://github.com/desireedmello/mentalhealthchatbotCanada/blob/main/README.md#breakdown-of-the-repository-files)
- [Installation](https://github.com/desireedmello/mentalhealthchatbotCanada/blob/main/README.md#installation)
- [Usage](https://github.com/desireedmello/mentalhealthchatbotCanada/blob/main/README.md#usage)
- [Mental Health Awareness Canada Demo](https://github.com/desireedmello/mentalhealthchatbotCanada/blob/main/README.md#mental-health-awareness-canada-demo)
- [Support](https://github.com/desireedmello/mentalhealthchatbotCanada/blob/main/README.md#support)
- [Road-map](https://github.com/desireedmello/mentalhealthchatbotCanada/blob/main/README.md#road-map)
- [Contributing](https://github.com/desireedmello/mentalhealthchatbotCanada/blob/main/README.md#contributing)
- [References](https://github.com/desireedmello/mentalhealthchatbotCanada/blob/main/README.md#references)
- [Project Status](https://github.com/desireedmello/mentalhealthchatbotCanada/blob/main/README.md#project-status)

---

## Repository Details

'Mental Health Awareness Canada' is available in .ipynb for Jupyter Notebook and .py Pycharm IDE (Works on both Community and Professional Pycharm IDE)

For Jupter Notebook consider the following files

```
- trainingmodel.ipynb      
- mentalhealthbot.ipynb
- mentalhealthCanada.json                
- vocabulary.pkl   
- categories.pkl             
- mentalhealthbot_model.h5
```

For Pycharm IDE consider the following files

```
- trainingmodel.py
- mentalhealthbot.py
- mentalhealthCanada.json
- vocabulary.pkl
- categories.pkl
- mentalhealthbot_model.h5
```

---

## Breakdown of the Repository Files:


- trainingmodel.ipynb / trainingmodel.py - Consists of the code required for training the model.
- mentalhealthbot.ipynb / mentalhealthbot.py - Consists of the code required for designing and running the model's GUI.
- mentalhealthCanada.json - Dataset consisting of mental health data and resources needed for training the model.
- vocabulary.pkl and categories.pkl - Stores the list of vocabulary and categories for the model.
- mentalhealthbot_model.h5 - The 'Mental Health Awareness Canada' model created by trainingmodel and used in mentalhealthbot.


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

First execute trainingmodel.ipynb / trainingmodel.py code to train the model and then execute mentalhealthbot.ipynb / mentalhealthbot.py code to run the application.

Note: While running the model you may encounter this error:

```
ImportError: Could not find the DLL(s) 'msvcp140_1.dll'. TensorFlow requires that these DLLs be installed in a directory that is named in your %PATH% environment variable. You may install these DLLs by downloading "Microsoft C++ Redistributable for Visual Studio 2015, 2017 and 2019" for your platform from this URL: https://support.microsoft.com/help/2977003/the-latest-supported-visual-c-downloads
```

If so please download the required Visual Studio from [Microsoft Support](https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0)

---

## Mental Health Awareness Canada Demo

![MHAC](https://user-images.githubusercontent.com/76941265/129854441-43e52b2c-84e7-4612-af3a-044552316c28.gif)

'Mental Health Awareness Canada' will responds to queries typed in by the user regarding mental health issues and resources available in Canada.

---

## Support

If you have any questions please email me at dmellod@lakeheadu.ca or desiree2dmello@gmail.com

---

## Road-map

- [x] Added mental health issues into 'Mental Health Awareness Canada'
- [ ] Need to add more resources funded by the Canadian Government
- [ ] Incorporate sentiment analysis on user responses

---

## Contributing

In case you encounter any issues please report them [here](https://github.com/desireedmello/mentalhealthchatbotCanada/issues)

---

## References

1.  Government of Canada, "Mental health and wellness," Canada, 12 April 2021. [Online]. Available: https://www.canada.ca/en/public-health/topics/mental-health-wellness.html. [Accessed 16 July 2021].
2.  A. Viraj, ”How To Build Your Own Chatbot Using Deep Learning," Medium, 1 November 2020. [Online]. Available: https://towardsdatascience.com/how-to-build-your-own-chatbot-using-deep-learning-bb41f970e281. [Accessed 16 July 2021].
3.  Amruta99, ”Learn to Develop Simple Chatbots using Python and Deep Learning!," Analytics Vidhya, 22 June 2021 [Online]. Available: https://www.analyticsvidhya.com/blog/2021/06/learn-to-develop-a-simple-chatbot-using-python-and-deep-learning/. [Accessed 16 July 2021].
4.  F. Chollet, ”The Sequential model," Keras, 12 April 2020.  [Online]. Available: https://keras.io/guides/sequential_model/. [Accessed 16 July 2021].
5. The Python Standard Library, ”Graphical User Interfaces with Tk," Python. [Online]. Available: https://docs.python.org/3/library/tk.html. [Accessed 16 July 2021].

---

## Project Status

'Mental Health Awareness Canada' is still open for further improvements.

