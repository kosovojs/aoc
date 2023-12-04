import re

lines = open('./input1.txt', 'r', encoding='utf-8')

#  12 red cubes, 13 green cubes, and 14 blue
availability = {
	'red': 12,
	'green': 13,
	'blue': 14
}

def get_match(inp, regex):
	result = re.search(regex, inp)

	if result:
		return int(result.group(1))

	return 0

def is_possible(r, g, b):
	if r > availability['red'] or g > availability['green'] or b > availability['blue']:
		return False

	return True

id_sum = 0

for line in lines:
	line = line.strip()

	game_id = get_match(line, '^Game (\d+)')

	games = line.split(':')[1]

	subsets = games.split(';')

	possible = True
	for subset in subsets:
		red = get_match(subset, '(\d+) red')
		green = get_match(subset, '(\d+) green')
		blue = get_match(subset, '(\d+) blue')

		if not is_possible(red, green, blue):
			possible = False
			break

	if possible:
		id_sum += game_id

print(id_sum)
