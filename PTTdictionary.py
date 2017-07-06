# coding=Big5
import pyodbc
import nltk
from nltk.util import ngrams
import string

# load dictionary
path = 'C:\\Users\\david_000\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\jieba\\dict.big.txt'
mydict = getDictionary(path)

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\david_000\AppData\Local\Programs\Python\Python35\Scripts\tutorial\PTT.accdb;' 
)
cnxn = pyodbc.connect(conn_str)
cursor = cnxn.cursor()

nrow = 443687
unit = 1000
parts = nrow // unit + 1

result = {}
for part in range(0, parts):
    print(part)
    start = part * unit + 1 
    end = min(nrow, (part+1)*unit)
    # load data
    SQL = "SELECT title FROM PTT_Gossiping WHERE ID >"+ str(start) + "AND ID < " + str(end)
        
    cursor.execute(SQL)
    text = []
    for row in cursor.fetchall():
        text.append(str(row))
        
    removeSW(text)
    
    # connect all posts into a long string
    mytext = ''.join(text)
    len(mytext)
    
    u'''
    compute ngrams (bigram ~ ngram)
    '''
    ngramList = []
    n = 6
    for i in range(2, n):
        ngramList.append(word_grams(mytext, i))
        
    # remove short ngrams included in long ngrams
    # take only terms show in >= 1% of all articles. When short terms has 80% chance eclipsed in long terms, remove.
    myngrams = removeEclipsed(ngramList, n, 0.01 * unit, 0.2) 
    len(myngrams)
    
    u'''
    check dictionary
    '''
    for k, v in myngrams.items():
        if k not in mydict:
            if k in result.keys():
                result[k] += v
            else:
                result[k] = v
    
    len(result)

cursor.close()
cnxn.close()

len(result)



output = ""
for term, freq in result.items():
    output += term + " " + str(freq) + "\n"

output
text_file = open("C:\\Users\\david_000\\workspace\\chineseTM\\Output.txt", "w", encoding = 'utf8')
text_file.write(output)
text_file.close()
