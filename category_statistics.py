
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

for i in list:
    Re = re.findall(r'(0|[1-9][0-9]*)[^(\s)]*$',i)

    list2.extend(Re)

# print(list2)

# convert list string to list int
for i in range(0, len(list2)):
    list2[i] = int(list2[i])

f.write(str(list2) + "\n")

print("- Enter a any number: ", end='')
count = 0
k = input()
k = int(k)

for i in list2:
    if i > k:
        count = count + 1

# printing the intersection
print("-> The number of categories greater than %2d is: "%(k) + str(count))

