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
old_name=file_path
myfile1= os.path.basename(file_path).split('/')[-1]
docfilename=myfile1.split(".")[0] 

MY_TEXT = docx2txt.process(file_path) 

with open("D:\converted_original_docx.txt", "w", encoding='utf-8') as text_file:  
    print(MY_TEXT, file=text_file)


stop_words = set(stopwords.words('english')) - set(['7T', '1.5T', '3T','9T'])  # remove stopwords"
file1 = open("D:\converted_original_docx.txt", encoding='utf-8')


# Use this to read file content as a stream:
line = file1.read()
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('D:\converted_reduced_docx.txt', 'a', encoding='utf-8')
        appendFile.write(" " + r)
        appendFile.close()

frequency = {}
document_text = open('D:\converted_reduced_docx.txt', 'r', encoding='utf-8')
text_string = document_text.read().lower()#r'\b[a-z]{3,15}\b'
regex1 = r'\d[-.]\d\d[a-zA-Z]'
regex2 = r'\d[-.]\d[a-zA-Z]'
regex3=r'\s\b\d[a-zA-Z]+'
regex4 = r'\b[a-zA-Z]{2,15}\b'  
match_pattern= re.compile("(%s|%s|%s|%s)" % (regex1, regex2, regex3, regex4)).findall(text_string)
for word in match_pattern:# extract words and their ferequencies 
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
wordlist = []
frequencylist = []
print(wordlist)
print(frequency)

keys = list(frequency.keys())
#print(keys[1])
myval = [*frequency.keys()]
myvals = [*frequency.values()]  # "name"
#print(myval)
#print(myvals)
dict = {'word': myval, 'frequency': myvals}

df = pd.DataFrame(dict)
dfsorted = df.sort_values(by='frequency', ascending=False)

folder = "D:\\test"

destination = folder + '\\'+docfilename +  ".csv"
dfsorted.to_csv(destination)

#____________________________________________________________________________

rake_nltk_var = Rake()
nltk.download('punkt')

rake_nltk_var.extract_keywords_from_text(MY_TEXT)
keyword_extracted = rake_nltk_var.get_ranked_phrases()[0:60]
keyword_extracted
dict = {'word': keyword_extracted}  
       
df = pd.DataFrame(dict) 

destination1 = folder + '\\'+ docfilename + "_phrase1" +".csv"
df.to_csv(destination1)

#_________________________________________________________________________
#open text file in read mode
text_file = open("D:\converted_reduced_docx.txt", "r", encoding='utf-8')
 
#read whole file to a string
data = text_file.read()
rake_nltk_var.extract_keywords_from_text(data)
#rake_nltk_var.get_ranked_phrases(0:30)
keyword_extracted = rake_nltk_var.get_ranked_phrases()[0:60]
keyword_extracted
dict1 = {'word': keyword_extracted}  
       
df2 = pd.DataFrame(dict1) 
    
 
destination2 = folder + '\\'+ docfilename + "_phrase2" +".csv"
df2.to_csv(destination2)
#document_text.close()
#file1.close()
#text_file.close()
#os.remove("D:\converted_original_docx.txt")
#os.remove("D:\converted_reduced_docx.txt")
#____________________________________________________________________________


#----------