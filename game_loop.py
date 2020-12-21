import pygame
from spritesheet import Spritesheet
from player import Player
from tree import Tree
from christmas_text import Christmas
from mu import Mu
from wave import Wave
import sys
import os

#
# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath('.')
#
#     return os.path.join(base_path, relative_path)


#   Game window
pygame.init()
DISPLAY_W, DISPLAY_H = 480, 270
canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
running = True
clock = pygame.time.Clock()
house = pygame.image.load('house1.png').convert()

#   Load Player
cat = Player()
tree = Tree()
christmas_text = Christmas()
mu = Mu()
wave = Wave()


while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cat.LEFT_KEY, cat.FACING_LEFT = True, True
            elif event.key == pygame.K_RIGHT:
                cat.RIGHT_KEY, cat.FACING_LEFT = True, False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                cat.LEFT_KEY = False
            elif event.key == pygame.K_RIGHT:
                cat.RIGHT_KEY = False

#   animate/update sprite
    christmas_text.animate()
    mu.animate()
    wave.animate()
    tree.animate()
    cat.update()
#   Update window and display
    canvas.blit(house, (0, 0))
    mu.draw(canvas)
    wave.draw(canvas)
    tree.draw(canvas)
    cat.draw(canvas)
    christmas_text.draw(canvas)
    window.blit(canvas, (0, 0))
    pygame.display.update()
