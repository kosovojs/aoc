import re

input = open('./input1.txt', 'r', encoding='utf-8').read()

def prepare_input(input):
	return [[char for char in f.strip()] for f in input.split('\n') if len(f)>0]

input = prepare_input(input)

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
	curr_positions = []
	for row_ in range(row-1, row+2):
		for col_ in range(col-1, col+2):
			if col_ == col and row_ == row: continue

			value = input[row_][col_]

			if value.isdigit():
				curr_positions.append([row_, col_])

	return curr_positions

all_numbers = gather_all_numbers()

def get_numbers_from_positions(positions):
	numbers_to_get = []
	for position in positions:
		r, c = position
		for number, number_def in all_numbers.items():
			if r >= number_def.get('start')[0] and r <= number_def.get('end')[0] \
			and c >= number_def.get('start')[1] and c <= number_def.get('end')[1]:
				numbers_to_get.append(number)


	return numbers_to_get


ratio_sum = 0

for row in range(len(input)):
	for col in range(len(input[row])):
		val = input[row][col]

		if not val == '*': continue

		pos = check_adjacent(row, col)

		nmbrs = get_numbers_from_positions(pos)
		if len(set(nmbrs)) == 2:
			nmbrs = [all_numbers[pos].get('number') for pos in set(nmbrs)]

			ratio = nmbrs[0] * nmbrs[1]

			ratio_sum += ratio

print(ratio_sum)
