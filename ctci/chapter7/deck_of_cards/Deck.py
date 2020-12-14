import random
from Card import Card

class Deck:
    def __init__(self):
        hearts_2_4 = [Card(Card.HEART, Card.TWO), Card(Card.HEART, Card.THREE), Card(Card.HEART, Card.FOUR)]
        hearts_5_7 = [Card(Card.HEART, Card.FIVE), Card(Card.HEART, Card.SIX), Card(Card.HEART, Card.SEVEN)]
        hearts_8_10 = [Card(Card.HEART, Card.EIGHT), Card(Card.HEART, Card.NINE), Card(Card.HEART, Card.TEN)]
        hearts_jack_ace = [Card(Card.HEART, Card.JACK), Card(Card.HEART, Card.QUEEN), Card(Card.HEART, Card.KING), Card(Card.HEART, Card.ACE)]
        hearts = hearts_2_4 + hearts_5_7 + hearts_8_10 + hearts_jack_ace

        spades_2_4 = [Card(Card.SPADE, Card.TWO), Card(Card.SPADE, Card.THREE), Card(Card.SPADE, Card.FOUR)]
        spades_5_7 = [Card(Card.SPADE, Card.FIVE), Card(Card.SPADE, Card.SIX), Card(Card.SPADE, Card.SEVEN)]
        spades_8_10 = [Card(Card.SPADE, Card.EIGHT), Card(Card.SPADE, Card.NINE), Card(Card.SPADE, Card.TEN)]
        spades_jack_ace = [Card(Card.SPADE, Card.JACK), Card(Card.SPADE, Card.QUEEN), Card(Card.SPADE, Card.KING), Card(Card.SPADE, Card.ACE)]
        spades = spades_2_4 + spades_5_7 + spades_8_10 + spades_jack_ace

        diamonds_2_4 = [Card(Card.DIAMOND, Card.TWO), Card(Card.DIAMOND, Card.THREE), Card(Card.DIAMOND, Card.FOUR)]
        diamonds_5_7 = [Card(Card.DIAMOND, Card.FIVE), Card(Card.DIAMOND, Card.SIX), Card(Card.DIAMOND, Card.SEVEN)]
        diamonds_8_10 = [Card(Card.DIAMOND, Card.EIGHT), Card(Card.DIAMOND, Card.NINE), Card(Card.DIAMOND, Card.TEN)]
        diamonds_jack_ace = [Card(Card.DIAMOND, Card.JACK), Card(Card.DIAMOND, Card.QUEEN), Card(Card.DIAMOND, Card.KING), Card(Card.DIAMOND, Card.ACE)]
        diamonds = diamonds_2_4 + diamonds_5_7 + diamonds_8_10 + diamonds_jack_ace

        clubs_2_4 = [Card(Card.CLUB, Card.TWO), Card(Card.CLUB, Card.THREE), Card(Card.CLUB, Card.FOUR)]
        clubs_5_7 = [Card(Card.CLUB, Card.FIVE), Card(Card.CLUB, Card.SIX), Card(Card.CLUB, Card.SEVEN)]
        clubs_8_10 = [Card(Card.CLUB, Card.EIGHT), Card(Card.CLUB, Card.NINE), Card(Card.CLUB, Card.TEN)]
        clubs_jack_ace = [Card(Card.CLUB, Card.JACK), Card(Card.CLUB, Card.QUEEN), Card(Card.CLUB, Card.KING), Card(Card.CLUB, Card.ACE)]
        clubs = clubs_2_4 + clubs_5_7 + clubs_8_10 + clubs_jack_ace

        cards = hearts + spades + diamonds + clubs

        self._cards = cards

    def shuffle(self):
        for index, card in enumerate(self._cards):
            random_index = random.randint(0, len(self._cards) - 1)
            self._swap(self._cards, index, random_index)
    
    def _swap(self, ordered, index, swap_index):
        saved = ordered[index]
        ordered[index] = ordered[swap_index]
        ordered[swap_index] = saved

    def hit(self):
        return self._cards.pop()
