import re

# # # Chạy code của từng VERSION mới ra kết quả nha
# # # Version trước là đầu vào của version sau nên phải thực hiện chạy các version theo thứ tự

#  # VERSION_01 : 
#  #  #  input: input.txt
#  #  #  output: category_Test_01.txt

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
#  #  #  input: category_Test_01.txt
#  #  #  output: category_Test_02.txt

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
#  #  #  input: category_Test_02.txt
#  #  #  output: category_Test_03.txt

# link = "category_Test_02.txt"
# count = 0
# f = open ("category_Test_03.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0: break
#     else:
#         RE_01 = re.findall(r":\s[^\"]*", line)
#         f.write (str(RE_01) + "\n")



# VERSION_04
#  #  #  input: category_Test_03.txt
#  #  #  output: category_Test_04.txt

link = "category_Test_03.txt"
count = 0
f = open ("category_Test_04.txt", "w", encoding="utf8")
for line in open(link, "r", encoding='utf8'):
    if count < 0: break
    else:
        RE_01 = re.findall(r"\'.*\'", line)
        f.write (str(RE_01) + "\n")
