from deck import Deck
from collections import Counter


class Rankings(Deck):
    straight = []

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
                return True, 'Pair of ' + str(c[0]) + ' !'
        return False,

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
        if i == 2:
            return True, 'Two Pairs ' + str(pairs[0]) + ' and ' + str(pairs[1]) + ' !'
        else:
            return False,

    def get_three_of_a_kind(self):
        icons = []
        for card in self.get_main_player_visible_cards():
            icons.append(card[1])
        counter = Counter(icons)
        for c in counter.items():
            if c[1] == 3:
                return True, 'Three of a kind ' + str(c[0]) + ' !'
        return False,

    def get_straight(self):
        cards = [(i[0], self.get_card_weight(i)) for i in self.get_main_player_visible_cards()]
        cards = sorted(cards, key=lambda tup: tup[1])
        straight = [cards[0]]
        i = 1
        while i < len(cards):
            if cards[i][1] - self.get_card_weight(straight[-1]) <= 1:
                straight.append((cards[i][0], self.get_card_out_of_weight(cards[i][1])))
                i += 1
            else:
                straight.clear()
                straight.append((cards[i][0], self.get_card_out_of_weight(cards[i][1])))
                i += 1
        straight_icons = [self.get_card_weight(i) for i in straight]
        if len(set(straight_icons)) >= 5:
            self.straight = straight
            return True, 'Straight ' + str(self.straight) + ' !'
        else:
            return False,

    def get_flush(self):
        suits = []
        for card in self.get_main_player_visible_cards():
            suits.append(card[0])
        counter = Counter(suits)
        for c in counter.items():
            if c[1] >= 5:
                return True, 'Flush ' + str(suits) + ' !'
        return False,

    def get_full_house(self):
        if self.get_three_of_a_kind()[0] and self.get_pair()[0]:
            return True, 'Full House ' + str(self.get_main_player_visible_cards()) + ' !'
        else:
            return False,

    def get_four_of_a_kind(self):
        icons = []
        for card in self.get_main_player_visible_cards():
            icons.append(card[1])
        counter = Counter(icons)
        for c in counter.items():
            if c[1] == 4:
                return True, 'Four of a kind ' + str(c[0]) + ' !'
        return False,

    def get_straight_flush(self):
        self.get_straight()
        suits = []
        for card in self.straight:
            suits.append(card[0])
        counter = Counter(suits)
        for c in counter.items():
            if c[1] >= 5:
                return True, 'Straight Flush ' + str(self.get_main_player_visible_cards()) + ' !'
        return False,

    def get_royal_flush(self):
        self.get_straight()
        if self.get_straight_flush()[0] and 'A' in [s[1] for s in self.straight]:
            return True, 'Royal Flush ' + str(self.get_main_player_visible_cards()) + ' !'
        else:
            return False,

    @staticmethod
    def get_card_weight(card):
        if card[1] is '2':
            weight = 2
        elif card[1] is '3':
            weight = 3
        elif card[1] is '4':
            weight = 4
        elif card[1] is '5':
            weight = 5
        elif card[1] is '6':
            weight = 6
        elif card[1] is '7':
            weight = 7
        elif card[1] is '8':
            weight = 8
        elif card[1] is '9':
            weight = 9
        elif card[1] is '10':
            weight = 10
        elif card[1] is 'J':
            weight = 11
        elif card[1] is 'Q':
            weight = 12
        elif card[1] is 'K':
            weight = 13
        elif card[1] is 'A':
            weight = 14
        else:
            weight = 0
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
        if self.get_royal_flush()[0]:
            # print()
            # print('--royal-flush------')
            # print(self.get_royal_flush()[1])
            return 0
        elif self.get_straight_flush()[0]:
            # print()
            # print('--straight-flush---')
            # print(self.get_straight_flush()[1])
            return 1
        elif self.get_four_of_a_kind()[0]:
            # print()
            # print('--four-of-a-kind--')
            # print(self.get_four_of_a_kind()[1])
            return 2
        elif self.get_full_house()[0]:
            # print()
            # print('---full-house----')
            # print(self.get_full_house()[1])
            return 3
        elif self.get_flush()[0]:
            # print()
            # print('------flush------')
            # print(self.get_flush()[1])
            return 4
        elif self.get_straight()[0]:
            # print()
            # print('-----straight----')
            # print(self.get_straight()[1])
            return 5
        elif self.get_three_of_a_kind()[0]:
            # print()
            # print('-three-of-a-kind-')
            # print(self.get_three_of_a_kind()[1])
            return 6
        elif self.get_two_pairs()[0]:
            # print()
            # print('----two-pairs---')
            # print(self.get_two_pairs()[1])
            return 7
        elif self.get_pair()[0]:
            # print()
            # print('----one-pair----')
            # print(self.get_pair()[1])
            return 8
        else:
            # print()
            # print('Highest card ' + str(self.get_high_card()[1]) + ' !')
            return 9
