import pygame
from spritesheet import Spritesheet


class Christmas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_christmas()
        self.rect = self.christmas_frames[0].get_rect()
        self.rect.midbottom = (100, 80)
        self.current_frame = 0
        self.last_updated = 0
        self.current_frame = 0
        self.current_image = self.christmas_frames[0]

    def draw(self, display):
        display.blit(self.current_image, self.rect)


    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_updated > 400:
            self.last_updated = now
            self.current_frame = (self.current_frame + 1) % len(self.christmas_frames)
            self.current_image = self.christmas_frames[self.current_frame]

    def load_christmas(self):
        my_spritesheet = Spritesheet('christmas_text_sprite.png')
        # pygame.image.Load('my_image_name.png').convert()
        self.christmas_frames = [my_spritesheet.parse_sprite('christmastext1.png'),
                                 my_spritesheet.parse_sprite('christmastext2.png'),
                                 my_spritesheet.parse_sprite('christmastext3.png')]
