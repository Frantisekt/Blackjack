import random
from first_hand import *

deck = make_cards() # This line creates the deck.
deck2 = random.sample(deck, len(deck))
# print(deck2)

count, player, house = 0 , [], []
while count < 2:  # With this while loop draws the first cards 2 for each.
	player.append(deck2[0])  # draws a card for the player.
	deck2.pop(0)
	# Draws a card for the house.which gets the first card face down (not show).
	house.append(deck2[0])
	deck2.pop(0)
	count += 1

print('Player cards:', player)
print('House cards:', house[0])

points = 10 
while points > 0:
	bet = int(input('How much you want to bet?'))
	points = points - bet
	pot = bet*2

	while True: 
		p_value = 0
		h_value = 0
		print('You have:' + str(points) +  'points.')
		choice = input("Would you like to: Draw or Stay?")

		if choice == 'd':
			player.append(deck2[0])  # a new card for the player.  	# FACTORIZE
			deck2.pop(0)
			print('Hand Total value:', p_letter_value(player))
			print(player)
			if p_letter_value(player) > 21:
				print("You lost your bet", p_letter_value(player))
				bet = 0
				break  # active = False

		elif choice == 's':  # shows the hidden card from the house.
			while h_letter_value(house) <= p_letter_value(player):
				print("The house draws")   # FACTORIZE
				house.append(deck2[0])  # a new card for the house.
				deck2.pop(0)
				print(house)
				if h_letter_value(house) > 21:
					print("You won!", pot, h_letter_value(house))
					points = points + pot
					break  # active = False
				elif p_letter_value(player) < h_letter_value(house) <= 21:
					print("You lost!", h_letter_value(house))
					break # active = False
				elif p_letter_value(player) == h_letter_value(house) and h_letter_value(house) >= 18:
					print('The house Checks')
					points += bet
					break # active = False

			deck = make_cards() # this line creates the deck.
			deck2 = random.sample(deck, len(deck))
			count, player, house = 0, [], []

			while count < 2:  # With this while loop draws the first cards.
				#deck.pop(0)
				player.append(deck2[0])  # For the player.
				deck2.pop(0)
				# For the house. which gets the first card face down (not show).
				house.append(deck2[0])
				deck2.pop(0)
				count += 1
			print('Player cards:', player)
			print('House cards:', house[0])
			break