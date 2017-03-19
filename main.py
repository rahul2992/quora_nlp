import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
import codecs
	

# encoding=utf8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

file = 'train-2.csv'
data = pd.read_csv(file)

#print data.head(20)
negative = data.loc[data['is_duplicate'] == 0]
duplicate = data.loc[data['is_duplicate'] == 1]

q1 = data['question1'].values
q2 = data['question2'].values

q1t, q2t = [], []
#print type(q1[301412])
#print q1[301412].split()
#print nltk.wordpunct_tokenize(q1[301412])

for q in q1:
	if (type(q) != float):
		q = q.lower()
		q_tmp = nltk.wordpunct_tokenize(q)
		q1t.append(q_tmp)


for q in q2:
	if (type(q) != float):
		q = q.lower()
		q_tmp = nltk.wordpunct_tokenize(q)
		q2t.append(q_tmp)


#print data.head(20)

#print 'Negative:', negative.shape
#print 'Duplicate:', duplicate.shape

#Dataset is slightly unbalanced