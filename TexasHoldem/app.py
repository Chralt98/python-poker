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
    print('Hand Rank => Your Rank: ' + str(ranking.recognize_hand_ranking()) + ' !')
    print('------------------------------------OPPONENT-POSSIBILITIES-------------------------------------------------')
    counts = possibility.Possibility()
    counts.get_hand_ranking_counts()
    print('-----------------------------------------------------------------------------------------------------------')


if __name__ == '__main__':
    # Diamonds ('D'), Clubs ('C') Kreuz, Hearts ('H'), Spades ('S') Piek
    # Jack ('J'), Queen ('Q'), King ('K'), Ass ('A')
    # TODO ('SUIT', 'ICON')
    game.distribute_cards([('S', '6'), ('S', '5')])
    game.flop_cards(('H', '2'), ('H', '3'), ('D', '6'), ('C', 'K'), ('S', '4'))

    print_poker()
