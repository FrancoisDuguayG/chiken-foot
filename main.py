from Player import Player
from Bone import Bone
from Tile import Tile
from Board import Board


class Game:
    number_of_players = 6
    starting_hand_size = 7
    bone = Bone()
    board = Board()

    active_player = 0

    def __init__(self):
        self.players = [Player(self.bone.pick(self.starting_hand_size)) for _ in range(self.number_of_players)]

    def main(self):
        self.first_tile()
        while True:
            active_player = self.players[self.active_player]
            active_player.play(self.board)
            if active_player.finish():
                break
            self.next_player()

    def first_tile(self):
        for n in range(15, -1, -1):
            tile = Tile(n, n)
            for i, active_player in enumerate(self.players):
                # active_player = self.players[i]
                if tile in active_player.tiles:
                    active_player.play_first_tile(self.board, tile)
                    # self.active_player = (i+1) % self.number_of_players
                    self.players = self.players[i:] + self.players[0:i]
                    break
            else:
                continue
            break

    def next_player(self):
        self.active_player = (self.number_of_players + 1) % self.number_of_players


game = Game()
game.main()
# a=1
