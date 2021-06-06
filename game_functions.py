import display as d
import colors as c
import random


def start_game():
    matrix = [[0] * 4 for x in range(4)]
    row = random.randint(0, 3)
    col = random.randint(0, 3)
    matrix[row][col] = 2
    print(matrix)
    # d.cells[row][col]["frame"].configure(bg=c.TILE_COLORS[2])
    # d.cells[row][col]["number"].configure(bg=c.TILE_COLORS[2], text="2", font=c.LABEL_FONT, fg=c.LABEL_COLORS[2])


