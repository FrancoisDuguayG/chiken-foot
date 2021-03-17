from dataclasses import dataclass


@dataclass
class Tile:
    """
    >>> tile = Tile(4,5)
    >>> tile.side1
    4
    >>> tile2 = Tile(5,6)
    >>> tile3 = Tile(10,13)
    >>> tile4 = Tile(4,5)
    >>> 5 in tile
    True
    >>> tile != tile3
    True
    >>> tile == tile4
    True
    """
    side1: int
    side2: int

    def __iter__(self):
        yield self.side1
        yield self.side2

    def __contains__(self, item):
        return item in list(self)

    def __getitem__(self, item):
        if int(item) == 0:
            return self.side1
        elif int(item) == 1:
            return self.side2
        else:
            raise IndexError(item)
