

class Player:
    def __init__(self, starting_tiles):
        self.tiles = starting_tiles

    def play(self, board):
        pass

    def play_first_tile(self, board):
        print(self.tiles)
        pass

    def finish(self):
        return len(self.tiles) == 0


