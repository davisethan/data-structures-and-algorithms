from Deck import Deck
from Holder import Player, Dealer, IllegalBetException

class Blackjack:
    def play():
        name = input("Give player name ")
        pot = int(input(f"Give {name} pot "))
        players = [Player(name, pot)]
        blackjack = Blackjack(players)
        while blackjack._player_can_bet(players[0]):
            blackjack._play_round()

    def __init__(self, players, print = print, input = input):
        deck = Deck()
        deck.shuffle()
        
        self._deck = deck
        self._holders = players + [Dealer()]
        self._print = print
        self._input = input

    def _play_round(self):
        self._dealer_deals_cards()
        self._players_make_bets()
        self._holders_take_turns()
        self._finish_round()

    def _player_can_bet(self, player):
        return 0 < player.get_pot()

    def _dealer_deals_cards(self):
        for holder in self._holders:
            hand = [self._deck.hit(), self._deck.hit()]
            holder.set_hand(hand)

    def _players_make_bets(self):
        for player in self._holders[:-1]:
            self._player_makes_bet(player)

    def _player_makes_bet(self, player):
        self._print(f"Dealer has {self._holders[-1]._hand[0]}")
        self._print(f"{player.get_name()} has hand {', '.join([str(card) for card in player.get_hand()])}")
        self._print(f"{player.get_name()} has pot {player.get_pot()}")
        bet = int(self._input(f"{player.get_name()} give bet "))

        try:
            player.make_bet(bet)
        except IllegalBetException:
            self._print(f"Illegal bet. Bet should be integer from 1 to {player.get_pot()}")
            self._player_makes_bet(player)

    def _holders_take_turns(self):
        for player in self._holders[:-1]:
            self._player_takes_turn(player)

        self._dealer_takes_turn(self._holders[-1])

    def _player_takes_turn(self, player):
        hit = self._get_player_hit(player)
        self._player_takes_hit(player, hit)

    def _get_player_hit(self, player):
        if 21 < player.get_hand_score():
            return False
        
        hit = ""
        YES = "y"
        NO = "n"

        while hit not in (YES, NO):
            self._print(f"{player.get_name()} has score {player.get_hand_score()}")
            hit = self._input(f"Hit or stand. Hit? (y/n) ")

        return YES == hit

    def _player_takes_hit(self, player, hit):
        if hit:
            player.hit_deck(self._deck.hit())
            self._player_takes_turn(player)

    def _dealer_takes_turn(self, dealer):
        DEALER_HIT_SCORE = 17
        while DEALER_HIT_SCORE > dealer.get_hand_score():
            dealer.hit_deck(self._deck.hit())

    def _finish_round(self):
        dealer = self._holders[-1]
        for player in self._holders[:-1]:
            if self._player_tie(player):
                self._print(f"{player.get_name()} ties")
                player.add_to_pot(player._bet)
            elif self._player_blackjack(player):
                self._print(f"{player.get_name()} has Blackjack!")
                player.add_to_pot(player._bet + 2 * player._bet)
            elif self._player_loss(player):
                self._print(f"{player.get_name()} loss")
            elif self._player_win(player):
                self._print(f"{player.get_name()} wins!")
                player.add_to_pot(player._bet + player._bet)

            player.set_hand([])
            player.clear_bet()

    def _player_tie(self, player):
        dealer = self._holders[-1]
        return dealer.get_hand_score() == player.get_hand_score()

    def _player_blackjack(self, player):
        return 21 == player.get_hand_score() and 2 == len(player.get_hand())

    def _player_loss(self, player):
        dealer = self._holders[-1]
        player_loses = 21 < player.get_hand_score() or dealer.get_hand_score() > player.get_hand_score()
        return

    def _player_win(self, player):
        dealer = self._holders[-1]
        return dealer.get_hand_score() < player.get_hand_score() and 21 >= player.get_hand_score()

if __name__ == "__main__":
    Blackjack.play()
