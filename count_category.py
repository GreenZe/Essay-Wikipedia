import collections
import re
category = []

def data_analysis_input(link):
    count = 0
    data = []

    for line in open(link, "r", encoding='utf8'):
        if count < 0: break
        else:
            RE = re.findall(r"\'[^\']*\'",line)
            data.extend(RE)
            count += 1

    return data


# # ghi kết quả đếm được vào file number_of_category.txt
def num_of_category(data):

    # mở một file ghi lại số lần xuất hiện của từng category
    f = open ("number_of_category.txt", "w", encoding="utf8")

    c = collections.Counter(data) #đếm category bằng Counter()

    f.write(str(c))#ghi dữ liệu

    return c

def category_statistic(c,k):
    count = 0
    for i in c.items():#Lấy từng category và số lần xuất hiện của nó
        if int(i[1]) > k:# i[1] là số lần xuất hiện
            count += 1
            category.append(i[0]) # i[0] là category
    return count

if __name__ == "__main__":

    link = "category_round_04.txt" # dữ liệu cuối cùng từ file category_filter.py
    data = data_analysis_input(link)
    c = num_of_category(data)

    #input:category
    #output:Số lần xuất hiện của category đó
    print("- Enter any category: ", end='')
    text = input() # Nhập category có cấu trúc : '<category>'
    print("- The number of that category is: ", c[text],"\n")


    print("- Enter a any number: ", end='')
    k =input()
    print("-> The number of categories greater than %2d is: "%(k) + category_statistic(c,int(k)),"\n")

    #Các category có ít nhất k lần xuất hiện là:
    print("Các category có ít nhất k lần xuất hiện là: ",category)

    
