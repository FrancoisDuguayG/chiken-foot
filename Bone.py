from Tile import Tile
from random import shuffle


class Bone:
    max = 16
    numbers = range(0, max)

    def __init__(self):
        self._tiles = [Tile(x, y) for x in self.numbers for y in range(x, self.max)]
        shuffle(self._tiles)

    def __len__(self):
        return len(self._tiles)

    def __getitem__(self, position):
        return self._tiles[position]

    def __setitem__(self, position, value):
        self._tiles[position] = value

    def __str__(self):
        return str(self._tiles)

    def __repr__(self):
        return str(self)

    def pick(self, n=1):
        picks = self._tiles[:n]
        del self._tiles[:n]
        return picks
