from colorama import Fore, Back, Style
from bjclass import *
from bjfunctions import *

playing = True

# Game setup:

while True:
    # Print an opening statement
    print(Fore.CYAN + "Welcome to *BR BlackJack!*\nIn this game, you will face your gambling addiction just to get"
                      " rich!\nLet's quit talking and let's play, shall we??")
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_bank = Bank()  # Default value is = 100

    # Prompt the Player for their bet
    take_bet(player_bank)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_bank)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

    # Show all cards
    show_all(player_hand, dealer_hand)

    # Different winning scenarios:
    # Player hits 21
    if dealer_hand.value < player_hand.value:
        player_wins(player_hand, dealer_hand, player_bank)

    # Dealer burst
    elif dealer_hand.value > player_hand.value:
        dealer_bust(player_hand, dealer_hand, player_bank)

    # Dealer hits 21
    elif dealer_hand.value > player_hand.value:
        dealer_wins(player_hand, dealer_hand, player_bank)

    # Push / Draw
    else:
        push(player_hand, dealer_hand)

    # Inform Player of their chips total
    if player_bank.total >= 100:
        print(Fore.YELLOW + "\n Your bank balance is: ", player_bank.total)
    elif 50 <= player_bank.total <= 100:
        print(Fore.GREEN + "\n Your bank balance is: ", player_bank.total)
    else:
        print(Fore.RED + "\n Your bank balance is: ", player_bank.total)

    # Ask to play again
    new_game = input(Fore.LIGHTCYAN_EX + "Do you want to play again? Y for Yes / N for No: ")

    if new_game[0].upper() == 'y':
        playing = True
        continue
    else:
        print("Please, try typing correctly :D")
        break
