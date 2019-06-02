from rankings import Rankings
import itertools


class Possibility(Rankings):
    max_possibilities = 0
    royal_flushs = 0
    straight_flushs = 0
    four_of_a_kinds = 0
    full_houses = 0
    flushs = 0
    straights = 0
    three_of_a_kinds = 0
    two_pairs = 0
    one_pairs = 0
    high_cards = 0

    def reset_possibilities(self):
        self.max_possibilities = 0
        self.royal_flushs = 0
        self.straight_flushs = 0
        self.four_of_a_kinds = 0
        self.full_houses = 0
        self.flushs = 0
        self.straights = 0
        self.three_of_a_kinds = 0
        self.two_pairs = 0
        self.one_pairs = 0
        self.high_cards = 0

    def calculate_possibility(self, amount):
        if self.max_possibilities is 0:
            return '0 %'
        return str(100 * float(amount) / float(self.max_possibilities)) + str(' %')

    def pre_flop_hand_analyze(self):
        if self.get_main_player_cards()[0][1] is self.get_main_player_cards()[1][1]:
            # super pairs, for example two Aces
            super_pair = {'A': 1, 'K': 1, 'Q': 1, 'J': 1, '10': 2, '9': 3, '8': 4, '7': 5, '6': 6, '5': 6, '4': 7,
                          '3': 7, '2': 7}
            return super_pair[self.get_main_player_cards()[1][1]]

        tuple1 = (self.get_main_player_cards()[0][1], self.get_main_player_cards()[1][1])
        tuple2 = (self.get_main_player_cards()[1][1], self.get_main_player_cards()[0][1])

        if self.get_main_player_cards()[0][0] is self.get_main_player_cards()[1][0]:
            # same suited
            pairs = {('A', 'K'): 1, ('A', 'Q'): 2, ('Q', 'K'): 2, ('J', 'A'): 2, ('J', 'K'): 3, ('J', 'Q'): 3,
                     ('A', '10'): 3, ('K', '10'): 4, ('Q', '10'): 4, ('J', '10'): 3, ('A', '9'): 5, ('K', '9'): 6,
                     ('Q', '9'): 5, ('J', '9'): 4, ('10', '9'): 4, ('J', '8'): 6, ('10', '8'): 5, ('9', '8'): 4,
                     ('8', '7'): 5, ('7', '6'): 5, ('6', '5'): 5, ('5', '4'): 6,
                     ('A', '8'): 5, ('A', '7'): 5, ('A', '6'): 5, ('A', '5'): 5, ('A', '4'): 5, ('A', '3'): 5,
                     ('A', '2'): 5, ('K', '8'): 7, ('K', '7'): 7, ('K', '6'): 7, ('K', '5'): 7, ('K', '4'): 7,
                     ('K', '3'): 7, ('K', '2'): 7, ('Q', '8'): 7, ('J', '7'): 8, ('10', '7'): 7, ('9', '7'): 5,
                     ('9', '6'): 8, ('8', '6'): 6, ('8', '5'): 8, ('7', '5'): 7, ('7', '4'): 8, ('6', '4'): 7,
                     ('5', '3'): 8, ('4', '3'): 7, ('4', '2'): 8, ('3', '2'): 8}
            if tuple1 in pairs:
                return pairs[tuple1]
            if tuple2 in pairs:
                return pairs[tuple2]
            return 9
        else:
            # unsuited, not same suited
            pairs = {('A', 'K'): 2, ('A', 'Q'): 3, ('Q', 'K'): 4, ('J', 'A'): 4, ('J', 'K'): 5, ('J', 'Q'): 5,
                     ('A', '10'): 6, ('K', '10'): 6, ('Q', '10'): 6, ('J', '10'): 5, ('A', '9'): 8, ('K', '9'): 8,
                     ('Q', '9'): 8, ('J', '9'): 7, ('10', '9'): 7, ('J', '8'): 8, ('10', '8'): 8, ('9', '8'): 7,
                     ('8', '7'): 8, ('7', '6'): 8, ('6', '5'): 8, ('5', '4'): 8}
            if tuple1 in pairs:
                return pairs[tuple1]
            if tuple2 in pairs:
                return pairs[tuple2]
            return 10

    def get_hand_ranking_counts(self):
        i = 0
        original_main_player_cards = self.save_original_main_player_cards()
        # combinations does not symmetric pairs and not same pairs
        for card_pair in itertools.combinations(self.get_concealed_cards(), 2):
            i += 1
            self.add_main_player_card(card_pair[0][0], card_pair[0][1])
            self.add_main_player_card(card_pair[1][0], card_pair[1][1])
            typ = self.recognize_hand_ranking()
            self.recognize_typ(typ)
            self.remove_opponent_player_cards()

        self.set_main_player_cards(original_main_player_cards)
        self.max_possibilities = i
        print('Rank 0 Royal Flushs: ' + str(self.royal_flushs)
              + ', possiblity: ' + self.calculate_possibility(self.royal_flushs))
        print('Rank 1 Straight Flushs: ' + str(self.straight_flushs)
              + ', possiblity: ' + self.calculate_possibility(self.straight_flushs))
        print('Rank 2 Four of a kinds: ' + str(self.four_of_a_kinds)
              + ', possiblity: ' + self.calculate_possibility(self.four_of_a_kinds))
        print('Rank 3 Full houses: ' + str(self.full_houses)
              + ', possiblity: ' + self.calculate_possibility(self.full_houses))
        print('Rank 4 Flushs: ' + str(self.flushs)
              + ', possiblity: ' + self.calculate_possibility(self.flushs))
        print('Rank 5 Straights: ' + str(self.straights)
              + ', possiblity: ' + self.calculate_possibility(self.straights))
        print('Rank 6 Three of a kinds: ' + str(self.three_of_a_kinds)
              + ', possiblity: ' + self.calculate_possibility(self.three_of_a_kinds))
        print('Rank 7 Two Pairs: ' + str(self.two_pairs)
              + ', possiblity: ' + self.calculate_possibility(self.two_pairs))
        print('Rank 8 One Pairs: ' + str(self.one_pairs)
              + ', possiblity: ' + self.calculate_possibility(self.one_pairs))
        print('Rank 9 High Cards: ' + str(self.high_cards)
              + ', possiblity: ' + self.calculate_possibility(self.high_cards))
        print()
        print('MAX Possibilities: ' + str(self.max_possibilities))

        self.reset_possibilities()

    def recognize_typ(self, typ):
        if typ is 0:
            self.royal_flushs += 1
        elif typ is 1:
            self.straight_flushs += 1
        elif typ is 2:
            self.four_of_a_kinds += 1
        elif typ is 3:
            self.full_houses += 1
        elif typ is 4:
            self.flushs += 1
        elif typ is 5:
            self.straights += 1
        elif typ is 6:
            self.three_of_a_kinds += 1
        elif typ is 7:
            self.two_pairs += 1
        elif typ is 8:
            self.one_pairs += 1
        elif typ is 9:
            self.high_cards += 1
        else:
            print('Something is not working in possiblity.')
