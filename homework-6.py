import re
out_dict = {}
with open("h6.txt", "r") as inp:
    for line in inp:
        subj, nums = line.split(":")
        data = nums.strip().split(" ")

        out_dict[subj.strip()] = sum([int(num) for num in map(lambda x: (re.sub('[^0-9]','', x)), data) if num])

print(out_dict)