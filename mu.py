import pygame
from spritesheet import Spritesheet


class Mu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_mu()
        self.rect = self.mu_frames[0].get_rect()
        self.rect.midbottom = (314, 82)
        self.current_frame = 0
        self.last_updated = 0
        self.current_frame = 0
        self.current_image = self.mu_frames[0]

    def draw(self, display):
        display.blit(self.current_image, self.rect)


    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_updated > 200:
            self.last_updated = now
            self.current_frame = (self.current_frame + 1) % len(self.mu_frames)
            self.current_image = self.mu_frames[self.current_frame]

    def load_mu(self):
        my_spritesheet = Spritesheet('mu_sheet.png')
        # pygame.image.Load('my_image_name.png').convert()
        self.mu_frames = [my_spritesheet.parse_sprite('Mu1.png'), my_spritesheet.parse_sprite('Mu3.png'),
                          my_spritesheet.parse_sprite('Mu6.png'), my_spritesheet.parse_sprite('Mu3.png'),
                          my_spritesheet.parse_sprite('Mu1.png'), my_spritesheet.parse_sprite('Mu4.png'),
                          my_spritesheet.parse_sprite('Mu5.png'), my_spritesheet.parse_sprite('Mu4.png'),
                          my_spritesheet.parse_sprite('Mu1.png'), my_spritesheet.parse_sprite('Mu3.png'),
                          my_spritesheet.parse_sprite('Mu6.png'), my_spritesheet.parse_sprite('Mu3.png'),
                          my_spritesheet.parse_sprite('Mu2.png'), my_spritesheet.parse_sprite('Mu4.png'),
                          my_spritesheet.parse_sprite('Mu5.png'), my_spritesheet.parse_sprite('Mu4.png')
                          ]
