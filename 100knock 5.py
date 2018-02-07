
# coding: utf-8

# In[2]:

import CaboCha
import pydotplus
import subprocess


# In[3]:

def cabocha_analyze(input_file,output_file):
    c = CaboCha.Parser()
    with open(input_file,'r') as inputfile:
        with open(output_file,'wt',encoding='utf-8') as outputfile:
            for line in inputfile:
                tree = c.parse(line.strip())
                outputfile.write(tree.toString(CaboCha.FORMAT_LATTICE))

cabocha_analyze('neco.txt', 'neco.txt.cabocha')


# In[4]:

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    
    def is_end_of_sentence(self):
        return self.pos1 == '句点'
    
    def __str__(self):
        return 'surface: {}, base: {}, pos: {}, pos1: {}'.format(self.surface, self.base, self.pos, self.pos1)


# In[5]:

def cabocha_dic(analyzed):
    with open(analyzed,'r') as cabocha_analyzed:
        cabocha_a = cabocha_analyzed.read()
        words = []
        sentence = []
        morphs = []
        cabocha = cabocha_a.split('\n')
        del cabocha[-1]
        for line in cabocha:
            i = line.split()
            if i[0] == '*' or i[0] == 'EOS':
                pass
            else:
                words.append(i)
        for k in words:
            m = k[1].split(',')
            if len(m) < 7:
                del m
            else:
                _morph = Morph(surface = k[0],base = m[6], pos = m[0],pos1 = m[1])
                sentence.append(_morph) 
        print(sentence[:10])
    return morphs
    
necocabocha =  cabocha_dic('neco.txt.cabocha')
print(str(necocabocha[1]))
for morph in necocabocha[1]:
    print(str(morph))


# In[ ]:

if _morph.is_end_of_sentence:
    morphs.append(sentence)
    sentence = []

