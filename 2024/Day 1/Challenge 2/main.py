left_values = []
right_values = []
similarity = 0


def find_count(target, list):
    count = 0
    for value in list:
        if value == target:
            count += 1
    return count


for line in open("../../Day 2/location_ids.txt", "r").read().splitlines():
    (left, right) = line.split("   ")
    left_values.append(int(left))
    right_values.append(int(right))

for index, left_value in enumerate(left_values):
    similarity += left_value * find_count(left_value, right_values)


print(similarity)
