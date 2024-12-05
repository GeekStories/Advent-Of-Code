import re

pattern = r"(?:mul\(\d+,\d+\)|do\(\)|don't\(\))"
number_pattern = r"\d+,\d+"

should_mul = True
total = 0

data = open("../memory.txt", "r").read()
match = re.findall(pattern, data)

for result in match:
    if result == "do()":
        should_mul = True
        continue

    if result == "don't()":
        should_mul = False
        continue

    if should_mul:
        numbers = re.search(number_pattern, result).group()
        (x, y) = numbers.split(",")
        total += int(x) * int(y)

print(total)
