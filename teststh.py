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


import numpy as np
from PIL import Image

import nltk #with this functions we expand stopwords with verbs and their derivative  
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
data = open(r'D:\converted2_reduced_docx.txt',mode = 'r', encoding = 'utf-8').read()
tokens = nltk.word_tokenize(data)
pos_tagged_tokens = nltk.pos_tag(tokens)

list_of_verbs = []
for i in range(len(pos_tagged_tokens)):
    if pos_tagged_tokens[i][1].startswith('V'):
       list_of_verbs.append(pos_tagged_tokens[i][0])
    
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(list_of_verbs)


              
file1 = open("D:\middle_converted_reduced_docx.txt", encoding='utf-8')#then we prone our text again aggainst having stop words 
#print(type(stop_words))

# Use this to read file content as a stream:
line = file1.read()
words = line.split()
for r in words:
    if not r in stopwords:
        appendFile = open('D:\converted_reduced_docx.txt', 'a', encoding='utf-8')
        appendFile.write(" " + r)
        appendFile.close()
                      