
from multiprocessing import Pool
from collections import defaultdict
from itertools import chain
import json

def mapper(document_id, document):
    # generate the key-value pairs
    return [(word, document_id) for word in document]

def reducer(word, document_ids):
    return (word, list(document_ids))

def map_reduce(mapper, reducer, documents):
    # use a Pool to map the mapper function over the documents
    with Pool() as pool:
        pairs = pool.starmap(mapper, documents.items())

    # flatten the list of lists
    pairs = list(chain.from_iterable(pairs))

    # group the pairs by key
    grouped = defaultdict(list)
    for pair in pairs:
        grouped[pair[0]].append(pair[1])

    # use a Pool to map the reducer function over the grouped data
    with Pool() as pool:
        inverted_index = pool.starmap(reducer, grouped.items())

    return dict(inverted_index)

def main():
    with open('cleared_dataset/documents.json', 'r') as f:
        documents = json.load(f)
        f.close()

    inverted_index = map_reduce(mapper, reducer, documents)
    # print(inverted_index)

    with open('cleared_dataset/inverted_index.json', 'w') as f:
        json.dump(inverted_index, f, ensure_ascii=False)
        f.close()
    

if __name__ == '__main__':
    main()