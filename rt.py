import io
import os
import pandas as pd
import numpy as np
import PyPDF2
from rake_nltk import Rake
# import textract
import docx2txt
import tkinter as tk
from tkinter import  filedialog
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# pip install wordcloud
#from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
frequency = {}
document_text = open('D:\converted_reduced_docx.txt', 'r', encoding='utf-8')
text_string = document_text.read().lower()#r'\b[a-z]{3,15}\b'


match_pattern = re.findall(r'\b[a-z]{2,15}\b'|'\d[-.]\d[a-zA-Z]', text_string)  
#match_pattern = re.findall(r'\W+', text_string)
for word in match_pattern:  
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
wordlist = []
frequencylist = []
print(wordlist)
print(frequency)