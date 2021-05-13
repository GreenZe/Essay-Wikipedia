# The input code is the category and prints the number of occurrence

import re

list = []
list2 = []
list3 = []

link = "num_cate_test.txt"
count = 0

for line in open(link, "r", encoding='utf8'):
       list.extend(line.split(", "))

for i in list:
    Re = re.findall(r'\"(.*)\"',i)
    Re2 = re.findall(r'\: (.*)',i)
    list2.extend(Re)
    list3.extend(Re2)

list3 = list3[::-1]
list2 = list2[::-1]

print("- Enter any category: ", end='')
check = input()

print("- The number of that category is: ", end='')
for i in range(len(list3)):
    for i in range(len(list2)):
        if check == list2[i]:
            data = list3[i]
print(data)
