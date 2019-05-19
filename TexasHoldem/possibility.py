from rankings import Rankings


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

    def calculate_possibility(self, amount):
        return str(100 * float(amount) / float(self.max_possibilities)) + str(' %')

    def get_hand_ranking_counts(self):
        i = 0
        main_player_cards = self.remove_opponent_player_cards()
        self.remove_from_concealed_cards(main_player_cards)
        for y in self.get_concealed_cards():
            for x in self.get_concealed_cards():
                i += 1
                self.add_main_player_card(x[0], x[1])
                self.add_main_player_card(y[0], y[1])
                typ = self.recognize_hand_ranking()
                self.recognize_typ(typ)
                self.remove_opponent_player_cards()
        self.set_main_player_cards(main_player_cards)
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
        print('MAX Possibilities: ' + str(i))

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
