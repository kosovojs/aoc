lines = open('./input1.txt', 'r', encoding='utf-8')

int_sum = 0

replace_mapping = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9',
}

def while_stmt(string_start_idx, finalized_input, ordering):
	if ordering == 'asc':
		return string_start_idx < len(finalized_input)

	return string_start_idx > -1

def get_digit(input, ordering):
	string_start_idx = 0 if ordering == 'asc' else len(input)-1

	finalized_input = input

	while while_stmt(string_start_idx, finalized_input, ordering):
		if finalized_input[string_start_idx].isdigit():
			return finalized_input[string_start_idx]

		current_input = finalized_input[string_start_idx:]
		replaced = False

		for to_repl, replacable in replace_mapping.items():
			if current_input.startswith(to_repl):
				finalized_input = "{}{}{}".format(finalized_input[:string_start_idx], replacable, finalized_input[string_start_idx+len(to_repl):])
				replaced = True

				string_start_idx = 0 if ordering == 'asc' else len(finalized_input)-1
				break
		if not replaced:
			if ordering == 'asc':
				string_start_idx += 1
			else:
				string_start_idx -= 1


def get_first_digit(input):
	return get_digit(input, 'asc')

def get_last_digit(input):
	return get_digit(input, 'desc')

for line in lines:
	line = line.strip()
	#orig_line = line

	first = get_first_digit(line)
	last = get_last_digit(line)

	line_value = int("{}{}".format(first, last))

	#debug.append("{} -> {}: {}".format(orig_line, line, line_value))

	int_sum += line_value

print(int_sum)
