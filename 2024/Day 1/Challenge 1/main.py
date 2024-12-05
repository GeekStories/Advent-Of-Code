left_values = []
right_values = []
difference = 0

for line in open("../location_ids.txt", "r").read().splitlines():
    (left, right) = line.split("   ")
    left_values.append(int(left))
    right_values.append(int(right))

left_values.sort()
right_values.sort()

for index, left_value in enumerate(left_values):
    difference += abs(left_value - right_values[index])

print(difference)
