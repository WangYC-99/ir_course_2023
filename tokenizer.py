import jieba
import json

with open('stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords = [line.strip() for line in f.readlines()]
    f.close()

documents = {}

# for doc_id in range(1, 11804):
for doc_id in range(2, 10):
    # 加载停用词

    with open('dataset/file{}.txt'.format(doc_id - 1), 'r') as f:
        text = f.read()
        f.close()

    # 使用jieba进行分词
    seg_list = jieba.cut(text, cut_all=False)

    # 去除停用词
    filtered_seg_list = [word for word in seg_list if word not in stopwords]

    documents['doc{}'.format(doc_id - 1)] = filtered_seg_list

with open('cleared_dataset/documents_tiny.json', 'w') as f:
    json.dump(documents, f, ensure_ascii=False)
    f.close()