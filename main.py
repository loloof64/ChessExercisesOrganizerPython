# coding: utf-8
 
from tkinter import Tk, Label, Entry, Button
from tkinter.messagebox import showinfo, showerror

from chess_board import ChessBoard

window = Tk()

chess_board = ChessBoard(window)
chess_board.pack()

window.mainloop()