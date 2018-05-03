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
            print(m.group()[:-1])

# In[]
import re

with open('uk.json','rt') as f:
    jsonuk = f.read()
    m = re.search("{{基礎情報.*(\n.*?)+\n}}",jsonuk)
    if m:
        basic_info = (m.group())
    basic = basic_info.split("|")
    basic_dic = {}
    print(basic[4])
    for i in basic:
        if re.search("=",i):
            basic_key = i.split(" = ")[0]
            basic_value = i.split(" = ")[1].replace("\n","")
            basic_dic.update({basic_key:basic_value})
    print(basic_dic)

# In[]
import re

with open('uk.json','rt') as f:
    jsonuk = f.read()
    m = re.search("{{基礎情報.*(\n.*?)+\n}}",jsonuk)
    if m:
        basic_info = (m.group())
    basic = basic_info.split("|")
    basic_dic = {}
    for i in basic:
        if re.search("\'+",i):
            i = re.sub("\'+","",i)
        if re.search("=",i):
            basic_key = i.split(" = ")[0]
            basic_value = i.split(" = ")[1].replace("\n","")
            basic_dic.update({basic_key:basic_value})
    print(basic_dic)

# In[]
import re

with open('uk.json','rt') as f:
    jsonuk = f.read()
    m = re.search("{{基礎情報.*(\n.*?)+\n}}",jsonuk)
    if m:
        basic_info = (m.group())
    basic = basic_info.split("|")
    basic_dic = {}
    for i in basic:
        i = re.sub("\[+","",i)
        i = re.sub("\]+","",i)
        i = re.sub("\'+","",i)
        if re.search("=",i):
            basic_key = i.split(" = ")[0]
            basic_value = i.split(" = ")[1].replace("\n","")
            basic_dic.update({basic_key:basic_value})
    print(basic_dic)

# In[]
import re

with open('uk.json','rt') as f:
    jsonuk = f.read()
    m = re.search("{{基礎情報.*(\n.*?)+\n}}",jsonuk)
    if m:
        basic_info = (m.group())
    basic = basic_info.split("|")
    basic_dic = {}
    for i in basic:
        i = re.sub("\[+","",i)
        i = re.sub("\]+","",i)
        i = re.sub("\'+","",i)
        i = re.sub("<.*>","",i)
        i = re.sub("\[.*\]","",i)
        if re.search("=",i):
            basic_key = i.split(" = ")[0]
            basic_value = i.split(" = ")[1].replace("\n","")
            basic_dic.update({basic_key:basic_value})
    print(basic_dic)

# In[]
import re
import requests
import json

with open('uk.json','rt') as f:
    jsonuk = f.read()
    m = re.search("{{基礎情報.*(\n.*?)+\n}}",jsonuk)
    if m:
        basic_info = (m.group())
    basic = basic_info.split("|")
    basic_dic = {}
    for i in basic:
        i = re.sub("\[+","",i)
        i = re.sub("\]+","",i)
        i = re.sub("\'+","",i)
        i = re.sub("<.*>","",i)
        i = re.sub("\[.*\]","",i)
        if re.search("=",i):
            basic_key = i.split(" = ")[0]
            basic_value = i.split(" = ")[1].replace("\n","")
            basic_dic.update({basic_key:basic_value})
    url = 'https://www.mediawiki.org/w/api.php'
    payload = {"action": "query",
           "titles": "File:{}".format(basic_dic[u"国旗画像"]),
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}
    json_data = requests.get(url, params=payload).json()
    print(json_data)
    url_flag = json_data["query"]["pages"]["-1"]["imageinfo"]
    print(url_flag[0]["url"])
