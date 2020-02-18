# coding: utf-8
 
from tkinter import Tk, PhotoImage
from chess_board import ChessBoard

window = Tk()
window.resizable(False, False)
window.title("Chess Exercises Organizer")
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='knight.png'))

chess_board = ChessBoard(window, 40)

chess_board.pack()

window.mainloop()