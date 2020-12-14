import unittest
from Blackjack import Blackjack
from Card import Card
from Deck import Deck
from Holder import Player, IllegalBetException

class TestHolder(unittest.TestCase):
    def test_get_hand_score(self):
        # (case name, hand, expected hand score)
        cases = [
            ("numbers_no_faces_no_aces", [Card(Card.HEART, Card.TWO), Card(Card.HEART, Card.THREE)], 5),
            ("no_numbers_faces_no_aces", [Card(Card.HEART, Card.JACK), Card(Card.HEART, Card.QUEEN)], 20),
            ("numbers_faces_no_aces", [Card(Card.HEART, Card.TWO), Card(Card.HEART, Card.JACK)], 12),
            ("no_numbers_no_faces_aces", [Card(Card.HEART, Card.ACE), Card(Card.SPADE, Card.ACE)], 12),
            ("numbers_no_faces_aces", [Card(Card.HEART, Card.TWO), Card(Card.HEART, Card.ACE)], 13),
            ("no_numbers_faces_aces", [Card(Card.HEART, Card.JACK), Card(Card.HEART, Card.ACE)], 21),
            ("numbers_faces_aces", [Card(Card.HEART, Card.TWO), Card(Card.HEART, Card.JACK), Card(Card.HEART, Card.ACE)], 13),
        ]
        for case in cases:
            with self.subTest(case[0]):
                player = Player()
                player.set_hand(case[1])

                actual_hand_score = player.get_hand_score()

                self.assertEqual(case[2], actual_hand_score)

    def test_player_makes_bet(self):
        pot = 100
        bet = 10
        player = Player("Jill", pot)

        player.make_bet(bet)

        self.assertEqual(pot - bet, player.get_pot())
        self.assertEqual(bet, player.get_bet())

class TestBlackjack(unittest.TestCase):
    def test_dealer_deals_cards(self):
        blackjack = Blackjack([Player()])

        blackjack._dealer_deals_cards()

        player_hand = blackjack._holders[0].get_hand()
        dealer_hand = blackjack._holders[1].get_hand()

        self.assertEqual(2, len(player_hand))
        self.assertEqual(2, len(dealer_hand))
        self.assertEqual(48, len(blackjack._deck._cards))

    def test_player_makes_bet(self):
        player = Player("Jill", 100)
        # (case name, bet, expected prints, expected inputs)
        cases = [
            (
                "legal_bet",
                [10],
                ["Dealer has", "has hand", "has pot"],
                [("give bet", 10)]
            ),
            (
                "noninteger_bet",
                [10.10, 10],
                ["Dealer has", "has hand", "has pot", "Illegal bet", "Dealer has", "has hand", "has pot"],
                [("give bet", 10.10), ("give bet", 10)]
            ),
            (
                "below_zero_bet",
                [-10, 10],
                ["Dealer has", "has hand", "has pot", "Illegal bet", "Dealer has", "has hand", "has pot"],
                [("give bet", -10), ("give bet", 10)]
            ),
            (
                "over_pot_bet",
                [110, 10],
                ["Dealer has", "has hand", "has pot", "Illegal bet", "Dealer has", "has hand", "has pot"],
                [("give bet", 110), ("give bet", 10)]
            ),
        ]
        for case in cases:
            expected_prints = list(reversed(case[2]))
            expected_inputs = list(reversed(case[3]))
            def test_print(statement):
                self.assertTrue(expected_prints.pop() in statement)
            def test_input(prompt):
                expected_input = expected_inputs.pop()
                self.assertTrue(expected_input[0] in prompt)
                return expected_input[1]
            blackjack = Blackjack([player], test_print, test_input)
            blackjack._dealer_deals_cards()

            blackjack._player_makes_bet(player)

    def test_get_player_hit(self):
        player = Player("Jill", 100)
        # (case name, expected prints, expected inputs)
        cases = [
            ("ask_twice_to_stand", ["has score", "has score"], [("Hit or stand", "b"), ("Hit or stand", "n")]),
        ]
        for case in cases:
            expected_prints = list(reversed(case[1]))
            expected_inputs = list(reversed(case[2]))
            def test_print(statement):
                self.assertTrue(expected_prints.pop() in statement)
            def test_input(prompt):
                expected_input = expected_inputs.pop()
                self.assertTrue(expected_input[0] in prompt)
                return expected_input[1]
            blackjack = Blackjack([player], test_print, test_input)
            blackjack._dealer_deals_cards()
            
            blackjack._get_player_hit(player)

    def test_finish_round(self):
        player = Player("Jill", 100)
        # (case name, expected prints, player cards, dealer cards)
        cases = [
            (
                "player_loss",
                ["loss"],
                [Card(Card.HEART, Card.TEN), Card(Card.HEART, Card.NINE)],
                [Card(Card.SPADE, Card.TEN), Card(Card.DIAMOND, Card.TEN)]
            ),
            (
                "player_tie",
                ["tie"],
                [Card(Card.HEART, Card.TEN), Card(Card.CLUB, Card.TEN)],
                [Card(Card.SPADE, Card.TEN), Card(Card.DIAMOND, Card.TEN)]
            ),
            (
                "player_win",
                ["win"],
                [Card(Card.SPADE, Card.TEN), Card(Card.DIAMOND, Card.TEN)],
                [Card(Card.HEART, Card.TEN), Card(Card.HEART, Card.NINE)]
            ),
            (
                "player_blackjack_dealer_blackjack",
                ["tie"],
                [Card(Card.HEART, Card.TEN), Card(Card.HEART, Card.ACE)],
                [Card(Card.SPADE, Card.JACK), Card(Card.SPADE, Card.ACE)]
            ),
            (
                "player_blackjack_dealer_non_blackjack",
                ["Blackjack"],
                [Card(Card.HEART, Card.TEN), Card(Card.HEART, Card.ACE)],
                [Card(Card.HEART, Card.TEN), Card(Card.HEART, Card.NINE)]
            ),
        ]
        for case in cases:
            expected_prints = list(reversed(case[1]))
            def test_print(statement):
                self.assertTrue(expected_prints.pop() in statement)
            blackjack = Blackjack([player], test_print)
            blackjack._holders[0].set_hand(case[2])
            blackjack._holders[1].set_hand(case[3])

            blackjack._finish_round()

if __name__ == "__main__":
    unittest.main()
