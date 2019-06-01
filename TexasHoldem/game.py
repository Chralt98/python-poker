from possibility import Possibility


class Game(Possibility):
    def reset(self):
        self.remove_opponent_player_cards()
        self.remove_open_table_cards()
        self.remove_burned_cards()
        self.clear_straights()
        self.reset_possibilities()

    def distribute_cards(self, pair):
        self.add_main_player_card(pair[0][0], pair[0][1])
        self.add_main_player_card(pair[1][0], pair[1][1])

    def flop_cards(self, *args):
        for arg in args:
            self.set_card_visible(arg[0], arg[1])

    def burn_card(self, card):
        self.burn_one_card(card)
