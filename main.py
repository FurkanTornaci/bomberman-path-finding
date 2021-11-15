from typing import Counter
import pygame

from game import start

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

bg = pygame.image.load("bg.jpg")

BLACK = (5, 56, 107)
WHITE = (237, 245, 225)
HOVER_COLOR = (50, 70, 90)
FONT = pygame.font.SysFont ("Times New Norman", 20)

text0 = FONT.render("Finding the path in the maze using different path finding algorithms", True, WHITE)
text1 = FONT.render("A STAR (Shortest Path)", True, WHITE)
text2 = FONT.render("BFS", True, WHITE)
text3 = FONT.render("DFS", True, WHITE)
text4 = FONT.render("HUMAN", True, WHITE)  

rect0 = pygame.Rect(175,50,450,30)
rect1 = pygame.Rect(300,100,150,40)
rect2 = pygame.Rect(300,200,150,40)
rect3 = pygame.Rect(300,300,150,40)
rect4 = pygame.Rect(300,400,150,40)

buttons = [
    [text0, rect0, BLACK],
    [text1, rect1, BLACK],
    [text2, rect2, BLACK],
    [text3, rect3, BLACK],
    [text4, rect4, BLACK],
    ]
background_image = pygame.image.load("./images/Pixel-Art-800x600.jpg").convert()
def game_intro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEMOTION: 
                    for button in buttons:
                        if button[1].collidepoint(event.pos):
                            button[2] = HOVER_COLOR
                        else:
                            button[2] = BLACK
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    Counter = 0
                    if button[1].collidepoint(event.pos):
                        for i in range(len(buttons)):
                            if buttons[i] == button:
                                if i == 0:
                                    continue
                                algorithms = ["ASTAR", "BFS", "DFS", "HUMAN"]
                                start(algorithms[i-1],2)
                        

        screen.fill((92, 219, 149))
        screen.blit(background_image, (0, 0))

        for text, rect, color in buttons:
            pygame.draw.rect(screen, color, rect)
            screen.blit(text, rect)

        pygame.display.flip()
        clock.tick(15)


game_intro()
pygame.quit()