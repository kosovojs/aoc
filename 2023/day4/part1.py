lines = open('./input1.txt', 'r', encoding='utf-8')

card_sum = 0

def get_winnings(winners, my_cards):
	winners = winners.split(' ')
	my_cards = my_cards.split(' ')
	winners = [f.strip() for f in winners if f.strip() != '']
	my_cards = [f.strip() for f in my_cards if f.strip() != '']

	my_winning_numbers = set(my_cards) & set(winners)

	if len(my_winning_numbers) < 1:
		return 0

	return 2 ** (len(my_winning_numbers) - 1)

for line in lines:
	line = line.strip()

	card_data = line.split(':')[1]

	winners, my_cards = card_data.split('|')

	card_sum += get_winnings(winners, my_cards)

print(card_sum)
