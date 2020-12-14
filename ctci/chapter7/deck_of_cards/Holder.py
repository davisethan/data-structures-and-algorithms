from abc import ABC
from Card import Card

class Holder(ABC):
    def __init__(self):
        self._hand = []

    def set_hand(self, hand):
        self._hand = hand

    def hit_deck(card):
        self._hand.append(card)

    def get_hand_score(self):
        self._sort_hand_by_aces()
        return self._get_sorted_hand_score()

    def _sort_hand_by_aces(self):
        for index, card in enumerate(self._hand):
            if Card.ACE in str(card):
                self._hand.append(self._hand.pop(index))

    def _get_sorted_hand_score(self):
        hand_score = 0
        for card in self._hand:
            if Card.TWO in str(card):
                hand_score += 2
            elif Card.THREE in str(card):
                hand_score += 3
            elif Card.FOUR in str(card):
                hand_score += 4
            elif Card.FIVE in str(card):
                hand_score += 5
            elif Card.SIX in str(card):
                hand_score += 6
            elif Card.SEVEN in str(card):
                hand_score += 7
            elif Card.EIGHT in str(card):
                hand_score += 8
            elif Card.NINE in str(card):
                hand_score += 9
            elif Card.TEN in str(card):
                hand_score += 10
            elif Card.JACK in str(card):
                hand_score += 10
            elif Card.QUEEN in str(card):
                hand_score += 10
            elif Card.KING in str(card):
                hand_score += 10
            elif Card.ACE in str(card):
                BLACKJACK_SCORE = 21
                ACE_HIGH_SCORE = 11
                ACE_LOW_SCORE = 1
                if BLACKJACK_SCORE < hand_score + ACE_HIGH_SCORE:
                    hand_score += ACE_LOW_SCORE
                else:
                    hand_score += ACE_HIGH_SCORE
        return hand_score

class Player(Holder):
    def __init__(self, name, pot):
        self._name = name
        self._pot = pot
        self._bet = 0

    def make_bet(self, amount):
        if 0 >= amount:
            raise IllegalBetException()
        elif self._pot < amount:
            raise IllegalBetException()
        elif not isinstance(amount, int):
            raise IllegalBetException()

        self._bet = amount
        self._pot -= self._bet


class IllegalBetException(Exception):
    pass
