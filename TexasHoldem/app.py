import rankings
import possibility
from game import Game

NUMBER_OF_PLAYERS = 9

game = Game(NUMBER_OF_PLAYERS)


def print_poker():
    print()
    print('-----------------------------------------TEXAS-HOLDEM-POKER------------------------------------------------')
    print()
    print('Main player cards: ' + str(game.get_main_player_cards()))
    print('Table open cards: ' + str(game.get_table_open_cards()))
    ranking = rankings.Rankings()
    print('Hand Rank (0 is Royal Flush) => Your Rank: ' + str(ranking.recognize_hand_ranking()) + ' !')
    print('---------------------------------------------COUNTS--------------------------------------------------------')
    counts = possibility.Possibility()
    counts.get_hand_ranking_counts()


if __name__ == '__main__':
    # Diamonds ('D'), Clubs ('C'), Hearts ('H'), Spades ('S')
    # Jack ('J'), Queen ('Q'), King ('K'), Ass ('A')
    # TODO ('SUIT', 'ICON')
    game.distribute_cards([('D', '7'), ('H', '8')])
    game.flop_cards(('H', 'J'), ('D', '6'), ('C', '8'), ('S', '3'), ('S', '2'))

    print_poker()
