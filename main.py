from resources.game import Game
from tkinter import *
from collections import namedtuple

Rect = namedtuple('Rect', 'x0, y0, x1, y1')
game = Game()
game.create_deck()

hand_ranking_names = {0: 'royal flush', 1: 'straight flush', 2: 'four of a kind', 3: 'full house', 4: 'flush',
                      5: 'straight', 6: 'three of a kind', 7: 'two pair', 8: 'one pair', 9: 'high card'}


def print_poker():
    print()
    print('---------TEXAS-HOLDEM-POKER--------')
    print()
    print('Main player cards: ' + str(game.get_main_player_cards()))
    print('Table open cards: ' + str(game.get_table_open_cards()))
    print('Hand Rank => Your Rank: ' + str(game.recognize_hand_ranking()) + ', ' + str(
        hand_ranking_names[game.recognize_hand_ranking()]).upper() + ' !')
    print('Your pre flop rank (1 is best and 10 is worst): ' + str(game.pre_flop_hand_analyze()))
    print('------OPPONENT-POSSIBILITIES-------')
    game.get_hand_ranking_counts()
    print('-----------------------------------')


def new_print():
    print()
    print('###################################')
    print('############# NEXT ################')
    print('###################################')


class ImageMapper(object):
    def __init__(self, image, img_rects):
        self.width, self.height = image.width(), image.height()
        self.img_rects = img_rects

    def find_rect(self, x, y):
        for i, r in enumerate(self.img_rects):
            if (r.x0 <= x <= r.x1) and (r.y0 <= y <= r.y1):
                return i, r.x0, r.x1, r.y0, r.y1
        return None


class Window(Frame):
    selected_cards = []
    canvas_rectangles = []
    burned_cards = []
    canvas_burned_rectangles = []
    colors = {0: 'LightGreen', 1: 'LightGreen', 2: 'red', 3: 'red', 4: 'red', 5: 'red', 6: 'red', 7: 'lightgrey'}
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
        self.msg = Message(self, textvariable=self.msg_text, width=640, bg='lightgrey')
        self.msg.grid(row=0, column=0)

        self.quit_button = Button(self, text='CLEAR', command=self.clear_selected_card, fg='white', bg='grey')
        self.quit_button.grid(row=1, column=0)

        self.canvas = Canvas(bg='grey', height=(4 * 76.75), width=(13 * 49.231))
        self.picture = PhotoImage(file='resources/card_deck.png')
        img_rects = []
        for y in range(4):
            for x in range(13):
                x0 = x * 49.231
                y0 = y * 76.75
                img_rects.append(Rect(x0, y0, x0 + 49.231, y0 + 76.75))
        self.image_mapper = ImageMapper(self.picture, img_rects)

        self.canvas.create_image(0, 0, image=self.picture, anchor=NW)
        self.canvas.bind('<Button-1>', self.image_click)
        self.canvas.bind("<Button-3>", self.right_click)
        self.canvas.grid(row=2, column=0)

    def right_click(self, event):
        x0 = self.image_mapper.find_rect(event.x, event.y)[1]
        x1 = self.image_mapper.find_rect(event.x, event.y)[2]
        y0 = self.image_mapper.find_rect(event.x, event.y)[3]
        y1 = self.image_mapper.find_rect(event.x, event.y)[4]
        hit = self.image_mapper.find_rect(event.x, event.y)[0]
        card = self.cards[hit]
        if card in self.burned_cards or card in self.selected_cards:
            return
        game.burn_card(card)
        self.burned_cards.append(card)
        self.canvas_burned_rectangles.append(self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.colors[7]))
        if len(self.selected_cards) >= 2:
            print_poker()

    def image_click(self, event):
        hit = self.image_mapper.find_rect(event.x, event.y)[0]
        hit = self.cards[hit]
        # avoid double selection
        if hit in self.selected_cards or hit in self.burned_cards:
            return
        self.selected_cards.append(hit)
        if len(self.selected_cards) == 2:
            new_print()
            game.distribute_cards(self.selected_cards)
            print_poker()
            self.msg_text.set('{} selected.'.format('Cards {}'.format(self.selected_cards)))
            if game.pre_flop_hand_analyze() < 8:
                print('Good pre flop hand. You should play!')
            else:
                print('Not a good idea to play with this pre flop hand. Bluff or fold!')
        elif len(self.selected_cards) == 5:
            new_print()
            game.flop_cards(self.selected_cards[2], self.selected_cards[3], self.selected_cards[4])
            self.msg_text.set('{} selected.'.format('Cards {}'.format(self.selected_cards)))
            print_poker()
            game.get_main_player_hand_ranking_probability(2)
        elif len(self.selected_cards) == 6:
            new_print()
            game.flop_cards(self.selected_cards[2], self.selected_cards[3],
                            self.selected_cards[4], self.selected_cards[5])
            self.msg_text.set('{} selected.'.format('Cards {}'.format(self.selected_cards)))
            print_poker()
            game.get_main_player_hand_ranking_probability(1)
        elif len(self.selected_cards) == 7:
            new_print()
            game.flop_cards(self.selected_cards[2], self.selected_cards[3],
                            self.selected_cards[4], self.selected_cards[5], self.selected_cards[6])
            self.msg_text.set('{} selected.'.format('Cards {}'.format(self.selected_cards)))
            print_poker()
        elif len(self.selected_cards) > 7:
            self.start_new_round()
            self.msg_text.set('{} selected.'.format('Cards {}'.format(self.selected_cards)))
            return
        x0 = self.image_mapper.find_rect(event.x, event.y)[1]
        x1 = self.image_mapper.find_rect(event.x, event.y)[2]
        y0 = self.image_mapper.find_rect(event.x, event.y)[3]
        y1 = self.image_mapper.find_rect(event.x, event.y)[4]
        self.canvas_rectangles.append(
            self.canvas.create_rectangle(x0, y0, x1, y1, outline=self.colors[len(self.selected_cards) - 1],
                                         fill='', width=5))

    def clear_selected_card(self):
        self.start_new_round()
        self.msg_text.set('{} selected.'
                          .format('nothing' if self.selected_cards is None else 'Cards {}'.format(self.selected_cards)))

    def start_new_round(self):
        for r in self.canvas_rectangles:
            self.canvas.delete(r)
        for b in self.canvas_burned_rectangles:
            self.canvas.delete(b)
        game.reset()
        self.selected_cards = []
        self.canvas_burned_rectangles = []
        self.burned_cards = []
        new_print()


# Diamonds ('D'), Clubs ('C') Kreuz, Hearts ('H'), Spades ('S') Piek
# Jack ('J'), Queen ('Q'), King ('K'), Ass ('A')
# TODO ('SUIT', 'ICON')
# game.distribute_cards([('C', 'J'), ('D', '10')])
# game.flop_cards(('D', '8'), ('S', 'K'), ('H', 'A'), ('D', 'Q'))
# This creates the main window of an application
root = Tk()
app = Window(root)
root.title("Poker Possibilities")
root.geometry("640x400")
root.configure(background='lightgrey')
# Start the GUI
root.mainloop()
