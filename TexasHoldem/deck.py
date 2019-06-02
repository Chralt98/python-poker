class Deck:
    # cards which the main player can not see for example every card at beginning
    concealed_cards = []
    # cards which the main player can see on table
    table_open_cards = []
    # cards of the main player
    main_player_cards = []
    burned_cards = []

    def create_deck(self):
        # Diamonds, Clubs, Hearts, Spades
        suits = {'D', 'C', 'H', 'S'}
        # Jack, Queen, King, Ass
        icons = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
        for icon in icons:
            for suit in suits:
                # create the tuple card list and nobody can see them
                self.concealed_cards.append((suit, icon))

    def set_card_visible(self, suit, icon):
        if (suit, icon) in self.concealed_cards:
            self.table_open_cards.append((suit, icon))
            self.concealed_cards.remove((suit, icon))

    def get_main_player_visible_cards(self):
        return self.get_main_player_cards() + self.get_table_open_cards()

    def add_main_player_card(self, suit, icon):
        if (suit, icon) in self.concealed_cards:
            self.main_player_cards.append((suit, icon))
            self.concealed_cards.remove((suit, icon))

    def set_main_player_cards(self, cards):
        self.main_player_cards = cards

    def remove_opponent_player_cards(self):
        cards = list(self.get_main_player_cards())
        for card in cards:
            self.concealed_cards.append(card)
        self.main_player_cards = []
        return cards

    def remove_open_table_cards(self):
        cards = list(self.get_table_open_cards())
        for card in cards:
            self.concealed_cards.append(card)
        self.table_open_cards = []

    def save_original_main_player_cards(self):
        cards = list(self.get_main_player_cards())
        self.main_player_cards = []
        return cards

    def get_main_player_cards(self):
        return self.main_player_cards

    def get_table_open_cards(self):
        return self.table_open_cards

    def get_number_of_main_player_cards(self):
        return len(self.main_player_cards)

    def get_number_of_open_cards(self):
        return len(self.table_open_cards)

    def get_number_of_concealed_cards(self):
        return len(self.concealed_cards)

    def get_concealed_cards(self):
        return self.concealed_cards

    def burn_one_card(self, card):
        if card in self.concealed_cards:
            self.burned_cards.append(card)
            self.concealed_cards.remove(card)
        else:
            print('Burn card is not in concealed cards!')

    def remove_burned_cards(self):
        for card in self.burned_cards:
            self.concealed_cards.append(card)
        self.burned_cards = []
