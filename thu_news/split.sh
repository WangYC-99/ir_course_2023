#!/bin/bash

# 假设你的文件名是 file.txt
filename='valid.txt'
# 计数器
count=10403

# 读取文件的每一行
while IFS= read -r line
do
    # 在每个新文件中写入行
    echo "$line" > "../dataset/file$count.txt"
    # 计数器增加
    ((count++))
done < "$filename"