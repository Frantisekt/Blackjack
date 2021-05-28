def make_cards(p1=["♣", "♦", "♥", "♠"], p2=["J", "Q", "K", "A"], deck = []):
    # Need to be here otherwise the cards
    # will be drawn from the top of the same deck.
    for i in range(2, 11):  # This for loop creates the cards from 2-10.
        for j in p1:
            card = str(i) + j
            deck.append(card)
    for x in p1:  # This for loop create the cards with letters.
        for y in p2:
            card2 = y + x
            deck.append(card2)
    return deck

# This function substract the value for the 2-10 cards.
def p_letter_value(player, p_value=0):
	for n in player:
		if len(n) == 3:
			p_value += int(n[0:2])
		elif n[0] == 'K' or n[0] == 'Q' or n[0] == 'J':
			p_value += 10
		elif n[0] == 'A':
			p_value += 11
		else:
			p_value += int(n[0])
# This function is to modify the 'A' value in case it
	for m in player:
		if p_value > 21 and m[0] == 'A':  # over pass the 21 value.
			p_value = p_value - 10
	return p_value

# This function substract the value for the 2-10 cards.
def h_letter_value(house, h_value=0):
	for n in house:
		if n[0] == 'K' or n[0] == 'Q' or n[0] == 'J':
			h_value += 10
		elif n[0] == 'A':
			h_value += 11
		else:
			h_value += int(n[0])
	# This function is to modify the 'A' value in case it
	for m in house:
		if h_value > 21 and m[0] == 'A':  # over pass the 21 value.
			h_value = h_value - 10
	return h_value


def deal_out(deck2, player=[], house=[], count=0):
    while count < 2:  # With this while loop draws the first cards 2 for each.
        # deck.pop(0)
        player.append(deck2[0])  # draws a card for the player.
        deck2.pop(0)
        # Draws a card for the house.which gets the first card face down (not show).
        house.append(deck2[0])
        deck2.pop(0)
        count += 1
    return player, house[0]
