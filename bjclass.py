import random
# Class:

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):

        self.deck = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)

                self.deck.append(created_card)

    def __str__(self):
        deck_list = ''
        for card in self.deck:
            deck_list += '\n' + card.__str__()
        return 'The deck has: ' + deck_list

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:

    def __init__(self):
        self.cards = []  # We will start with no cards, empty list just like what I did @ Deck
        self.value = 0  # Start with no value
        self.aces = 0  # I need to keep an eye on the aces, I just don't know how :P

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Bank:

    def __init__(self):
        self.total = 100  # Initial bet can be set to a default value, or some value from the user using input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.total - 10

