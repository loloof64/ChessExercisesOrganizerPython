import cairosvg
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import PhotoImage

class ChessImages():
    def __init__(self, size=50):
        self._size = size
        self._build_pieces()

    def get_image(self, type):
        return self._pieces[type]

    
    def _build_pieces(self):
        refs = [
            'pl', 'nl', 'bl', 'rl', 'ql', 'kl',
            'pd', 'nd', 'bd', 'rd', 'qd', 'kd',
        ]
        pieces = dict([])

        for ref in refs:
            path = "chess_vectors/Chess_{}t45.svg".format(ref)
            piece_data = cairosvg.svg2png(
                url=path,
                scale=self._size/45.0
            )
            img = Image.open(BytesIO(piece_data))
            pieces[ref] = ImageTk.PhotoImage(img)

        self._pieces = pieces
