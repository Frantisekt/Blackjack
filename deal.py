    
def deal_out(player, house, deck2, count):
    while count < 2:  # With this while loop draws the first cards 2 for each.
        # deck.pop(0)
        player.append(deck2[0])  # draws a card for the player.
        deck2.pop(0)
        # Draws a card for the house.which gets the first card face down (not show).
        house.append(deck2[0])
        deck2.pop(0)
        count += 1
    return  player, house[0]