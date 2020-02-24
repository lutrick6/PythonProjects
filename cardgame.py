from random import shuffle


class Table:
    # def __init__(self):
    #     self.Deck()
    #     self.Discard()
    #     self.Hand()

    class Card:

        '''
        Class for individule cards.
        The return string(__str__) will change the output of each card
        depending on its value with Ace being the value 14 or 1
        '''

        def __init__(self, grade, suite):
            self.grade = grade
            self.suite = suite

        def __str__(self):
            if self.grade == 11:
                return 'Jack of {}'.format(self.suite)
            if self.grade == 12:
                return 'Queen of {}'.format(self.suite)
            if self.grade == 13:
                return 'King of {}'.format(self.suite)
            if self.grade == 14 or self.grade == 1:
                return 'Ace of {}'.format(self.suite)
            return '{} of {}'.format(self.grade, self.suite)

    class Deck:
        '''
        Class for creating a deck
        the __init__ method will build out the deck then shuffle it
        the Attribute 'cards' are outside of the init method due to the draw method located
        in the Hand class.
        '''

        cards = []

        def __init__(self):
            self.build()
            self.shuffle()

        def __len__(self):  # Used for iteration purposes if needed
            return int(len(self.cards))

        def build(self):  # Build Method will construct the deck based on two lists
            grades = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # List 1
            suites = ["Spades", "Clubs", "Hearts", "Diamonds"]  # List 2
            # Iterates over grades and suites to append the attribute cards with the class Card.
            # Each Card will be an object with a grade and suite
            for g in grades:
                for s in suites:
                    self.cards.append(Table.Card(g, s))

        def shuffle(self):  # Shuffles using Random from the standard library
            shuffle(self.cards)

    class Discard:
        '''
        Discard class for creating a discard pile and methods to send cards from both hand and
        deck if needed.
        '''

        def __init__(self):
            self.discardpile = []

    class Hand:
        '''
        Hand class for creating player hands that will initize a size, cards in hand and
        then draw them based on hand size.
        '''

        def __init__(self, size):
            self.size = size
            self.hand = []
            self.draw()

        def __len__(self):
            return int(self.size)

        def draw(self):
            for i in range(self.size):
                self.hand.append(Table.Deck.cards.pop(i))


deck = Table.Deck()
p1_hand = Table.Hand(5)
p2_hand = Table.Hand(5)

for i in range(len(p1_hand.hand)):
    print(p1_hand.hand[i])
print('')
print('')
for i in range(len(p2_hand.hand)):
    print(p2_hand.hand[i])
print("Deck still has {} cards left".format(len(deck)))
