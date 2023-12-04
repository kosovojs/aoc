import re
from collections import Counter

lines = open('./input1.txt', 'r', encoding='utf-8')

def get_match(inp, regex):
	result = re.search(regex, inp)

	if result:
		return int(result.group(1))

	return 0

card_sum = 0

def get_winnings(winners, my_cards):
	winners = winners.split(' ')
	my_cards = my_cards.split(' ')
	winners = [f.strip() for f in winners if f.strip() != '']
	my_cards = [f.strip() for f in my_cards if f.strip() != '']

	my_winning_numbers = set(my_cards) & set(winners)

	return len(my_winning_numbers)

cards = []
card_winnings = {}
last_card = 0

for line in lines:
	line = line.strip()
	card_nr = int(get_match(line, '^Card\s+(\d+)'))
	last_card = card_nr
	cards.append(card_nr)

	copies_of_card = cards.count(card_nr)

	card_data = line.split(':')[1]

	winners, my_cards = card_data.split('|')

	winning_cards = get_winnings(winners, my_cards)
	card_winnings.update({card_nr: winning_cards})

	cards_to_add = [f for f in range(card_nr+1, card_nr+winning_cards+1)]

	res = cards_to_add * copies_of_card
	cards.extend(res)

print(len([f for f in cards if f <= last_card]))
