# coding: utf-8
 
from tkinter import Canvas, ALL
import tkinter.font as tkFont

import chess

class ChessBoard(Canvas):
    def __init__(self, parent=None, cells_size=50):
        self._cells_size = cells_size
        self._board_size = cells_size * 9
        self.logic = chess.Board()
        Canvas.__init__(self, parent, width=self._board_size, height=self._board_size, background="#44EE66")
        self._paint()

    def _paint(self):
        self._erase_canvas()
        self._paint_cells()
        self._paint_coordinates()
        self._paint_player_turn()

    def _erase_canvas(self):
        self.delete(ALL)

    def _paint_cells(self):
        for row in range(0 ,8):
            for col in range(0, 8):
                is_white_cell = (col+row) % 2 == 0
                if is_white_cell:
                    color = "#ffce9e"
                else:
                    color = "#d18b47"
                x1 = self._cells_size * (col + 0.5)
                y1 = self._cells_size * (row + 0.5)
                x2 = self._cells_size * (col + 1.5)
                y2 = self._cells_size * (row + 1.5)
                self.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    def _paint_coordinates(self):
        color = "yellow"
        font_size = int(self._cells_size * 0.3)
        font = tkFont.Font(size=font_size, weight='bold')

        for col in range(0, 8):
            UPPERCASE_A_CODE = 65
            text = "{}".format(chr(UPPERCASE_A_CODE + col))
            x = self._cells_size * (1.0 + col)
            yt = self._cells_size * 0.25
            yb = self._cells_size * 8.75
            self.create_text(x, yt, text=text, fill=color, font=font)
            self.create_text(x, yb, text=text, fill=color, font=font)

        for row in range(0, 8):
            DIGIT_1_CODE = 49
            text = "{}".format(chr(DIGIT_1_CODE + 7 - row))
            xl = self._cells_size * 0.25
            xr = self._cells_size * 8.75
            y = self._cells_size * (1.0 + row)
            self.create_text(xl, y, text=text, fill=color, font=font)
            self.create_text(xr, y, text=text, fill=color, font=font)

    def _paint_player_turn(self):
        if self.logic.turn == chess.WHITE:
            color = "white"
        else:
            color = "black"
        location_top = self._cells_size * 8.5
        location_bot = self._cells_size * 9.0
        self.create_oval(location_top, location_top, location_bot, location_bot, fill=color, outline="")
