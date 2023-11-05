from collections import defaultdict
from math import log
import json

with open('cleared_dataset/inverted_index.json', 'r') as f:
    inverted_index = json.load(f)

def tf_idf(query, inverted_index, total_docs):
    # 计算每个单词的IDF
    idf = {word: log(total_docs / len(docs)) for word, docs in inverted_index.items()}

    # 计算查询中每个单词的TF
    tf = defaultdict(int)
    for word in query:
        tf[word] += 1

    # 计算每个文档的得分
    scores = defaultdict(float)
    for word in query:
        if word in inverted_index:
            for doc in inverted_index[word]:
                scores[doc] += tf[word] * idf[word]

    # 按得分排序
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return sorted_scores


total_docs = len(set(doc for docs in inverted_index.values() for doc in docs))
query = ['中国', '赢得']
print(tf_idf(query, inverted_index, total_docs))