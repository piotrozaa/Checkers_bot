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




    
def pretty_print_moves(move):
    to_print = "["
    for m in move:
        to_print += str(m.x) + ", " + str(m.y)
    to_print += "]"
    print(to_print)




def Min_max(state, depth,max_depth):
    if depth == max_depth:
        return Evaluation(state)
    value = 0
    list=state.PossibleMoves()
    for move in list:
        """if(depth%2==1):
            value = max(value,Min_max(state.make_move(move).copy(), depth + 1, max_depth))
        else:
            value=min(value,Min_max(state.make_move(move).copy(), depth + 1, max_depth))"""
#         if state.isBlack(Position(2, 2)) and state.isWhite(Position(3, 3)):
#         print("in minmax: ")
#        pretty_print_moves(move)

        new_board = state.make_move(move)
        value = max(value, 1-Min_max(new_board, depth + 1, max_depth))
    return value


class MinMaxBot():
    def make_move(self,board):
        value=-1
        for move in board.PossibleMoves():
            if Min_max(board.make_move(move),1,4)>value:
                return_move=move
        return return_move

