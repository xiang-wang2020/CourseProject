import pandas as pd 
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_data():
    pass
    # l = []
    # for i in range(1,1000):
    #     my_file = open('faculty/'+str(i*10)+'.txt', "r")
    #     l.append(my_file.read())
    # print(l[5])

    # for i in range(len(l)):
    #     l[i] = l[i] + '\n'
    # file1 = open('faculties.txt', 'w') 
    # file1.writelines(l) 
    # file1.close() 

def clean(l):
    lowered = []
    for i in l:
        i = i.lower()
        lowered.append(i)

    no_punctuations = []
    for i in lowered:
        i = i.translate(str.maketrans('', '', string.punctuation))
        no_punctuations.append(i)
    tokenized = []
    for i in no_punctuations:
        i = i.split(' ')
        tokenized.append(i)
    return tokenized

def get_corpus(good_keywords = None, bad_keywords = None):
    l = []
    file1 = open('faculties.txt', 'r') 
    l = file1.readlines()
    cleaned = clean(l)
    # print(len(cleaned))
    if good_keywords != None:
        good_keywords = good_keywords.lower().split()
    if bad_keywords != None:
        bad_keywords = bad_keywords.lower().split()

    if (good_keywords != None and len(good_keywords) != 0) and (bad_keywords != None and len(bad_keywords) != 0):
        temp = []
        for i in range(len(cleaned)):
            red = True
            for j in bad_keywords:
                if j in cleaned[i]:
                    red = False
                    break
            if red == False:
                continue
            for j in good_keywords:
                if j in cleaned[i]:
                    temp.append(l[i])
        l = temp
    elif good_keywords != None and len(good_keywords) != 0:
        temp = []
        for i in range(len(cleaned)):
            for j in good_keywords:
                if j in cleaned[i]:
                    temp.append(l[i])
        l = temp
    elif bad_keywords != None and len(bad_keywords) != 0:
        temp = []
        for i in range(len(cleaned)):
            for j in bad_keywords:
                if j in cleaned[i]:
                    continue
                else:
                    temp.append(l[i])
        l = temp
    if len(l) == 0:
        return None, None, None
    vector = TfidfVectorizer(stop_words='english', lowercase=True, token_pattern="(?u)\\b\\w\\w+\\b")
    base = vector.fit_transform(l) 
    return l, vector, base

def analysis_data(l, vector, base, query, length):
    search = vector.transform(query)
    cosine_distance = cosine_similarity(search, base)
    similarity_list = cosine_distance[0]
    res = sorted(range(len(similarity_list)), key=lambda i: similarity_list[i], reverse=True)[-length:]
    return res

#  testing
# l, vector, base = get_corpus(None, bad_keywords = "graph")
# query = ['architecture','Computer']
# res = analysis_data(l, vector, base, query, 5)
# print(len(res))
# for i in res:
#     print(l[i][:50])

