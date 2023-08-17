import  pygame
from constants import BROWN, WIDTH, HEIGHT, SQUARE
from game import Game
from net_server import Network

win = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("Client - Checkers")

def get_position_mouse(pos):
    x, y = pos
    row = y//SQUARE
    col = x//SQUARE
    return row, col

def main():
    run = True
    n = Network()
    startpos = n.getPlayer()

    clock = pygame.time.Clock()
    game = Game(win)

    while run:
        clock.tick(60)

        if game.winner() != None:
            print(game.winner())
            run = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_position_mouse(pos)
                game.select(row,col)

        game.update()
    pygame.quit()

if __name__ == "__main__":
    main() 