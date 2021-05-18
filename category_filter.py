import re

link = "input.txt"
count = 0
temp = 0
data_category = []
f = open("category.txt", "w", encoding="utf8")
for line in open(link, "r", encoding='utf8'):
    if count < 0:
        break
    else:
        # Thực hiện lấy list category của từng bài viết
        RE_01 = re.findall(r"\'category\':\s\[[^\[]*\]", line)

        if(RE_01 != []):
            f.write(RE_01[0]+"\n") # ghi dữ liệu vào file category.txt

            # Lấy từng category của mỗi bài đưa vào data_category[] để tiếp tục xử lý
            RE_02 = re.findall(r"\'[^\']*\'",RE_01[0])
            if(RE_02 != []):
                for i in range(1,len(RE_02)):
                    data_category.append(RE_02[i])