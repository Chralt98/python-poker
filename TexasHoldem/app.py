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
    game.distribute_cards([('D', 'K'), ('C', 'K')])
    game.flop_cards(('C', 'Q'), ('C', 'J'), ('C', '10'), ('D', '10'), ('H', '10'))

    print_poker()
