import math
import operator

# calculate probability of a term in a document
# Tính xác suất của từ trong tài liệu 
def p_td(term_freq, doc_length, avg_doc_length, corpus_size, doc_freq):
    return ((term_freq + (0.5 * doc_freq)) / (doc_length + (0.5 * corpus_size))) / ((1 - 0.5) + (0.5 * (doc_length / avg_doc_length)))

# Tính xác suất của từ trong câu truy vấn (số lần xuất hiện / tổng từ trong câu truy vấn)
def p_tq(term_freq, query_length):
    return (term_freq / query_length)

# calculate document score
def score(doc, query, doc_length, avg_doc_length, corpus_size, doc_freq):
    score = 1
    for term, qtf in query.items():
        if term in doc:
            ptd = p_td(doc[term], doc_length, avg_doc_length, corpus_size, doc_freq.get(term, 0))
            ptq = p_tq(qtf, len(query))
            score *= math.pow(ptd, ptq) * math.pow((1 - ptd), (1 - ptq))
    return score

# rank documents using PRP and BIM
def prp_bim_ranking(corpus, query, avg_doc_length):
    scores = {}
    doc_freq = {}
    corpus_size = len(corpus)
    # query_length = len(query)
    for doc_id, doc in corpus.items():
        doc_length = sum(doc.values())
        s = score(doc, query, doc_length, avg_doc_length, corpus_size, doc_freq)
        scores[doc_id] = s
        for term in doc:
            doc_freq[term] = doc_freq.get(term, 0) + 1
    ranked_docs = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    return ranked_docs

# example usage

from utils.helper import *
doc_dict = read_docs()
query_list = read_queries()

def map_term_count(doc_content):
    result = {}
    # doc_length = len(doc_content)
    for word in doc_content.split():
        if word not in result:
            result[word] = doc_content.count(word)
    return result
    

corpus = dict(map(lambda item: (item[0], map_term_count(item[1])), doc_dict.items()))
query_list = list(map(map_term_count, query_list))
avg_doc_length = 3

for query in query_list:
    ranked_docs = prp_bim_ranking(corpus, query, avg_doc_length)
    # print(ranked_docs)
    # print("==============")
    # break