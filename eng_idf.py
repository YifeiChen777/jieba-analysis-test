import nltk
from nltk.corpus import stopwords
from collections import defaultdict
import sys
import os
import math

def small_corpus_idf(directory):
    stop_words = set(stopwords.words('english')) 
    documents = defaultdict(int)
    total_count = 0
    for filename in os.listdir(directory):
        l = []
        dic_file = os.path.join(directory, filename)
        with open(dic_file, "r") as file:
            total_count += 1
            lines = file.readlines()
            word_set = set()
            for line in lines:
                lline = line.strip('\n').split()
                word_set.update(lline)
            for word in set(word_set):
                if not word.isspace() and word not in stop_words:
                    documents[word] += 1

    diction = defaultdict(float)
    for word, count in documents.items():
        idf = math.log(total_count / count)
        # print(word + " " + str(idf))
        diction[word] = idf
    a = sorted(diction.items(), key=lambda x: x[1], reverse=False)
    return [each[0] for each in a[0:25]]

if __name__ == "__main__":
    r = small_corpus_idf("static/small_english")
    print(r)
    print(set(stopwords.words('chinese')) )