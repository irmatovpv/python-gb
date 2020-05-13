from itertools import count
from sys import argv

script_name, start_number, stop= argv

start_number, stop = int(start_number), int(stop)

for el in count(start_number):
    if el > stop:
        break
    else:
        print(el)