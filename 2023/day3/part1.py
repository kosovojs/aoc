import re

input = open('./input1.txt', 'r', encoding='utf-8').read()

id_sum = 0


def prepare_input(input):
	return [[char for char in f.strip()] for f in input.split('\n') if len(f)>0]

input = prepare_input(input)

positions = []


def gather_all_numbers():
	numbers = {}
	for row in range(len(input)):
		curr_start = 0
		curr_end = 0
		last_was_digit = False
		curr_number = []
		for col in range(len(input[row])):
			val = input[row][col]

			if not val.isdigit():
				if last_was_digit:
					numbers.update({
						'{}-{}'.format(row, curr_start): {
							'number': int(''.join(curr_number)),
							'start': [row, curr_start],
							'end': [row, curr_end]
						}
					})

					last_was_digit = False
					curr_number = []
				continue

			if last_was_digit:
				curr_number.append(val)
				curr_end = col

				if col == len(input[row])-1:
					numbers.update({
						'{}-{}'.format(row, curr_start): {
							'number': int(''.join(curr_number)),
							'start': [row, curr_start],
							'end': [row, curr_end]
						}
					})

				continue

			curr_number = []
			curr_number.append(val)
			curr_start = col
			curr_end = col
			last_was_digit = True

			if col == len(input[row])-1:
				numbers.update({
					'{}-{}'.format(row, curr_start): {
						'number': int(''.join(curr_number)),
						'start': [row, curr_start],
						'end': [row, curr_end]
					}
				})

	return numbers

def check_adjacent(row, col):
	global positions
	for row_ in range(row-1, row+2):
		for col_ in range(col-1, col+2):
			if col_ == col and row_ == row: continue

			value = input[row_][col_]

			if value.isdigit():
				positions.append([row_, col_])


all_numbers = gather_all_numbers()

for row in range(len(input)):
	for col in range(len(input[row])):
		val = input[row][col]

		if val.isdigit() or val == '.': continue

		check_adjacent(row, col)

numbers_to_get = []

for position in positions:
	r, c = position
	for number, number_def in all_numbers.items():
		if r >= number_def.get('start')[0] and r <= number_def.get('end')[0] \
		and c >= number_def.get('start')[1] and c <= number_def.get('end')[1]:
			numbers_to_get.append(number)

answer = 0
for pos in list(set(numbers_to_get)):
	number = all_numbers[pos].get('number')

	answer += number

print(answer)
