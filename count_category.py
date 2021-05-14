import re
from typing import Counter

link = "category_round_04.txt" # dữ liệu cuối cùng từ file category_filter.py

count = 0
list = []

# tạo một file ghi lại số lượng category
f = open ("number_of_category.txt", "w", encoding="utf8")

for line in open(link, "r", encoding='utf8'):
    if count < 0: break
    else:
        RE = re.findall(r"\[\"(.*)\"]",line)
        list.extend(RE)
        count += 1


data = []

for i in list:
   data.extend(i.split(', '))

print(len(data))

# ghi kết quả đếm được vào file number_of_category.txt
f.write (str(Counter(data)) + "\n")