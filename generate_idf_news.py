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
            # if flag > 1000:
            #     break
            # flag += 1
            total_document += 1
            data = json.loads(line)
            jiecut = jieba.lcut(data['content'])
            for each in set(jiecut):
                if each.isspace() or each.isnumeric() or each in string.punctuation:
                    continue
                documents[each] += 1

    for word, count in documents.items():
        idf = math.log(total_document / count)
        print(word + " " + str(idf))


if __name__ == "__main__":
    load_json_news("static/news2016zh_valid.json")
