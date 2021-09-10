import math

from PIL import Image, ImageColor
import IPython.display

from Position import Position
from Piece import Piece
from Board import Board
from Game import Game


def Evaluation(board):
    numberOfWhites = len(board.whites)
    numberOfBlacks = len(board.blacks)
    for piece in board.whites:
        if (piece.king):
            numberOfWhites += 4

    for piece in board.blacks:
        if (piece.king):
            numberOfBlacks += 4

    totalPieces = numberOfBlacks + numberOfWhites
    return numberOfWhites / totalPieces

max_depth=3

"""def PossibleMoves(Board):
    list=[]
    if (Board.capture_possible()):
        for white in Board.whites:
            if not white.king:
                for i in [-1, 1]:
                    if Board.isBlack(white.position().add(1, i)):
                        if Board.isEmpty(white.position().add(2, 2*i)):
                            list.append(white.position(),white.position.add(2,2*i))
            else:
                for xi in [-1, 1]:
                    for yi in [-1, 1]:
                        where = white.position().add(yi, xi)
                        # Go in that direction, until an occuppied field is found or we reach the end of the board
                        while (Board.isEmpty(where)):
                            where = where.add(yi, xi)
                        if Board.isBlack(where) and Board.isEmpty(where.add(yi, xi)):
                            list.append(white.position(),where.add(yi, xi))
                            where = where.add(yi, xi)
                            where = where.add(yi, xi)
                            while(Board.isEmpty((where))):
                                list.append(white.position(), where)
                                where = where.add(yi, xi)

    else:
        for a in Board.whites:
            a.position()
            for i in [-1,1]:
                if(Board.isEmpty(a.position.add(1,i))):
                    list.append(a.position(),a.position.add(1,i))"""








def Min_max(state, depth,max_depth):
    if(depth==0):
        return state
    if depth == max_depth:
        return Evaluation(state)
    value = 0
    list=state.PossibleMoves()
    for move in list:
        value = max(value, 1 - Min_max(state, depth + 1, max_depth))
    return value


class MinMaxBot():
    def make_move(self,board):
        value=0
        for move in board.PossibleMoves():
            if Min_max(board.make_move(move),1,3)>value:
                return_move=move
        return return_move

