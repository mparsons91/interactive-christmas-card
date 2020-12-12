import pygame
from spritesheet import Spritesheet


class Tree(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_tree()
        self.rect = self.tree_frames[0].get_rect()
        self.rect.midbottom = (60, 270)
        self.current_frame = 0
        self.last_updated = 0
        self.current_frame = 0
        self.current_image = self.tree_frames[0]

    def draw(self, display):
        display.blit(self.current_image, self.rect)


    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_updated > 600:
            self.last_updated = now
            self.current_frame = (self.current_frame + 1) % len(self.tree_frames)
            self.current_image = self.tree_frames[self.current_frame]

    def load_tree(self):
        my_spritesheet = Spritesheet('tree_sheet.png')
        # pygame.image.Load('my_image_name.png').convert()
        self.tree_frames = [my_spritesheet.parse_sprite('tree1.png'), my_spritesheet.parse_sprite('tree2.png'),
                            my_spritesheet.parse_sprite('tree3.png'), my_spritesheet.parse_sprite('tree4.png'),
                            my_spritesheet.parse_sprite('tree5.png'), my_spritesheet.parse_sprite('tree6.png')]