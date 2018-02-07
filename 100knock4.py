
# coding: utf-8

# In[2]:

import sys
import MeCab
mecab = MeCab.Tagger("-Ochasen")
node = mecab.parse("すもももももももものうち")
print(node)


# In[3]:

import sys
import MeCab

necofile = 'neco.txt'
necofile_parse = 'neco.txt.mecab'

def parse_neco(basetext,outtext):
    mecab = MeCab.Tagger('-Ochasen')
    with open(basetext,'r') as readfile:
        with open(outtext,'w') as outfile:
            outfile.write(mecab.parse(readfile.read()))

neco_mecab = parse_neco(necofile,necofile_parse)
print(neco_mecab)


# In[4]:

def to_dict(tabbed):
    words = tabbed.split('\n')
    sentence = []
    keitaiso = []
    keitaiso_line = []
    keitaiso_result = []
    for lines in words:
        line = lines.split('\t')
        keitaiso_line.append(line)
        if len(line) >=2:
            result = line[3].split('-')
            keitaiso_result.append(result)
            if len(result) >=2:
                gyo = {
                    'surface':line[0],
                    'base':line[2],
                    'pos':result[0],
                    'pos1':result[1]
                }
            else:
                gyo = {
                    'surface':line[0],
                    'base':line[1],
                    'pos':result[0],
                    'pos1':''
                }
            keitaiso.append(gyo)
            if gyo['pos1'] == '句点':
                sentence.append(keitaiso)
                keitaiso = []
    print(keitaiso_line[:100])
    return sentence

with open('neco.txt.mecab','r') as necome:
    neco_dict = to_dict(necome.read())
    print(neco_dict[:100])


# In[5]:

verb = []
for i in neco_dict:
    for k in i:
        if k['pos'] == '動詞':
            verb.append(k['surface'])
print(verb)


# In[6]:

verb_base = []
for i in neco_dict:
    for k in i:
        if k['pos'] == '動詞':
            verb_base.append(k['base'])
print(verb_base)


# In[7]:

sahen = []
for i in neco_dict:
    for k in i:
        if k['base'] != '——':   
            if k['pos'] == '名詞' and k['pos1'] == 'サ変接続':
                sahen.append(k['surface'])
print(sahen)


# In[8]:

phrase = []
for i in neco_dict:
    for k in range(len(i)):
        if i[k]['surface'] == 'の' and i[k-1]['pos'] == '名詞' and i[k+1]['pos'] == '名詞':
            phrase.append(i[k-1]['surface'] + i[k]['surface'] + i [k+1]['surface'])
print(phrase)


# In[9]:

nouns = []
for i in neco_dict:
    for k in range(len(i)):
        if i[k]['pos'] == '名詞' and i[k+1]['pos'] == '名詞':
            nouns.append(i[k]['surface'] + i[k+1]['surface'])
print(nouns)


# In[10]:

count_dic = {}
for i in neco_dict:
    for k in i:
        if k['surface'] not in count_dic:
            count_dic.update({k['surface']:1})
        if k['surface'] in count_dic:
            count_dic[k['surface']] += 1
count_dic = [(k, v) for k, v in sorted(count_dic.items(), key=lambda x: x[1], reverse=True)]
print(count_dic)



# In[20]:

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
ten = count_dic[:10]
print(ten)
words = []
for i in ten:
    words.append(i[0])
    xrange = len(words)
topten = ten.zip()
print(words)


# In[ ]:


