# ir_course 2023 Autuam
> by WangYC
>  @ Gaoling School, Renmin University of China

## Usage
split raw train&val&test set to docs
```
cd thu_news
bash split.sh
```
tokenize and remove stopwords to build a doc list:
```
python tokenizer.py
```
using map-reduce method to convert a inverted_index:
```
python mapreduce.py
```
using TD-IDF method to rank the docs by relevance:
```
python relevance_rank.py
```

## dataset
from https://aistudio.baidu.com/datasetdetail/16287
```
cd dataset
ls -l | grep "^-" | wc -l
```
check the quantity of files
```
>>> 11803
```