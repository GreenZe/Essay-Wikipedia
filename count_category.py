import collections
from category_filter import data_category

category = []

# # ghi kết quả đếm được vào file number_of_category.txt
def num_of_category(data):

    # mở một file ghi lại số lần xuất hiện của từng category
    f = open ("number_of_category.txt", "w", encoding="utf8")

    c = collections.Counter(data) #đếm category bằng Counter()

    f.write(str(c))#ghi dữ liệu

    return c

# Thống kê các category
# Số lượng category xuất hiện ít nhất k lần.
def category_statistic(c,k):
    count = 0
    for i in c.items():#Lấy từng category và số lần xuất hiện của nó
        if int(i[1]) > k:# i[1] là số lần xuất hiện
            count += 1
            category.append(i[0]) # i[0] là category
    return count


if __name__ == "__main__":

    link = "category.txt" # dữ liệu cuối cùng từ file category_filter.py
    # data = data_analysis_input(link)
    

    c = num_of_category(data_category) # data_category[] được import từ category_filter


    #input:category
    #output:Số lần xuất hiện của category đó
    print("- Enter any category: ", end='')
    text = input() # Nhập category có cấu trúc : '<category>'
    print("- The number of that category is: ", c[text],"\n")



    print("- Enter a any number: ", end='')
    k =int(input())
    print("-> The number of categories greater than k times is: ", category_statistic(c,k),"\n")


    #Các category có ít nhất k lần xuất hiện được ghi vào num_of_greater_.txt
    fo = open ("num_of_category_greater_.txt", "w", encoding="utf8")
    for i in category:
        fo.write(str(i) + "\n")

    
 