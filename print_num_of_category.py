# The input code is the category and prints the number of occurrences

import re

list = []
list2 = []
list3 = []

# lấy dữ liệu từ file number_of_category.txt
# đã hoàn thành từ count_category.py
link = "number_of_category.txt"
count = 0

f = open ("category_in_line.txt", "w", encoding="utf8")
for line in open(link, "r", encoding='utf8'):
       list.extend(line.split(", "))
       f.write(str(list) + "\n")
for i in list:
    # Re = re.findall(r'\"\'[^\']*\'\"',i)
    Re = re.findall(r'\"(.*)\"', i)
    Re2 = re.findall(r'(0|[1-9][0-9]*)[^(\s)]*$',i)

    list2.extend(Re)
    list3.extend(Re2)

list3 = list3[::-1]
list2 = list2[::-1]

print(len(list2))
print(len(list3))

print("- Enter any category: ", end='')
check = input()

print("- The number of that category is: ", end='')
for i in range(len(list3)):
    for i in range(len(list2)):
        if check == list2[i]:
            data = list3[i]
print(data)