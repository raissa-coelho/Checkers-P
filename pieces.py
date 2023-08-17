import pygame
from constants import SQUARE, GOLD, CROWN

class Piece:
    PAD = 10
    BORDER = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.queen = False
        self.x = 0
        self.y = 0
        self.cal_pos()
    
    def cal_pos(self):
        self.x = SQUARE * self.col + SQUARE//2
        self.y = SQUARE * self.row + SQUARE//2
    
    def make_QUEEN(self):
        self.queen = True
    
    def draw(self, win):
        radius =  SQUARE//2 - self.PAD
        pygame.draw.circle(win, GOLD, (self.x, self.y), radius+self.BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y),radius)
        if self.queen:
            win.blit(CROWN, (self.x-CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.cal_pos()
    
    def __repr__(self):
        return str(self.color)