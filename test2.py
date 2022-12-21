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
from PIL import Image
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#text2="D:\converted_reduced_docx.txt"
#Importing Dataset
#mask1 = np.array(Image.open(r'C:\keywordsextracting\keywordsextracting\myshape.png'))
wc=WordCloud(background_color='black',height=1000,width=600)


#text2="D:\converted_reduced_docx.txt"
text = open(r'D:\converted_reduced_docx.txt',mode = 'r', encoding = 'utf-8').read()
text= re.sub(r'\b[a-zA-Z]{2}\b', '', text)
text= re.sub(r'\b[a-zA-Z]{1}\b', '', text)
#c = WordCloud(background_color='white',height=600,width=400)
wc.generate(text)
plt.imshow(wc, interpolation = "None")

# Off the x and y axis
plt.axis('off')

# Now show the output cloud
plt.show()

