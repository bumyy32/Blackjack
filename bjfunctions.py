# Functions:
def take_bet(bank):
    while True:
        try:
            bank.bet = int(input("Please, enter your bet: "))
        except ValueError:
            print("Sorry, bet must be a number!")
        else:
            if bank.bet > bank.total:
                print("Not enough cash! You have: ", bank.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # using this to control a upcoming loop.

    while True:
        x = input("Would you like to hit (H) or stand (S) ?: ")

        if x[0].lower() == 'h':
            hit(deck, hand)  # Using hit above.

        elif x[0].lower() == 's':
            playing = False

        else:
            print("Try again, using H for Hit and S for Stand!")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


# endgames:
def player_bust(player, dealer, bank):
    print("Player busted!")
    bank.lose_bet()


def player_wins(player, dealer, bank):
    print("Player wins!")
    bank.win_bet()


def dealer_bust(player, dealer, bank):
    print("Dealer busted!")
    bank.win_bet()


def dealer_wins(player, dealer, bank):
    print("Dealer wins!")
    bank.lose_bet()


def push(player, dealer):
    print("Dealer and player tie! It's a push!")

