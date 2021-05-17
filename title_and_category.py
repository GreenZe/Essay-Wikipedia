import re

link = "input.txt"
count = 0
f = open("title_and_category.txt", "w", encoding="utf8")
for line in open(link, "r", encoding='utf8'):
    if count < 0:
        break
    else:
        RE_01 = re.findall(r"\'title\':\s\'[^\']*\'|\'title\':\s\"[^\"]*\"", line)
        if RE_01 != []:
            f.write(RE_01[0]+"\n")

        RE_02= re.findall(r"\'category\':\s\[[^\[]*\]", line)
        if(RE_02 != []):
            f.write(RE_02[0]+"\n")