
# Category của từng bài
# Số lượng bài viết là 197800
import re

link = "input.txt"
count = 0
temp = 0
f = open("category.txt", "w", encoding="utf8")
for line in open(link, "r", encoding='utf8'):
    temp+=1
    if count < 0:
        break
    else:
        RE_01 = re.findall(r"\'category\':\s\[[^\[]*\]", line)
        if(RE_01 != []):
            RE_02 = re.findall(r"\[[^[\]]*]",str(RE_01))
            if(RE_02 != []):
                RE_03 = re.findall(r"[\'\"][^[\]]*[\'\"]",str(RE_02))
                f.write(str(RE_03)+"\n")
