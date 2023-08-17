from board import Board
from constants import BROWN, WHITE, BLUE, SQUARE
import pygame

class Game:

    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BROWN
        self.valid_moves = {}
    
    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_move(self.valid_moves)
        pygame.display.update()
    
    def _move(self, row, col):
        piece = self.board.get_piece(row,col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row,col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BROWN:
            self.turn = WHITE
        else:
            self.turn = BROWN

    def select(self, row, col):
        if self.selected:
            r = self._move(row,col)
            if not r:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row,col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        
        return False
    
    def draw_valid_move(self, move):
        for mo in move:
            row, col = mo
            pygame.draw.circle(self.win, BLUE, (col*SQUARE+SQUARE//2, row*SQUARE+SQUARE//2), 15)