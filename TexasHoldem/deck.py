
class Deck:
    MAX_NUMBER_OF_CARDS = 52
    # number of cards which are still in game and not folded
    number_of_active_cards = MAX_NUMBER_OF_CARDS
    # cards which the main player can not see
    concealed_cards = []
    # cards which the main player can see on table
    open_cards = []
    # cards of the main player
    main_player_cards = []
    # cards other players has
    invisible_distributed_cards = 0

    def __init__(self):
        # Diamonds, Clubs, Hearts, Spades
        suits = {'D', 'C', 'H', 'S'}
        # Jack, Queen, King, Ass
        icons = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
        for icon in icons:
            for suit in suits:
                # create the tuple card list and nobody can see them
                self.concealed_cards.append((suit, icon))

    def get_current_number_of_cards(self):
        return len(self.concealed_cards)

    def set_card_visible(self, suit, icon):
        if (suit, icon) in self.concealed_cards:
            self.open_cards.append((suit, icon))
            self.concealed_cards.remove((suit, icon))
        else:
            print('Card is not in concealed cards.')

    def get_main_player_visible_cards(self):
        return self.get_main_player_cards() + self.get_open_cards()

    def add_main_player_card(self, suit, icon):
        if (suit, icon) in self.concealed_cards:
            self.main_player_cards.append((suit, icon))
            self.concealed_cards.remove((suit, icon))
        else:
            print('Card is not in concealed cards.')

    def get_main_player_cards(self):
        return self.main_player_cards

    def get_open_cards(self):
        return self.open_cards

    def fold_cards(self):
        self.number_of_active_cards -= 2
        self.invisible_distributed_cards -= 2

    def distribute_two_cards(self):
        self.invisible_distributed_cards += 2

    def get_invisible_distributed_number_of_cards(self):
        return self.invisible_distributed_cards

    def get_number_of_active_cards(self):
        return self.number_of_active_cards

    def get_number_of_open_cards(self):
        return len(self.open_cards)

    def get_number_of_concealed_cards(self):
        return len(self.concealed_cards)
