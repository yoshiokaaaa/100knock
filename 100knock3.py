# In[]
import json

def jsonread(filename, title):
    with open(filename,'r') as f:
        json_line = f.readlines()
        for lines in json_line:
            json_read = json.loads(lines)
            if json_read['title'] == title:
                print(json_read['text'])

jsonread('jawiki-country.json','イギリス')

# In[]
import re

with open('uk.txt','rt') as f:
    jsonuk = f.read()
    uktext = jsonuk.split("\n")
    for line in uktext:
        if re.search(r"Category:",line):
            print(line)

# In[]
import re

with open('uk.json','rt') as f:
    jsonuk = f.read()
    uktext = jsonuk.split("\n")
    for line in uktext:
        if re.search(r"Category:",line):
            print(line[11:-2])

import re

with open('uk.json','rt') as f:
    jsonuk = f.read()
    uktext = jsonuk.split("\n")
    for line in uktext:
        if re.search(r"Category:",line):
            print(line.replace(r"Category:","")[2:-2])

# In[]
import re

with open('uk.json','rt') as f:
    section = []
    jsonuk = f.read()
    uktext = jsonuk.split("\n")
    for line in uktext:
        if re.search("==",line):
            section.append(line[1:-1])
    section_dict = {}
    for word in section:
        remove = word.count("=")//2
        section_dict.update({word[remove:-remove]:remove})
    section_dic = sorted(section_dict.items(),key = lambda x: x[1])
    print(dict(section_dic))


# In[]
import re

with open('uk.json','rt') as f:
    jsonuk = f.read()
    uktext = jsonuk.split("\n")
    for line in uktext:
        m = re.search(u"(ファイル|File):(.*?[|])",line)
        if m:
            print(m.group()[5:-1])
