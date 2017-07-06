'''
Created on Jul 5, 2017

@author: david_000
'''
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font = fm.FontProperties(fname='c:\\windows\\fonts\\kaiu.ttf')

file = "C:\\Users\\david_000\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\jieba\\PTTdictionary.txt"

data = pd.DataFrame(columns=('term', 'n', 'part'))
with open(file, encoding = 'utf8') as f:
    content = f.readlines()
    count = 0
    for row in content:
        row = row.replace("\n", "")
        
        data.loc[count] = np.array(row.split(" "))
        count += 1

data['n'] = pd.to_numeric(data['n'], errors='coerce')
mydata = data.sort(['n', 'term'], ascending = True)
mydata = mydata.loc[mydata['n'] >= 300]

mydata.shape

#mydata = mydata.set_index('term')
p = mydata['n'].plot.barh(rot = 0, fontsize = 10)
p.set_yticklabels(mydata['term'], fontproperties=font, fontsize = 15)
plt.show()






