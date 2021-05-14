
import re

"""
    Chúng ta sẽ run code 4 round để lấy ra được dữ liệu cuối
    cùng chỉ còn lại tất cả các category từ file dữ liệu lớn 
    ban đầu (ở đây là file content.txt, dung lượng: 9.34GB) 
"""
#  # ROUND 1

# link = "D:\\Tieu Luan\\Rinsha\\content.txt"
# count = 0
# f = open("category_round_01.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0:
#         break
#     else:
#         RE_02 = re.findall(r"\'category\'.*outgoing_link", line)
#         if (RE_02 != []):
#             f.write(str(RE_02) + "\n")

# # ROUND 2

# link = "category_round_01.txt"
# count = 0
# f = open ("category_round_02.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0: break
#     else:
#         RE_02 = re.findall(r"\'category\':\s\[[^]]*]",line)
#         if (RE_02 != []):
#             f.write (str(RE_02) + "\n")

# # ROUND 3

# link = "category_round_02.txt"
# count = 0
# f = open ("category_round_03.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0: break
#     else:
#         RE_01 = re.findall(r":\s[^\"]*", line)
#         f.write (str(RE_01) + "\n")

# # ROUND 4
# file category - finish

link = "category_round_03.txt"
count = 0
f = open ("category_round_04.txt", "w", encoding="utf8")
for line in open(link, "r", encoding='utf8'):
    if count < 0: break
    else:
        RE_01 = re.findall(r"\'.*\'", line)
        f.write (str(RE_01) + "\n")
