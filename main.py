# coding: utf-8
 
from tkinter import Tk
from chess_board import ChessBoard

window = Tk()
window.resizable(False, False)
window.title("Chess Exercises Organizer")

chess_board = ChessBoard(window)

chess_board.pack()

window.mainloop()