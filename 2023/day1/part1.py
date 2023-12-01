lines = open('./input1.txt', 'r', encoding='utf-8')

int_sum = 0

for line in lines:
	integers = [int(token) for token in line if token.isdigit()]
	if len(integers) == 1:
		integers.append(integers[0])

	if len(integers) < 2:
		print(line.strip())

	line_value = int("{}{}".format(integers[0], integers[-1]))

	int_sum += line_value

print(int_sum)
