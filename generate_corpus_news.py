import sys

import jieba
import jieba.analyse
from optparse import OptionParser
from collections import defaultdict
import math
import json 

def load_json_news(filename):
    documents = defaultdict(int)
    total_document = 0

    f = open(filename,) 
    with open(filename, 'r') as f:
        flag = 0
        for line in f:
            if flag > 1000:
                break
            flag += 1
            data = json.loads(line)
            jiecut = jieba.lcut(data['content'])
            for each in jiecut:
                if each.isspace():
                    continue
                total_document += 1
                documents[each] += 1

    for key, value in documents.items():
        idf = math.log(total_document / count)
        print(key + " " + str(idf))


if __name__ == "__main__":
    load_json_news("static/news2016zh_valid.json")
