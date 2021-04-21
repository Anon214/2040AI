from tkinter import *
import Colors as c

tile_size = 120
border_edge = 15


class Game(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.build_gui()

        self.mainloop()

    def build_gui(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR)
        background.grid()
        game_background = Frame(background, bg=c.GAME_BACKGROUND_COLOR)
        game_background.grid(padx=20, pady=20)

        row_num = 0
        col_num = 0
        for x in range(1, 17):
            pad_x_value = border_edge
            pad_y_value = (0, border_edge)

            if x > 4:
                pad_x_value = (0, border_edge)

            if x == 1 or x == 5 or x == 9 or x == 13:
                pad_y_value = border_edge

            cell = Frame(game_background, bg=c.EMPTY_TILE_COLOR, width=tile_size, height=tile_size)
            cell.grid(row=row_num, column=col_num, padx=pad_x_value, pady=pad_y_value)
            row_num += 1
            if row_num % 4 == 0:
                col_num += 1
                row_num = 0


Game()
