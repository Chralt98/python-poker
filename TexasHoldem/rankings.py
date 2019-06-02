from deck import Deck
from collections import Counter


class Rankings(Deck):
    straight = []
    straight_flush = []

    def clear_straights(self):
        self.straight = []
        self.straight_flush = []

    def get_high_card(self):
        if self.get_card_weight(self.main_player_cards[0]) < self.get_card_weight(self.main_player_cards[1]):
            return self.main_player_cards[1]
        else:
            return self.main_player_cards[0]

    def get_pair(self):
        icons = []
        for card in self.get_main_player_visible_cards():
            icons.append(card[1])
        counter = Counter(icons)
        for c in counter.items():
            if c[1] == 2:
                return True
        return False

    def get_two_pairs(self):
        icons = []
        for card in self.get_main_player_visible_cards():
            icons.append(card[1])
        counter = Counter(icons)
        i = 0
        pairs = []
        for c in counter.items():
            if c[1] == 2:
                i += 1
                pairs.append(c[0])
        if i >= 2:
            return True
        else:
            return False

    def get_three_of_a_kind(self):
        icons = []
        for card in self.get_main_player_visible_cards():
            icons.append(card[1])
        counter = Counter(icons)
        for c in counter.items():
            if c[1] == 3:
                return True
        return False

    def get_straight(self):
        cards = [(i[0], self.get_card_weight(i)) for i in self.get_main_player_visible_cards()]
        cards = sorted(cards, key=lambda tup: tup[1])
        cards = [(i[0], self.get_card_out_of_weight(i[1])) for i in cards]
        straight = [cards[0]]
        i = 1
        while i < len(cards):
            if (self.get_card_weight(cards[i]) - self.get_card_weight(straight[-1])) <= 1:
                straight.append((cards[i][0], cards[i][1]))
                i += 1
            else:
                if len(straight) < 5:
                    straight.clear()
                    straight.append((cards[i][0], cards[i][1]))
                i += 1
        if set(['2', '3', '4', '5', 'A']).issubset([i[1] for i in cards]):
            straight = []
            for card in cards:
                if card[1] is ('2' or '3' or '4' or '5' or 'A' or '6' or '7'):
                    straight.append(card)
            self.straight = straight
            return True
        straight_icons = [self.get_card_weight(i) for i in straight]
        if len(set(straight_icons)) >= 5:
            self.straight = straight
            return True
        else:
            return False

    def get_flush(self):
        suits = []
        for card in self.get_main_player_visible_cards():
            suits.append(card[0])
        counter = Counter(suits)
        for c in counter.items():
            if c[1] >= 5:
                return True
        return False

    def get_full_house(self):
        icons = []
        for card in self.get_main_player_visible_cards():
            icons.append(card[1])
        counter = Counter(icons)
        pairs = 0
        three_of_a_kinds = 0
        for c in counter.items():
            if c[1] == 3:
                three_of_a_kinds += 1
            if c[1] == 2:
                pairs += 1
        if (pairs >= 1 and three_of_a_kinds == 1) or three_of_a_kinds == 2:
            return True
        return False

    def get_four_of_a_kind(self):
        icons = []
        for card in self.get_main_player_visible_cards():
            icons.append(card[1])
        counter = Counter(icons)
        for c in counter.items():
            if c[1] >= 4:
                return True
        return False

    def get_straight_flush(self):
        suits = []
        for card in self.get_main_player_visible_cards():
            suits.append(card[0])
        counter = Counter(suits)
        most_common_suit = 'placeholder'
        for c in counter.items():
            if c[1] >= 5:
                most_common_suit = str(c[0])
        if most_common_suit == 'placeholder':
            return False
        cards = []
        for card in self.get_main_player_visible_cards():
            if card[0] == most_common_suit:
                cards.append(card)
        # second straight check for suits
        cards = [(i[0], self.get_card_weight(i)) for i in cards]
        cards = sorted(cards, key=lambda tup: tup[1])
        cards = [(i[0], self.get_card_out_of_weight(i[1])) for i in cards]
        straight = [cards[0]]
        i = 1
        while i < len(cards):
            if (self.get_card_weight(cards[i]) - self.get_card_weight(straight[-1])) <= 1:
                straight.append((cards[i][0], cards[i][1]))
                i += 1
            else:
                if len(straight) < 5:
                    straight.clear()
                    straight.append((cards[i][0], cards[i][1]))
                i += 1
        if set(['2', '3', '4', '5', 'A']).issubset([i[1] for i in cards]):
            straight = []
            for card in cards:
                if card[1] is ('2' or '3' or '4' or '5' or 'A' or '6' or '7'):
                    straight.append(card)
            self.straight_flush = straight
            return True
        straight_icons = [self.get_card_weight(i) for i in straight]
        if len(set(straight_icons)) >= 5:
            self.straight_flush = straight
            return True
        else:
            return False

    def get_royal_flush(self):
        self.get_straight_flush()
        if self.get_straight_flush() and set(['A', 'K', 'Q', 'J', '10']).issubset([s[1] for s in self.straight_flush]):
            return True
        else:
            return False

    @staticmethod
    def get_card_weight(card):
        if str(card[1]) is '2':
            weight = 2
        elif str(card[1]) is '3':
            weight = 3
        elif str(card[1]) is '4':
            weight = 4
        elif str(card[1]) is '5':
            weight = 5
        elif str(card[1]) is '6':
            weight = 6
        elif str(card[1]) is '7':
            weight = 7
        elif str(card[1]) is '8':
            weight = 8
        elif str(card[1]) is '9':
            weight = 9
        elif str(card[1]) is '10':
            weight = 10
        elif str(card[1]) is 'J':
            weight = 11
        elif str(card[1]) is 'Q':
            weight = 12
        elif str(card[1]) is 'K':
            weight = 13
        elif str(card[1]) is 'A':
            weight = 14
        else:
            weight = 999
            print('No possible icon.')
        return weight

    @staticmethod
    def get_card_out_of_weight(icon):
        if icon is 2:
            weight = '2'
        elif icon is 3:
            weight = '3'
        elif icon is 4:
            weight = '4'
        elif icon is 5:
            weight = '5'
        elif icon is 6:
            weight = '6'
        elif icon is 7:
            weight = '7'
        elif icon is 8:
            weight = '8'
        elif icon is 9:
            weight = '9'
        elif icon is 10:
            weight = '10'
        elif icon is 11:
            weight = 'J'
        elif icon is 12:
            weight = 'Q'
        elif icon is 13:
            weight = 'K'
        elif icon is 14:
            weight = 'A'
        else:
            weight = '1'
            print('No possible number of card.')
        return weight

    def recognize_hand_ranking(self):
        if self.get_royal_flush():
            return 0
        elif self.get_straight_flush():
            return 1
        elif self.get_four_of_a_kind():
            return 2
        elif self.get_full_house():
            return 3
        elif self.get_flush():
            return 4
        elif self.get_straight():
            return 5
        elif self.get_three_of_a_kind():
            return 6
        elif self.get_two_pairs():
            return 7
        elif self.get_pair():
            return 8
        else:
            return 9
