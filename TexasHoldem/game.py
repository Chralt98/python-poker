import deck
import rankings


class Game:
    number_of_players = 0
    deck = deck.Deck()
    main_player_card_pair = ()

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players

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

    def flop_cards(self, first, second, third):
        self.deck.set_card_visible(first[0], first[1])
        self.deck.set_card_visible(second[0], second[1])
        self.deck.set_card_visible(third[0], third[1])

    def turn_card(self, fourth):
        self.deck.set_card_visible(fourth[0], fourth[1])

    def river_card(self, fifth):
        self.deck.set_card_visible(fifth[0], fifth[1])

    def remove_player(self):
        self.number_of_players -= 1

    def get_number_of_players(self):
        return self.number_of_players

    def player_folds(self):
        self.deck.fold_cards()


if __name__ == '__main__':
    game = Game(9)
    game.distribute_cards([('D', '7'), ('D', '8')])
    game.flop_cards(('D', 'J'), ('D', '10'), ('D', '9'))
    game.turn_card(('S', '3'))
    game.river_card(('S', '8'))
    print('Open cards: ' + str(game.get_open_cards()))
    ranking = rankings.Rankings()
    print(str(ranking.recognize_hand_ranking()))
