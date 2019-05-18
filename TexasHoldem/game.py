import deck


class Game:
    deck = deck.Deck()
    main_player_card_pair = ()
    number_of_players = 0

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players

    def get_table_open_cards(self):
        return self.deck.get_table_open_cards()

    def get_main_player_cards(self):
        return self.deck.get_main_player_cards()

    def distribute_cards(self, pair):
        if self.number_of_players <= 0:
            print('Please add players before distributing cards!')
        else:
            # the main player does not count so that is why -1
            for i in range(self.number_of_players - 1):
                self.deck.distribute_two_cards()
            self.deck.add_main_player_card(pair[0][0], pair[0][1])
            self.deck.add_main_player_card(pair[1][0], pair[1][1])

    def flop_cards(self, *args):
        for arg in args:
            self.deck.set_card_visible(arg[0], arg[1])

    def player_folds(self):
        self.deck.fold_cards()
