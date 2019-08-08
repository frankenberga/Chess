import chess
import cProfile
from ChessGame import ChessGame
from RandomAI import RandomAI
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI

def test():
    player1 = MinimaxAI(3)
    player2 = RandomAI()

    game = ChessGame(player1, player2)
    game.make_move()

cProfile.run("test()")
