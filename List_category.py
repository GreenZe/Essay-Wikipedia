# Đưa từng dòng thành dạng danh sách các category
import re

link = "category_Test_04.txt"

count = 0
list = []
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