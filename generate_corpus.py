import sys

import jieba
import jieba.analyse
from optparse import OptionParser
import math

def process_file(filename):
    documents = []
    set_word = set()
    flag = 0
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            flag += 1
            if flag >= 1000:
                break
            sentence = line.rsplit('_!_')
            l = []
            for each in sentence[3:]:
                jiecut = jieba.lcut(each)
                l += jiecut
            documents.append(l)
            set_word.update(l)
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
    process_file("static/toutiao_cat_data.txt")