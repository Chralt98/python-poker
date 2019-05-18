from TexasHoldem import deck
from TexasHoldem import player
from TexasHoldem import rankings


class Game:
    number_of_players = 0
    players = []
    deck = deck.Deck()
    main_player_card_pair = ()
    small_blind_amount = 0
    big_blind_amount = 0
    poker_pot = 0
    minimal_chips_amount = 0

    def __init__(self, number_of_players, chips_value):
        self.number_of_players = number_of_players
        for i in range(number_of_players):
            self.players.append(player.Player(i, chips_value))

    def start_round(self, start_player_id, small_blind_amount):
        self.poker_pot = 0
        self.set_initial_blinds(start_player_id)
        self.set_small_blind_amount(small_blind_amount)
        self.set_big_blind_amount(2 * small_blind_amount)

    def finish_round(self):
        for p in self.players:
            p.set_small_blind(False)
            p.set_big_blind(False)

    def get_open_cards(self):
        return self.deck.get_open_cards()

    def distribute_cards(self, pair):
        if self.number_of_players == 0:
            print('Please add players before distributing cards!')
        else:
            # the main player does not count so that is why -1
            for i in range(self.number_of_players - 1):
                self.deck.distribute_two_cards()
            self.main_player_card_pair = pair
            print('Main player cards: ' + str(self.get_main_player_pair()))
            self.deck.add_main_player_card(pair[0][0], pair[0][1])
            self.deck.add_main_player_card(pair[1][0], pair[1][1])

    def get_main_player_pair(self):
        return self.main_player_card_pair

    def set_small_blind_amount(self, amount):
        self.small_blind_amount = amount

    def set_big_blind_amount(self, amount):
        self.big_blind_amount = amount
        self.set_minimal_chips_amount(amount)

    def get_small_blind_amount(self):
        return self.small_blind_amount

    def get_big_blind_amount(self):
        return self.big_blind_amount

    def set_initial_blinds(self, small_blind_player_id):
        self.players[small_blind_player_id].set_small_blind(True)
        self.players[small_blind_player_id].sub_chips_amount(self.get_small_blind_amount())
        self.players[(small_blind_player_id + 1) % self.number_of_players].set_big_blind(True)
        self.players[(small_blind_player_id + 1) % self.number_of_players].sub_chips_amount(self.get_big_blind_amount())

    def flop_cards(self, first, second, third):
        self.deck.set_card_visible(first[0], first[1])
        self.deck.set_card_visible(second[0], second[1])
        self.deck.set_card_visible(third[0], third[1])

    def turn_card(self, fourth):
        self.deck.set_card_visible(fourth[0], fourth[1])

    def river_card(self, fifth):
        self.deck.set_card_visible(fifth[0], fifth[1])

    def remove_player(self, player_id):
        self.players.pop(player_id)
        self.number_of_players -= 1

    def get_number_of_players(self):
        return self.number_of_players

    def set_minimal_chips_amount(self, amount):
        if self.minimal_chips_amount >= self.get_big_blind_amount():
            self.minimal_chips_amount = amount
        else:
            print('Minimal chips amount has to be greater or equals big blind.')

    def get_minimal_chips_amount(self):
        return self.minimal_chips_amount

    def player_folds(self):
        self.deck.fold_cards()

    def player_pays(self, player_id, amount):
        if self.get_minimal_chips_amount() <= amount:
            self.players[player_id].sub(amount)
            self.poker_pot += amount
        else:
            print('Player needs to pay the minimal amount to continue playing.')

    def player_wins(self, player_id):
        self.players[player_id].add(self.poker_pot)


if __name__ == '__main__':
    game = Game(9, 1000)
    game.start_round(0, 50)
    game.distribute_cards([('D', '7'), ('D', '8')])
    game.flop_cards(('D', 'J'), ('D', '10'), ('D', '9'))
    game.turn_card(('S', '3'))
    game.river_card(('S', '8'))
    print('Open cards: ' + str(game.get_open_cards()))
    ranking = rankings.Rankings()
    ranking.recognize_hand_ranking()
