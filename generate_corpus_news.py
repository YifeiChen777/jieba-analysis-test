import sys

import jieba
import jieba.analyse
from optparse import OptionParser
import math
import json 

def load_json_news(filename):
    documents = []
    set_word = set()

    f = open(filename,) 
    # data = json.load(f) 
    # contents = data['content']
    with open(filename, 'r') as f:
        flag = 0
        for line in f:
            if flag > 1000:
                break
            flag += 1
            data = json.loads(line)
            jiecut = jieba.lcut(data['content'])
            documents.append(jiecut)
            set_word.update(jiecut)

    total_document = len(documents)
    for word in set_word:
        if word.isspace():
            continue
        count = 0
        for d in documents:
            if word in d:
                count += 1
        idf = math.log(total_document / count)
        print(word + " " + str(idf))


if __name__ == "__main__":
    load_json_news("static/news2016zh_valid.json")
