import re

# # # Chạy code của từng VERSION mới ra kết quả nha
#  # VERSION_01

# link = "input.txt"
# count = 0
# f = open("category_Test_01.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0:
#         break
#     else:
#         RE_02 = re.findall(r"\'category\'.*outgoing_link", line)
#         if (RE_02 != []):
#             f.write(str(RE_02) + "\n")

# # VERSION_02

# link = "category_Test_01.txt"
# count = 0
# f = open ("category_Test_02.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0: break
#     else:
#         RE_02 = re.findall(r"\'category\':\s\[[^]]*]",line)
#         if (RE_02 != []):
#             f.write (str(RE_02) + "\n")

# # VERSION_03

# link = "category_Test_02.txt"
# count = 0
# f = open ("category_Test_03.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0: break
#     else:
#         RE_01 = re.findall(r":\s[^\"]*", line)
#         f.write (str(RE_01) + "\n")

# VERSION_04

link = "category_Test_03.txt"
count = 0
f = open ("category_Test_04.txt", "w", encoding="utf8")
for line in open(link, "r", encoding='utf8'):
    if count < 0: break
    else:
        RE_01 = re.findall(r"\'.*\'", line)
        f.write (str(RE_01) + "\n")
