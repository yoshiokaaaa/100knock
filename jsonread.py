import json

def jsonread(filename, title):
    readfile = ""
    with open(filename,'rt') as f:
        json_line = f.readlines()
        for lines in json_line:
            json_read = json.loads(lines)
            if json_read['title'] == title:
                    readfile += json_read['text']
    return readfile

uk = open('uk.txt','wt')
uk.write(jsonread('jawiki-country.json',u'イギリス'))
uk.close()
