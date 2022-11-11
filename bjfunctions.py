from colorama import Fore, Back, Style
from bjclass import *


# Functions:
def take_bet(bank):
    while True:
        try:
            bank.bet = int(input(Fore.CYAN + "Please, enter your bet: "))
        except ValueError:
            print(Fore.RED + "Sorry, bet must be a number!")
        else:
            if bank.bet > bank.total:
                print(Fore.RED + "Not enough cash! You have: ", bank.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # using this to control a upcoming loop.

    while True:
        x = input(Fore.CYAN + "Would you like to hit (H) or stand (S) ?: ")

        if x[0].lower() == 'h':
            hit(deck, hand)  # Using hit above.

        elif x[0].lower() == 's':
            print(Fore.WHITE + "The dealer is playing")
            playing: bool = False

        else:
            print(Fore.RED + "Try again, using H for Hit and S for Stand!")
            continue
        break


def show_some(player, dealer):
    print(Fore.MAGENTA + "\nDealer's Hand:")
    print(Fore.MAGENTA + " <card hidden>")
    print(Fore.MAGENTA + '', dealer.cards[1])
    print(Fore.BLUE + "\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print(Fore.MAGENTA + "\nDealer's Hand:", *dealer.cards, sep='\n ')
    print(Fore.MAGENTA + "Dealer's Hand =", dealer.value)
    print(Fore.BLUE + "\nPlayer's Hand:", *player.cards, sep='\n ')
    print(Fore.BLUE + "Player's Hand =", player.value)


# endgames:
def player_bust(player, dealer, bank):
    print(Fore.RED + "Player busted!")
    bank.lose_bet()


def player_wins(player, dealer, bank):
    print(Fore.GREEN + "Player wins!")
    bank.win_bet()


def dealer_bust(player, dealer, bank):
    print(Fore.MAGENTA + "Dealer busted!")
    bank.win_bet()


def dealer_wins(player, dealer, bank):
    print(Fore.MAGENTA + "Dealer wins!")
    bank.lose_bet()


def push(player, dealer):
    print(Fore.CYAN + "Dealer and player tie! It's a push!")
