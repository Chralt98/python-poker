import rankings
import possibility
from game import Game


game = Game()


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
    game.distribute_cards([('C', 'A'), ('H', 'Q')])
    game.flop_cards(('D', 'K'), ('H', '3'), ('S', '2'), ('D', '8'), ('J', 'S'))

    print_poker()
