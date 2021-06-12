from tkinter import *
import colors as c
import random
import game_functions

border_edge = 10
width = 700
height = 700


class Game(Frame):
    matrix = [[0] * 4 for x in range(4)]

    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')

        self.cells = []

        src_width = self.winfo_screenwidth()
        src_height = self.winfo_screenheight()
        x = (src_width / 2) - (width / 2)
        y = (src_height / 2) - (height / 2)
        self.master.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        def right(event):
            game_functions.right_stack(self.matrix)
            self.update_gui()

        self.master.bind("<Right>", right)

        self.build_gui()
        self.draw_initial_squares()

        self.master.resizable(False, False)
        self.mainloop()

    # builds base board
    def build_gui(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR, width=width, height=height)
        background.pack()

        # self.bind("<Left>", game_functions.right_stack(self.matrix))
        # background.bind("<Right>", right)
        # background.bind("<Up>", up)
        # background.bind("<Down>", down)

        game_background = Frame(background, bg=c.GAME_BACKGROUND_COLOR)
        game_background.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.09)

        row_num = 0
        col_num = 0
        tile_size = (width - (border_edge * 6)) / 5 - 0.75

        for x in range(4):
            row_insert = []
            for y in range(4):
                pad_x_value = border_edge
                pad_y_value = border_edge

                if y > 0:
                    pad_y_value = (0, border_edge)

                if x > 0:
                    pad_x_value = (0, border_edge)

                cell = Frame(game_background, bg=c.EMPTY_TILE_COLOR, width=tile_size, height=tile_size)
                cell.grid(row=row_num, column=col_num, padx=pad_x_value, pady=pad_y_value)
                cell_number = Label(game_background, bg=c.EMPTY_TILE_COLOR, justify=CENTER, text="")
                cell_number.grid(row=row_num, column=col_num, padx=pad_x_value, pady=pad_y_value)
                cell_data = {'frame': cell, 'number': cell_number}
                row_insert.append(cell_data)

                row_num += 1
                if row_num % 4 == 0:
                    col_num += 1
                    row_num = 0
            self.cells.append(row_insert)

    def draw_initial_squares(self):
        for i in range(2):
            if random.random() < 0.9:
                value = 2
            else:
                value = 4
            row = random.randint(0, 3)
            col = random.randint(0, 3)

            while self.matrix[row][col] != 0:
                row = random.randint(0, 3)
                col = random.randint(0, 3)

            self.matrix[row][col] = value

            self.cells[col][row]["frame"].configure(bg=c.TILE_COLORS[value])
            self.cells[col][row]["number"].configure(bg=c.TILE_COLORS[value],
                                                     text=str(value),
                                                     font=c.LABEL_FONT,
                                                     fg=c.LABEL_COLORS)
        self.update_gui()

    def update_gui(self):
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    self.cells[j][i]["frame"].configure(bg=c.EMPTY_TILE_COLOR)
                    self.cells[j][i]["number"].configure(bg=c.EMPTY_TILE_COLOR,
                                                         text="")
                else:
                    self.cells[j][i]["frame"].configure(bg=c.TILE_COLORS[self.matrix[i][j]])
                    self.cells[j][i]["number"].configure(bg=c.TILE_COLORS[self.matrix[i][j]],
                                                         text=str(self.matrix[i][j]),
                                                         font=c.LABEL_FONT,
                                                         fg=c.LABEL_COLORS)


Game()
