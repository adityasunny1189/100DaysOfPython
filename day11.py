# BlackJack Game
import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 11]

def random_card():
	return cards[random.randint(0, len(cards) - 1)]

def add_total(cards_collection):
	final_sum_of_card = 0
	for i in cards_collection:
		final_sum_of_card += i
	return final_sum_of_card

def calculate_winner(your_cards, comp_cards):
	your_card_sum = add_total(your_cards)
	comp_card_sum = add_total(comp_cards)
	if your_card_sum > 21:
		return "Comp Win"
	elif your_card_sum > comp_card_sum:
		return "You Win"
	else:
		return "Comp Win"

def start_game():
	play_game = input("Do you want to play game: ")
	your_cards = [random_card(), random_card()]
	comp_cards = [random_card(), random_card()]
	if play_game == "yes":
		print(f"Your cards are {your_cards}")
		print(f"Computer first card is {comp_cards[0]}")
		another_card = input("Do you want another card: ")
		if another_card == "yes":
			your_cards.append(random_card())
			print(f"Your final cards are {your_cards}")
			print(f"Computer final cards are {comp_cards}")
			print(calculate_winner(your_cards, comp_cards))
		else:
			print(f"Your final cards are {your_cards}")
			print(f"Computer final cards are {comp_cards}")
			print(calculate_winner(your_cards, comp_cards))

start_game()