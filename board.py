# coding: utf-8
 
from tkinter import Frame, Canvas

class ChessBoard(Frame):
    def __init__(self, parent=None, cells_size=50):
        self.cells_size = cells_size
        self.board_size = cells_size * 9
        Frame.__init__(self, parent, background="#44EE66", width=self.board_size, height=self.board_size)
        self.canvas = Canvas(self, width=self.board_size, height=self.board_size)