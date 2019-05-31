import possibility
from game import Game
from tkinter import *
from collections import namedtuple

Rect = namedtuple('Rect', 'x0, y0, x1, y1')
game = Game()
game.create_deck()


def print_poker():
    print()
    print('-----------------------------------------TEXAS-HOLDEM-POKER------------------------------------------------')
    print()
    print('Main player cards: ' + str(game.get_main_player_cards()))
    print('Table open cards: ' + str(game.get_table_open_cards()))
    counts = possibility.Possibility()
    print('Hand Rank => Your Rank: ' + str(counts.recognize_hand_ranking()) + ' !')
    print('------------------------------------OPPONENT-POSSIBILITIES-------------------------------------------------')
    counts.get_hand_ranking_counts()
    print('-----------------------------------------------------------------------------------------------------------')


class ImageMapper(object):
    def __init__(self, image, img_rects):
        self.width, self.height = image.width(), image.height()
        self.img_rects = img_rects

    def find_rect(self, x, y):
        for i, r in enumerate(self.img_rects):
            if (r.x0 <= x <= r.x1) and (r.y0 <= y <= r.y1):
                return i
        return None


class Window(Frame):
    selected_cards = []
    cards = {0: ('C', 'A'), 1: ('C', '2'), 2: ('C', '3'), 3: ('C', '4'), 4: ('C', '5'), 5: ('C', '6'),
             6: ('C', '7'), 7: ('C', '8'), 8: ('C', '9'), 9: ('C', '10'), 10: ('C', 'J'), 11: ('C', 'Q'),
             12: ('C', 'K'), 13: ('D', 'A'), 14: ('D', '2'), 15: ('D', '3'), 16: ('D', '4'), 17: ('D', '5'),
             18: ('D', '6'), 19: ('D', '7'), 20: ('D', '8'), 21: ('D', '9'), 22: ('D', '10'), 23: ('D', 'J'),
             24: ('D', 'Q'), 25: ('D', 'K'), 26: ('H', 'A'), 27: ('H', '2'), 28: ('H', '3'), 29: ('H', '4'),
             30: ('H', '5'), 31: ('H', '6'), 32: ('H', '7'), 33: ('H', '8'), 34: ('H', '9'), 35: ('H', '10'),
             36: ('H', 'J'), 37: ('H', 'Q'), 38: ('H', 'K'), 39: ('S', 'A'), 40: ('S', '2'), 41: ('S', '3'),
             42: ('S', '4'), 43: ('S', '5'), 44: ('S', '6'), 45: ('S', '7'), 46: ('S', '8'), 47: ('S', '9'),
             48: ('S', '10'), 49: ('S', 'J'), 50: ('S', 'Q'), 51: ('S', 'K')}

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.msg_text = StringVar()
        self.msg = Message(self, textvariable=self.msg_text, width=640)
        self.msg.grid(row=0, column=0)

        self.picture = PhotoImage(file='card_deck.png')
        img_rects = []
        for y in range(4):
            for x in range(13):
                x0 = x * 49.231
                y0 = y * 76.75
                img_rects.append(Rect(x0, y0, x0 + 49.231, y0 + 76.75))
        self.image_mapper = ImageMapper(self.picture, img_rects)
        # use Label widget to display image
        self.image = Label(self, image=self.picture, borderwidth=0)
        self.image.bind('<Button-1>', self.image_click)
        self.image.grid(row=1, column=0)

        self.quit_button = Button(self, text='CLEAR', command=self.clear_selected_card)
        self.quit_button.grid(row=2, column=0)

    def image_click(self, event):
        hit = self.image_mapper.find_rect(event.x, event.y)
        hit = self.cards[hit]
        self.selected_cards.append(hit)
        if len(self.selected_cards) == 2:
            game.distribute_cards(self.selected_cards)
            print_poker()
        elif len(self.selected_cards) == 5:
            game.flop_cards(self.selected_cards[2], self.selected_cards[3], self.selected_cards[4])
            print_poker()
        elif len(self.selected_cards) == 6:
            game.flop_cards(self.selected_cards[2], self.selected_cards[3],
                            self.selected_cards[4], self.selected_cards[5])
            print_poker()
        elif len(self.selected_cards) == 7:
            game.flop_cards(self.selected_cards[2], self.selected_cards[3],
                            self.selected_cards[4], self.selected_cards[5], self.selected_cards[6])
            print_poker()
        elif len(self.selected_cards) > 7:
            self.start_new_round()
        self.msg_text.set('{} selected.'
                          .format('nothing' if self.selected_cards is None else 'Cards {}'.format(self.selected_cards)))

    def clear_selected_card(self):
        self.start_new_round()
        self.msg_text.set('{} selected.'
                          .format('nothing' if self.selected_cards is None else 'Cards {}'.format(self.selected_cards)))

    def start_new_round(self):
        game.reset_cards()
        self.selected_cards = []
        for i in range(30):
            print()


# Diamonds ('D'), Clubs ('C') Kreuz, Hearts ('H'), Spades ('S') Piek
# Jack ('J'), Queen ('Q'), King ('K'), Ass ('A')
# TODO ('SUIT', 'ICON')
# game.distribute_cards([('C', 'J'), ('D', '10')])
# game.flop_cards(('D', '8'), ('S', 'K'), ('H', 'A'), ('D', 'Q'))
# print_poker()
# This creates the main window of an application
root = Tk()
app = Window(root)
root.title("Poker Possibilities")
root.geometry("640x400")
root.configure(background='grey')
# Start the GUI
root.mainloop()
