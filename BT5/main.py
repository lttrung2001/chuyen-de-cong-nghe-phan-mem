from utils.helper import *
import numpy as np
import math

vocab_list = read_vocabs()
doc_dict = read_docs()
query_list = read_queries()

def boolean_vectorize(doc):
    vector = np.array([doc.count(term) / len(doc.split()) if term in doc else 0 for term in vocab_list])
    return vector

# def term_freq_vectorize(docs):
#     res = np.array([[doc.count(term) / len(doc) for term in vocab_list] for doc in docs])
#     return res

def cosine_similarity(x, y):
    return np.dot(x,y) / math.sqrt(np.dot(x,x) * np.dot(y,y))

def calculate_c(doc, query):
    doc_vector = boolean_vectorize(doc)
    query_vector = boolean_vectorize(query)
    p_relevant = cosine_similarity(doc_vector, query_vector)
    p_not_relevant = 1 - p_relevant
    sum_c = 0
    for i in range(len(doc_vector)):
        if (doc_vector[i] != 0 and query_vector[i] != 0):
            term_freq = doc_vector[i]
            pi = term_freq * p_relevant / p_relevant
            not_pi = (1 - term_freq) * p_relevant / p_relevant
            ri = term_freq * p_not_relevant / p_not_relevant
            not_ri = (1 - term_freq) * p_not_relevant / p_not_relevant
            ci = math.log1p(((pi + 0.5) * (not_ri + 0.5)) / ((ri + 0.5) * (not_pi + 0.5)))
            sum_c += ci
    return sum_c


if __name__ == "__main__":
    test_query = query_list[0]
    ranked_list = dict(map(lambda item: (item[0], calculate_c(item[1], test_query)), doc_dict.items()))
    print({k: v for k, v in sorted(ranked_list.items(), key= lambda item: item[1], reverse=True)[:10]})
        


