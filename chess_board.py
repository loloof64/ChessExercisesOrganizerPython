# coding: utf-8
 
from tkinter import Canvas, ALL

class ChessBoard(Canvas):
    def __init__(self, parent=None, cells_size=50):
        self._cells_size = cells_size
        self._board_size = cells_size * 9
        Canvas.__init__(self, parent, width=self._board_size, height=self._board_size, background="#44EE66")
        self._canvas_elements = []
        self._paint()

    def _paint(self):
        self._erase_canvas()
        for row in range(0,8):
            for col in range(0,8):
                is_white_cell = (col+row) % 2 == 0
                if is_white_cell:
                    color = "#ffce9e"
                else:
                    color = "#d18b47"
                x1 = self._cells_size * (col + 0.5)
                y1 = self._cells_size * (row + 0.5)
                x2 = self._cells_size * (col + 1.5)
                y2 = self._cells_size * (row + 1.5)
                self._canvas_elements.append(self.create_rectangle(x1, y1, x2, y2, fill=color))

    def _erase_canvas(self):
        self.delete(ALL)