### Tạo bộ dữ liệu bao gồm title và category

import re

#  # VERSION_01

# link = "input.txt"
# count = 0
# f = open("output_01.txt", "w", encoding="utf8")
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


# # VERSION_02

# link = "output_01.txt"
# count = 0
# f = open ("output_02.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0: break
#     else:
#         RE_01 = re.findall(r"\'title\':\s\'.*\',", line)
#         if (RE_01 != []):
#             f.write (str(RE_01) + "\n")

#         RE_02 = re.findall(r"\'category\'.*\']",line)
#         if (RE_02 != []):
#             f.write (str(RE_02) + "\n")


# # VERSION_03

# link = "output_02.txt"
# count = 0
# f = open ("output_03_perfect01.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0: break
#     else:
#         RE_01 = re.findall(r"\'title\':\s\'.*\'", line)
#         if (RE_01 != []):
#             f.write (str(RE_01) + "\n")
        
#         RE_02 = re.findall(r"\'category\':\s\[[^]]*]",line)
#         if (RE_02 != []):
#             f.write (str(RE_02) + "\n")

#  # VERSION_04

# link = "output_03_perfect01.txt"
# count = 0
# f = open ("output_04.txt", "w", encoding="utf8")
# for line in open(link, "r", encoding='utf8'):
#     if count < 0: break
#     else:
#         RE_01 = re.findall(r":\s[^\"]*", line)
#         f.write (str(RE_01) + "\n")

 # VERSION_05

link = "output_04.txt"
count = 0
f = open ("output_05_perfect02.txt", "w", encoding="utf8")
for line in open(link, "r", encoding='utf8'):
    if count < 0: break
    else:
        if not re.match("\[\':\s\[\]\'\]",line):
            RE_01 = re.findall(r"\'.*\'", line)
            f.write (str(RE_01) + "\n")
        else: f.write ("[ ]\n")