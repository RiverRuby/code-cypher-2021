# libraries used to extract, clean and manipulate the data
from helpers import *
import pandas as pd
import numpy as np
import string

# to plot the graphs
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# library used to count the frequency of words
from sklearn.feature_extraction.text import CountVectorizer

# to create the sentiment analysis model, tokenization and lemmatization
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize
import nltk.data
nltk.download('vader_lexicon')
nltk.download('punkt')

# genius token
client_id = 'PxzS3GRJYkyH8MVn1sgwMAzAiUSlqd_BICSisAVOlCCW9AmmzDg0IPCJC_qd1_qq'
client_secret = 'lTdOrNvmw0AoKElNZru1QDPl55sFy3EuoyXtWf4z9SII0Z7LhDcSwqRFU7AOSStuHG6CetaD2p8V_UFSooJJ8Q'
client_access = 'REZh59o8DCDIAX0B66n5eiKSm9ZGzbcsQ5WVywPdswHmRGRTgJOf-wIvZ0aFeK44'