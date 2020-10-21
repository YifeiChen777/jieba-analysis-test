import sys

import jieba
import jieba.analyse
from optparse import OptionParser

def jieba_analyze(filename):
    USAGE = "usage:    python extract_tags.py [file name] -k [top k]"
    parser = OptionParser(USAGE)
    parser.add_option("-k", dest="topK")
    # opt, args = parser.parse_args()

    content = open(filename, 'rb').read()
    tags = jieba.analyse.extract_tags(content, topK=3)

    print(",".join(tags))

if __name__ == "__main__":
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