import pygame
import time






#def __init__():
board = [[5,3,0,0,7,0,0,0,0],
      [6,0,0,1,9,5,0,0,0],
      [0,9,8,0,0,0,0,6,0],
      [8,0,0,0,6,0,0,0,3],
      [4,0,0,8,0,3,0,0,1],
      [7,0,0,0,2,0,0,0,6],
      [0,6,0,0,0,0,2,8,0],
      [0,0,0,4,1,9,0,0,5],
      [0,0,0,0,8,0,0,7,9]]
pygame.init()
gameDisplay = pygame.display.set_mode((600, 600))  # Screen dimensions, blocks are 67x67
pygame.display.set_caption('Sudoku')
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
boardImg = pygame.image.load('Board.png')


def message_display(text, i, j):
    numberText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, numberText)
    TextRect.center = (33+(i*66), 33+(j*66)) #33 pixels is center of first block, i = column #, j = row #, 66 is pixels in a block(Display length/9 for block. Block/2 for center.)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    return


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def createBoard(puzzle):
    for i in range(0, 9):
        for j in range(0, 9):
            message_display(str(board[i][j]), j, i)
            return


def game_loop():
    crashed = False
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gameDisplay.fill(white)
        gameDisplay.blit(boardImg, (0, 0))
        createBoard(board)
        pygame.display.update()
        clock.tick(30)

game_loop()

time.sleep(20)
pygame.quit()
quit()
