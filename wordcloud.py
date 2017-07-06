'''
Created on Jul 4, 2017

@author: david_000
'''
from os import path
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import jieba.posseg as pseg
import matplotlib.pyplot as plt
import pyodbc
import numpy as np
from PIL import Image

mask = np.array(Image.open("C:\\Users\\david_000\\workspace\\chineseTM\\gossiping.png"))
#image_colors = ImageColorGenerator(mask)
jieba.set_dictionary('C:\\Users\\david_000\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\jieba\\dict.big.txt')
jieba.load_userdict('C:\\Users\\david_000\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\jieba\\user.txt')
jieba.load_userdict('C:\\Users\\david_000\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\jieba\\PTTdictionary.txt')

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\david_000\AppData\Local\Programs\Python\Python35\Scripts\tutorial\PTT.accdb;' 
)
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()

SQL = "SELECT title FROM PTT_Gossiping"
cursor.execute(SQL)
text = []
for row in cursor.fetchall():
    text.append(str(row))

#removeSW(text)

wordList = list(jieba.cut(' '.join(text), cut_all = False))
dict = {}
for word in wordList:
    if len(word) > 1:
        if word in dict.keys():
            dict[word] += 1
        else:
            dict[word] = 1

my_wordcloud  = WordCloud(width=1600, height=800, mask = mask).generate_from_frequencies(dict)

plt.imshow(my_wordcloud)
#plt.imshow(my_wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.show()


