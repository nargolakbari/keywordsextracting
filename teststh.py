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

document_text = open('D:\converted_reduced_docx.txt', 'r', encoding='utf-8')
text_string = document_text.read().lower()
frequency = {}
regex1 = r'\d[-.]\d\d[a-zA-Z]'
regex2 = r'\d[-.]\d[a-zA-Z]'
regex3=r'\s\b\d[a-zA-Z]+'
regex4 = r'\b[a-zA-Z]{2,15}\b'  
match_pattern= re.compile("(%s|%s|%s|%s)" % (regex1, regex2, regex3, regex4)).findall(text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
wordlist = []
frequencylist = []


keys = list(frequency.keys())
#print(keys[1])
myval = [*frequency.keys()]
myvals = [*frequency.values()]  # "name"

dict = {'word': myval, 'frequency': myvals}

df = pd.DataFrame(dict)
dfsorted = df.sort_values(by='frequency', ascending=False)

folder = "D:\\result"
docfilename="myresult"
destination = folder + '\\'+docfilename +  ".csv"
dfsorted.to_csv(destination)