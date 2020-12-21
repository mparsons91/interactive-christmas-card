import pygame
from spritesheet import Spritesheet


class Wave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_wave()
        self.rect = self.wave_frames[0].get_rect()
        self.rect.midbottom = (170, 260)
        self.current_frame = 0
        self.last_updated = 0
        self.current_frame = 0
        self.current_image = self.wave_frames[0]

    def draw(self, display):
        display.blit(self.current_image, self.rect)

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_updated > 200:
            self.last_updated = now
            self.current_frame = (self.current_frame + 1) % len(self.wave_frames)
            self.current_image = self.wave_frames[self.current_frame]

    def load_wave(self):
        my_spritesheet = Spritesheet('wave_sheet.png')
        # pygame.image.Load('my_image_name.png').convert()
        self.wave_frames = [my_spritesheet.parse_sprite('wave3.png'), my_spritesheet.parse_sprite('wave2.png'),
                            my_spritesheet.parse_sprite('wave1.png'), my_spritesheet.parse_sprite('wave2.png')]

