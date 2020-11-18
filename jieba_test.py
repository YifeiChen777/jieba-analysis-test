import sys

import jieba
import math
import os
import jieba.analyse
from optparse import OptionParser

def small_corpus_idf(directory):
    documents = []
    word_set = set()
    stop_words = []
    with open("stopword.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.rstrip('\n'))
    for filename in os.listdir(directory):
        l = []
        dic_file = os.path.join(directory, filename)
        with open(dic_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                jiecut = jieba.lcut(line)
                l += jiecut
        word_set.update(l)
        documents.append(l)
    total_document = len(documents)
    diction = {}
    for word in word_set:
        if word.isspace() :
            continue
        if word in stop_words:
            continue
        count = 0
        for d in documents:
            if word in d:
                count += 1
        idf = math.log(total_document / count)
        # print(word + " " + str(idf))
        diction[word] = idf
    a = sorted(diction.items(), key=lambda x: x[1], reverse=False)
    return [each[0] for each in a[0:30]]
    # print(a[0:10])


def jieba_analyze(filename):
    USAGE = "usage:    python extract_tags.py [file name] -k [top k]"
    parser = OptionParser(USAGE) #
    parser.add_option("-k", dest="topK")
    # opt, args = parser.parse_args()

    jieba.analyse.set_stop_words("stopword.txt")

    content = open(filename, 'rb').read()
    jieba.analyse.set_idf_path("new_idf.txt")
    tags1 = jieba.analyse.extract_tags(content, topK=5)

    print(",".join(tags1))

if __name__ == "__main__":
    print(" ")
    small = small_corpus_idf("static/small_corpus")
    print(small)
    print(" ")
    print("1: ")
    jieba_analyze("static/Chi/1/1.txt")
    print("2: ")
    jieba_analyze("static/Chi/2/1.txt")
    print("3: ")
    jieba_analyze("static/Chi/3/1.txt")
    print("Common 1: ")
    jieba_analyze("static/Common/1/chi.txt")
    print("Common 2: ")
    jieba_analyze("static/Common/2/chi.txt")
    print("Common 3: ")
    jieba_analyze("static/Common/3/chi.txt")
    print("Common 4: ")
    jieba_analyze("static/Common/4/chi.txt")
    print("Common 5: ")
    jieba_analyze("static/Common/5/chi.txt")

    # with open("toutiao_idf.txt", 'r') as f:
    #     count = 0
    #     for line in f.readlines():
    #         count += 1
    #         print(count)
    #         a,b = line.strip().split(' ')