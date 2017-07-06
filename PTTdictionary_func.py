'''
Created on Jul 4, 2017

@author: david_000
'''
# -*- coding: Big5 -*-
import nltk
from nltk.util import ngrams
import string


def removeSW(stringList): 
    path = 'C:\\Users\\david_000\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\jieba\\ChineseSW.txt'
    sws = open(path, 'r', encoding = 'utf8').readlines()
    stop = []
    for sw in sws:
        stop.append(sw.replace("\n", ""))
    
    punc = set(string.punctuation + ' ' + '¡u' + '¡v' + '¡y' + '¡z')
    for i in range(0, len(stringList)):
        stringList[i] = stringList[i].replace("\\n", "")
        stringList[i] = ''.join(ch for ch in stringList[i] if ch not in punc)
        for s in stop:
            if s in stringList[i]:
                stringList[i] = stringList[i].replace(s, "")

def word_grams(words, n):
    s = {}
    for k, c in nltk.FreqDist(ngrams(words, n)).items():
        s["".join(k)] = c
    return s

def removeEclipsed(ngramList, n, num, ratio = 0.3):
    myngrams = {}
    for i in range(0, n-2-1):
        for k, v in ngramList[i].items():
            if v > num:
                flag = True
                for j in range(i+1, n-2):
                    for k2, v2 in ngramList[j].items():   
                        if abs(v - v2)/max(v, v2) < ratio  and k in k2:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    myngrams[k] = v
    return myngrams

def getDictionary(path):
    dict = open(path, 'r', encoding = 'utf8').read()
    dict = dict.split('\n')
    mydict = []
    for word in dict:
        if word != '':
            mydict.append(word[0:word.index(' ')])
    return mydict
