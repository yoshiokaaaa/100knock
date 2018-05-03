
# coding: utf-8

# In[1]:

import CaboCha
import pydotplus
import subprocess


# In[2]:

def cabocha_analyze(input_file,output_file):
    c = CaboCha.Parser()
    with open(input_file,'r') as inputfile:
        with open(output_file,'wt',encoding='utf-8') as outputfile:
            for line in inputfile:
                tree = c.parse(line.strip())
                outputfile.write(tree.toString(CaboCha.FORMAT_LATTICE))

cabocha_analyze('neco.txt', 'neco.txt.cabocha')


# In[3]:

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


# In[4]:

unko = Morph(surface='unko', base=1, pos=2, pos1='句点')
unko.is_end_of_sentence()


# In[5]:

def cabocha_list(analyzed):
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
                pass
            else:
                _morph = Morph(surface=k[0], base=m[6], pos=m[0], pos1=m[1])
                sentence.append(_morph) 
                if _morph.is_end_of_sentence():
                    morphs.append(sentence)
                    sentence = []
        print(words[:40])
    return morphs
    
necocabocha =  cabocha_list('neco.txt.cabocha')
for morph in necocabocha[2]:
    print(str(morph))


# In[6]:

class Chunk:
    def __init__(self,morphs:list,dst:str,srcs:list):
        self.morphs = morphs
        self.dst = int(dst)
        self.srcs = srcs
        
    def endofsentence(self):
        return self.dst == '-1'
    
    def __str__(self):
        return '{}\tsrcs{}\tdst[{}]'.format(self.morphs, self.srcs, self.dst)
    
    def relations(self):
        sent_relation = ''
        
    


# In[7]:

def cabocha_chunk(analyzed):
    with open(analyzed,'r') as cabocha_analyzed:
        cabocha_a = cabocha_analyzed.read()
        cabocha = cabocha_a.split('\n')
        chunk = []
        phrase= ''
        phrases = []
        chunks = []
        sentence = []
        sentences = []
        del cabocha[-1]
        for line in cabocha:
            i = line.split()
            if i[0] == '*':
                chunk.append(i[1])
                chunk.append(i[2].replace('D',''))
                chunks.append(chunk)
                chunk = []
                phrases.append(phrase)
                phrase = ''
            else:
                if i[0] != 'EOS':
                    phrase += i[0]
        del phrases[0]
        chun = chunks[:50]
        phr = phrases[:50]
        for a,b in zip(chunks,phrases):
            zipped = [a,b,[]]
            sentence.append(zipped)
            if a[0] == '0':
                sentence.remove(zipped)
                sentences.append(sentence)
                sentence = []
                sentence.append(zipped)
        del sentences[0]
        ch_sent = []
        ch_sents = []
        for k in sentences:
            for m in k:
                if m[0][1] == '-1':
                    pass
                else:
                    num = int(m[0][1])
                    num2 = int(m[0][0])
                    k[num][2].append(num2)
                _chunk = Chunk(morphs=m[1],dst=m[0][1],srcs=m[2])
                ch_sent.append(_chunk)
            ch_sents.append(ch_sent)
            ch_sent = []
        return ch_sents
                

chunked_file = cabocha_chunk('neco.txt.cabocha')
for morph in chunked_file[100]:
    print(str(morph))


# In[8]:

def relations_chunk(analyzed):
    with open(analyzed,'r') as cabocha_analyzed:
        cabocha_a = cabocha_analyzed.read()
        cabocha = cabocha_a.split('\n')
        chunk = []
        phrase= ''
        phrases = []
        chunks = []
        sentence = []
        sentences = []
        del cabocha[-1]
        for line in cabocha:
            i = line.split()
            if i[0] == '*':
                chunk.append(i[1])
                chunk.append(i[2].replace('D',''))
                chunks.append(chunk)
                chunk = []
                phrases.append(phrase)
                phrase = ''
            else:
                if i[0] == 'EOS':
                    pass
                else:
                    if len(i) > 1 and i[1].split(',')[0] == '記号':
                        pass
                    else:
                        phrase += i[0]
        del phrases[0]
        chun = chunks[:50]
        phr = phrases[:50]
        for a,b in zip(chunks,phrases):
            zipped = [a,b,[]]
            sentence.append(zipped)
            if a[0] == '0':
                sentence.remove(zipped)
                sentences.append(sentence)
                sentence = []
                sentence.append(zipped)
        del sentences[0]
        relation = []
        relations = []
        for k in sentences:
            for m in k:
                if m[0][1] == '-1':
                    pass
                else:
                    num = int(m[0][1])
                    num2 = int(m[0][0])
                    relation_phrases = m[1] + ' ' + k[num][1]
                    k[num][2].append(num2)
                    relation.append(relation_phrases)
            relations.append(relation)
            relation = []
        del relations[0]
        return relations
                

relations_file = relations_chunk('neco.txt.cabocha')
for i in relations_file[3]:
    print(i)


# In[ ]:



