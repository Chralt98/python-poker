import deck


class Game:
    deck = deck.Deck()
    deck.create_deck()

    def get_table_open_cards(self):
        return self.deck.get_table_open_cards()

    def get_main_player_cards(self):
        return self.deck.get_main_player_cards()

    def distribute_cards(self, pair):
        self.deck.add_main_player_card(pair[0][0], pair[0][1])
        self.deck.add_main_player_card(pair[1][0], pair[1][1])

    def flop_cards(self, *args):
        for arg in args:
            self.deck.set_card_visible(arg[0], arg[1])

