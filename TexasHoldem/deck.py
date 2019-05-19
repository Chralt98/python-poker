
class Deck:
    MAX_NUMBER_OF_CARDS = 52
    # number of cards which are still in game and not folded
    number_of_active_cards = MAX_NUMBER_OF_CARDS
    # cards which the main player can not see for example every card at beginning
    concealed_cards = []
    # cards which the main player can see on table
    table_open_cards = []
    # cards of the main player
    main_player_cards = []
    # cards other players has
    opponents_cards = 0

    def __init__(self):
        # Diamonds, Clubs, Hearts, Spades
        suits = {'D', 'C', 'H', 'S'}
        # Jack, Queen, King, Ass
        icons = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
        for icon in icons:
            for suit in suits:
                # create the tuple card list and nobody can see them
                self.concealed_cards.append((suit, icon))

    def get_number_concealed_cards(self):
        return len(self.concealed_cards)

    def set_card_visible(self, suit, icon):
        if (suit, icon) in self.concealed_cards:
            self.table_open_cards.append((suit, icon))
            self.concealed_cards.remove((suit, icon))
        else:
            print('Card is not in concealed cards.')

    def get_main_player_visible_cards(self):
        return self.get_main_player_cards() + self.get_table_open_cards()

    def add_main_player_card(self, suit, icon):
        if (suit, icon) in self.concealed_cards:
            self.main_player_cards.append((suit, icon))
            self.concealed_cards.remove((suit, icon))
        else:
            print('Card is not in concealed cards.')

    def set_main_player_cards(self, cards):
        self.main_player_cards = cards

    def remove_opponent_player_cards(self):
        cards = list(self.get_main_player_cards())
        for card in cards:
            self.concealed_cards.append(card)
        self.main_player_cards = []
        return cards

    def get_main_player_cards(self):
        return self.main_player_cards

    def remove_from_concealed_cards(self, cards):
        for card in cards:
            self.concealed_cards.remove(card)

    def get_table_open_cards(self):
        return self.table_open_cards

    def fold_cards(self):
        self.number_of_active_cards -= 2
        self.opponents_cards -= 2

    def distribute_two_cards(self):
        self.opponents_cards += 2

    def get_invisible_distributed_number_of_cards(self):
        return self.opponents_cards

    def get_number_of_active_cards(self):
        return self.number_of_active_cards

    def get_number_of_main_player_cards(self):
        return len(self.main_player_cards)

    def get_number_of_open_cards(self):
        return len(self.table_open_cards)

    def get_number_of_concealed_cards(self):
        return len(self.concealed_cards)

    def get_concealed_cards(self):
        return self.concealed_cards
