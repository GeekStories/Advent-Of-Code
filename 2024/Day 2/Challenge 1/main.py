safe_count = 0
values = []


def check_safe(line_values):
    increased = False
    decreased = False

    for i in range(len(line_values)):
        if i == len(line_values) - 1:
            break

        difference = line_values[i] - line_values[i + 1]

        if difference == 0:
            return False

        if abs(difference) > 3:
            return False

        if difference > 0:
            increased = True

        if difference < 0:
            decreased = True

        if increased and decreased:
            return False

    return True


for line in open("../reports.txt", "r").read().splitlines():
    values.append([int(value) for value in line.split(" ")])

for line in values:  # [1, 2, 3, 4, 7]
    if check_safe(line):
        safe_count += 1

print(f"{safe_count} / {len(values)}")
