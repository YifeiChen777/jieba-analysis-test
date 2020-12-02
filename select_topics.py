import numpy as np
from collections import defaultdict
import os
import jieba
from gensim import models

matrix = np.zeros((365,8))

def extract_idf(filename):
    idf_dict = defaultdict(float)
    index_dict = {}
    i = 0
    with open(filename,"r") as f:
        lines = f.readlines()
        for line in lines:
            word = line.split()[0]
            idf_dict[word] = float(line.split()[1])
            if not word in index_dict:
                index_dict[word] = i
                i += 1
    return idf_dict, index_dict

idf_dict, index_dict = extract_idf("chi_small_idf.txt")

def small_corpus_idf(directory):
    documents = []
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
                tmp = defaultdict(int)
                jiecut = jieba.lcut(line)
                for word in jiecut:
                    if word.isspace() or word.isnumeric() or word in stop_words:
                        continue
                    else:
                        tmp[word] += 1
                documents.append(tmp)
    return documents

documents = small_corpus_idf("static/small_corpus")
corpus_tfidf = []
for i in range(len(documents)):
    document = documents[i]
    total_word = 0
    tmp = []
    for key, value in document.items():
        total_word += value

    for key, value in document.items():
        tf = value / total_word
        tfidf = idf_dict[key] * tf
        matrix[index_dict[key]][i] = tfidf
        tmp.append((index_dict[key], tfidf))
    corpus_tfidf.append(tmp)
dictionary = {y:x for x,y in index_dict.items()}

lda_model_tfidf = models.LdaMulticore(corpus_tfidf, num_topics=5, id2word=dictionary, passes=2, workers=4)
for idx, topic in lda_model_tfidf.print_topics(-1):
    print('Topic: {} Word: {}'.format(idx, topic))


