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
root=tk.Tk()
root.withdraw()
file_path=filedialog.askopenfilename()
print(os.path.splitext(file_path)[0])
myfilename = print(os.path.splitext(file_path)[0])
print("hey&&&&&&&&&&:  ")
print(myfilename)  