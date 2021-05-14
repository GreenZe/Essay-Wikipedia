import re
"""
    Duyệt tương tự như category_filter.py để ra kết quả cuối cùng
"""
# # ROUND 1

# link = "D:\\Tieu Luan\\Rinsha\\content.txt"
# count = 0
# f = open("title_round_01.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0:
#         break
#     else:
#         RE_01 = re.findall(r"\'[A-Za-z]*\'\,\s\'title\':\s\'[^:]*", line)
#         if (RE_01 != []):
#             f.write(str(RE_01) + "\n")
#         RE_02 = re.findall(r"\'category\'.*outgoing_link", line)
#         if (RE_02 != []):
#             f.write(str(RE_02) + "\n")


# # ROUND 2

# link = "title_round_01.txt"
# count = 0
# f = open ("title_round_02.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0: break
#     else:
#         RE_01 = re.findall(r"\'title\':\s\'.*\',", line)
#         if (RE_01 != []):
#             f.write (str(RE_01) + "\n")
#
#         RE_02 = re.findall(r"\'category\'.*\']",line)
#         if (RE_02 != []):
#             f.write (str(RE_02) + "\n")


# # ROUND 3

# link = "title_round_02.txt"
# count = 0
# f = open ("title_round_03.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0: break
#     else:
#         RE_01 = re.findall(r"\'title\':\s\'.*\'", line)
#         if (RE_01 != []):
#             f.write (str(RE_01) + "\n")
#
#         RE_02 = re.findall(r"\'category\':\s\[[^]]*]",line)
#         if (RE_02 != []):
#             f.write (str(RE_02) + "\n")

# # ROUND 4

# link = "title_round_03.txt"
# count = 0
# f = open ("title_round_04.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0: break
#     else:
#         RE_01 = re.findall(r":\s[^\"]*", line)
#         f.write (str(RE_01) + "\n")

# # VERSION_05

link = "title_round_04.txt"
count = 0
f = open ("title_round_05.txt", "w", encoding="utf8")
for line in open(link, "r", encoding='utf8'):
    if count < 0: break
    else:
        if not re.match("\[\':\s\[\]\'\]",line):
            RE_01 = re.findall(r"\'.*\'", line)
            f.write (str(RE_01) + "\n")
        else: f.write ("[ ]\n")