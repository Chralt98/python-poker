
class Player:
    chips_value = 0
    player_id = 0
    is_small_blind = False
    is_big_blind = False

    def __init__(self, player_id, chips_value):
        self.player_id = player_id
        self.chips_value = chips_value

    def set_small_blind(self, is_small_blind):
        self.is_small_blind = is_small_blind

    def get_small_blind(self):
        return self.is_small_blind

    def set_big_blind(self, is_big_blind):
        self.is_big_blind = is_big_blind

    def get_big_blind(self):
        return self.is_big_blind

    def set_chips_value(self, number):
        self.chips_value = number

    def get_chips_value(self):
        return self.chips_value

    def get_player_id(self):
        return self.player_id

    def sub_chips_amount(self, amount):
        self.chips_value -= amount

    def add_chips_amount(self, amount):
        self.chips_value += amount
