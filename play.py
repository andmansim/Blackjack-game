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

cards = {chr(0x1f0a1): 11, chr(0x1f0a2): 2, chr(0x1f0a3): 3, chr(0x1f0a4): 4, chr(0x1f0a5): 5, chr(0x1f0a6): 6, chr(0x1f0a7): 7, chr(0x1f0a8): 8, chr(0x1f0a9): 9, chr(0x1f0aa): 10, chr(0x1f0ab): 10, chr(0x1f0ad): 10, chr(0x1f0ae): 10 }
deck = [chr(x) for x in range (0x1f0a1, 0x1f0ae)] 
    
def new_game(deck3):
    print("Values cards are:") 
    print (cards)
    mix_cards(deck3)
    total_player = distribute_cards(deck3) + distribute_cards(deck3)
    total_dealer = distribute_cards(deck3) + distribute_cards(deck3)

    print ("Cards player value: " , total_player)
    print ("Cards dealer value: " , total_dealer)

    if total_player < total_dealer:
        print("Dealer wins!")
    elif total_player > total_dealer:
        print("You win!")
    else:
        print("You tie with the Dealer")
        
def mix_cards (deck2):
    from random import shuffle
    shuffle(deck2)
    print(deck2)
    

def distribute_cards (deck1):
    card1 = deck1[0]
    print(card1)
    value1 = cards[card1]
    print (value1)
    deck1 += [deck1.pop(0)]
    deck1.pop()
    print (deck1)
    return value1

new_game(deck) 
answer = "Y"
while answer == "Y":
    print("Do you want to continue playing?: Y/N")
    answer = input() 
    if answer == "Y":
        cards = {chr(0x1f0a1): 11, chr(0x1f0a2): 2, chr(0x1f0a3): 3, chr(0x1f0a4): 4, chr(0x1f0a5): 5, chr(0x1f0a6): 6, chr(0x1f0a7): 7, chr(0x1f0a8): 8, chr(0x1f0a9): 9, chr(0x1f0aa): 10, chr(0x1f0ab): 10, chr(0x1f0ad): 10, chr(0x1f0ae): 10 }
        deck = [chr(x) for x in range (0x1f0a1, 0x1f0ae)] 
        new_game(deck)
