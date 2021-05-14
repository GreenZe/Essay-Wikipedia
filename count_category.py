import collections
import re

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
def num_of_category(data,text):

    # mở một file ghi lại số lần xuất hiện của từng category
    f = open ("number_of_category.txt", "w", encoding="utf8")

    c = collections.Counter(data) #đếm category bằng Counter()

    f.write(str(c))#ghi dữ liệu

    print("- The number of that category is: ", c[text])


if __name__ == "__main__":
    link = "category_round_04.txt" # dữ liệu cuối cùng từ file category_filter.py
    data = data_analysis_input(link)
    print("- Enter any category: ", end='')
    num_of_category(data,text = input())
    
    
