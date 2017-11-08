
# coding: utf-8

# In[3]:

a = "stressed"
a[::-1]


# In[4]:

vehicle = "パタトクカシーー"
vehicle[::2]


# In[11]:

patroll = "パトカー"
taxi = "タクシー"
s = "".join(i + j for i,j in zip(patroll,taxi))
s


# In[21]:

circle = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
circle_per = [len(i.strip(",.")) for i in circle.split()]
print(circle_per)


# In[2]:

atom = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
atom_list = atom.strip(",.").split()
atom_list
dict = {}
for (i, word) in enumerate(atom_list,1):
        if i in (1,5,6,7,8,9,15,16,19):
            dict.update({word[0]:i})
        else:
            dict.update({word[:2]:i})
print(dict)



# In[42]:

def ngram(x,n):
    return {tuple(x[i:i+n]) for i in range(len(x)-n+1)}


s = "I am an NLPer"
print(ngram(s,2))
print(ngram([t.strip(",.") for t in s.split()],2))


# In[45]:

X = ngram("paraparaparaside",2)
Y = ngram("pargrapgh",2)
print(X|Y)
print(X&Y)
print(X-Y)
print(Y-X)
c = "se"
if ngram(c,2) <= X:
    print("'se' is included in X")

if ngram(c,2) <=Y:
    print("'se' is included in Y")



# In[46]:

def ifab(x,y,z):
    return "%s時の%sは%s" %(x,y,z)

ifab(12,"気温",22.4)


# In[6]:

import re
def cipher(str):
    unk = ""
    for char in str:
        if 97 <= ord(char) <=123:
            unk += chr(219-ord(char))
        else:
            unk += char
    return unk

print(cipher(atom))
print()
print(cipher('Machine Learning'))



# In[ ]:
import random
typ = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
def typlo(s):
    s_random = []
    s_list = s.split()
    for word in s_list:
        if len(word) > 4:
            mid = list(word[1:-1])
            random.shuffle(mid)
            mid_word = "".join(mid)
            new_word = word[0] + mid_word + word[-1]
            s_random.append(new_word)
        else:
            s_random.append(word)
    return " ".join(s_random)

print(typlo(typ))

# In[]:
with open('hightemp.txt','r') as hightemp:
    line = len(hightemp.readlines())
print(line)

# In[]
with open('hightemp.txt','r') as hightemp:
    space = hightemp.read()
print(space)
print(space.replace("\t"," "))

# In[]
with open('hightemp.txt','r') as hightemp:
    col1 = open('col1.txt','w')
    col2 = open('col2.txt','w')
    for line in hightemp:
        col1.write(line.split()[0]+'\n')
        col2.write(line.split()[1]+'\n')
    col1.close()
    col2.close()

text = "My Name is Ryuya Yoshioka"
print(text[0])
print(text.split()[1])

# In[]
with open('col1.txt','r') as c1:
    col1 = c1.read()
    with open('col2.txt','r')as c2:
        col2 = c2.read()
        coladd = open('col_add.txt','w')
        print(col1)
        print(col2)
        coladd.write("\n".join(i+'\t'+j for i,j in zip(col1.split(),col2.split())))
        coladd.close()

# In[]
import sys

with open('hightemp.txt','r') as f:
    hightemp = f.read()
print(hightemp)
def Nline(s,n):
    s_line = s.split('\n')
    s_get = s_line[:n]
    return "\n".join(s_get)

print(Nline(hightemp,3))

# In[]
with open('hightemp.txt','r') as f:
    hightemp = f.read()
print(hightemp)
def Nline_reverse(s,n):
    s_line = s.split('\n')
    s_get = s_line[-n-1:]
    return "\n".join(s_get)

print(Nline_reverse(hightemp,6))

# In[]
import math

with open('hightemp.txt','r') as f:
    hightemp = f.read()
def Nsplit(s,n):
    s_line = s.split('\n')
    split_a = (len(s_line) - 1)%n
    split_b = len(s_line)//n
    b = [" ".join(s_line[i:i + split_b + 1]) for i in range(0,split_a * split_b - 1 ,split_b)]
    c = [" ".join(s_line[i:i + split_b]) for i in range(split_a * (split_b + 1) ,(len(s_line) - 1),split_b)]
    b_list = "\n".join(b)
    c_list = "\n".join(c)
    return b_list + "\n" + c_list



print(Nsplit(hightemp,7))

import math

a = [1,2,3,4,5,6,7,8,9,10]
def list_split(l,n):
    num = math.floor(len(l)/n)
    numb = len(l) % n
    b = [l[i:i + num + 1] for i in range(0,numb * num,num)]
    c = [l[i:i + num] for i in range(numb * (num + 1) ,len(l),num)]
    b.append(c)
    return b

print(list_split(a,4))

# In[]
with open('hightemp.txt','r') as f:
    hightemp = f.read()
    lines = hightemp.split("\n")
    col1 = []
    for line in lines:
        col1.append(line.split("\t")[0])
    col = set(col1)
    print(col)

with open('hightemp.txt','r') as f:
    hightemp = f.read()
    lines = hightemp.split("\n")
    for line in lines:
        col =  line.split("\t")[0]
    col1 = list(col)
    print(col1)
    print(col)
# In[]
with open('hightemp.txt','r') as f:
    hightemp = f.read()
    lines = hightemp.split("\n")
    col = []
    for line in lines:
        i = line.split("\t")
        col.append(i)
    del col[-1]
    col.sort(key=lambda x:x[3])
    print(col)
    a = []
    for i in col:
        k = " ".join(i)
        a.append(k)
    print(a)
    print("\n".join(a))

# In[]
with open('hightemp.txt','r') as f:
    hightemp = f.read()
    lines = hightemp.split("\n")
    col = []
    for line in lines:
        col.append(line.split("\t")[0])
    col_word = {word:col.count(word) for word in col}
    col_dic =  sorted(col_word.items(),key=lambda x: x[1],reverse = True)
    print(dict(col_dic))
