# coding: utf-8
 
from tkinter import Tk
from chess_board import ChessBoard

window = Tk()

chess_board = ChessBoard(window)

chess_board.pack()

window.mainloop()