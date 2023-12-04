import re

lines = open('./input1.txt', 'r', encoding='utf-8')

def get_match(inp, regex):
	result = re.search(regex, inp)

	if result:
		return int(result.group(1))

	return 0

power_sum = 0

for line in lines:
	line = line.strip()

	game_id = get_match(line, '^Game (\d+)')

	games = line.split(':')[1]

	subsets = games.split(';')

	max_values = {
		'red': 0,
		'green': 0,
		'blue': 0,
	}
	for subset in subsets:
		red = get_match(subset, '(\d+) red')
		green = get_match(subset, '(\d+) green')
		blue = get_match(subset, '(\d+) blue')

		if red > max_values['red']:
			max_values.update({
				'red': red,
			})
		if green > max_values['green']:
			max_values.update({
				'green': green,
			})
		if blue > max_values['blue']:
			max_values.update({
				'blue': blue,
			})

	game_power = max_values['red'] * max_values['green'] * max_values['blue']

	power_sum += game_power

print(power_sum)
