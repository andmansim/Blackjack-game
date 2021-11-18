# How to play blackjack?:
# player wins with 21 points or a higher value than the Dealer = distribuidor, without going bust = have a number higer than 21. You can win if the Dealer Busts and the player not. 
# The player see the first card of the Dealer. 
# movements: Hit = ask for more cards, but the maximun is 4. 
#           Stand = when you decide not to continue. But the Dealer will continue getting cards until it Bust, Stand or Win.  
#           Bust = player automatically lose if they get Bust, it doesn't matter if the Dealer does too.     
#           Push = when the player and the Dealer have blackjack. It return the best = apuesta and the cards are deal = repartir, again
#           Doubling Down = you can doit if you are dealt with a strong hand, and you can get a card before showing it
#           Splitting a pair = you can doit if the fist dealt the two cards are the same one. So you will play with two hands at the same time
#           Insurance = seguro, if the exposed card of the Deal is an Ace, you can do a bet to insurance, this is independent of the inicial one, it's 2:1
# winning the game: if the player wins, it's bet will return and you recieve the equal number of chips from the Dealer
# If you win with a Blackjack = 21 points, your bet will return and you recieve 3 chips for every 2 chips that you bet
# cards: 2 decks of 52 each one. The cards are from 2 to 10 with their equal value, Q = J = K =10, and As = 1/11
# valor de las cartas
print("Values cards are:") 
cards = {chr(0x1f0a1): 11, chr(0x1f0a2): 2, chr(0x1f0a3): 3, chr(0x1f0a4): 4, chr(0x1f0a5): 5, chr(0x1f0a6): 6, chr(0x1f0a7): 7, chr(0x1f0a8): 8, chr(0x1f0a9): 9, chr(0x1f0aa): 10, chr(0x1f0ab): 10, chr(0x1f0ad): 10, chr(0x1f0ae): 10 }
print (cards)
# cartas
deck = [chr(x) for x in range (0x1f0a1, 0x1f0ae)]
from random import shuffle
#choice(deck)
shuffle(deck)
print(deck)

print("Choose one number from 0 to 13:")
player = int(input())
position = deck[player]
position2 = deck[player + 1]
print(position)
print(position2)


value1 = cards[position]
value2 = cards[position2]
print (value1)
print (value2)
