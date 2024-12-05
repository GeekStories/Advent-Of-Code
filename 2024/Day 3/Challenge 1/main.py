import re

pattern = r"mul\(\d+,\d+\)"
number_pattern = r"\d+,\d+"

data = open("../memory.txt", "r").read()
match = re.findall(pattern, data)

total = 0
for result in match:
    numbers = re.search(number_pattern, result).group()
    (x, y) = numbers.split(",")
    total += int(x) * int(y)

print(total)
