import pygame
from spritesheet import Spritesheet


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, False
        self.load_frames()
        self.rect = self.idle_frames_left[0].get_rect()
        self.rect.midbottom = (240, 244)
        self.current_frame = 0
        self.last_updated = 0
        self.velocity = 0
        self.state = 'idle'
        self.current_image = self.idle_frames_left[0]

    def draw(self, display):
        display.blit(self.current_image, self.rect)

    def update(self):
        self.velocity = 0
        if self.LEFT_KEY:
            self.velocity = -2
        elif self.RIGHT_KEY:
            self.velocity = 2
        self.rect.x += self.velocity
        self.set_state()
        self.animate()

    def set_state(self):
        self.state = 'idle'
        if self.velocity > 0:
            self.state = 'moving right'
        elif self.velocity < 0:
            self.state = 'moving left'

    def animate(self):
        now = pygame.time.get_ticks()
        if self.state == 'idle':
            if now - self.last_updated > 200:
                self.last_updated = now
                self.current_frame = (self.current_frame +1) % len(self.idle_frames_left)
                if self.FACING_LEFT:
                    self.current_image = self.idle_frames_left[self.current_frame]
                elif not self.FACING_LEFT:
                    self.current_image = self.idle_frames_right[self.current_frame]
        else:
            if now - self.last_updated > 100:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames_left)
                if self.state == 'moving left':
                    self.current_image = self.walking_frames_left[self.current_frame]
                elif self.state == 'moving right':
                    self.current_image = self.walking_frames_right[self.current_frame]

    def load_frames(self):
        my_spritesheet = Spritesheet('angel_sheet.png')
        # pygame.image.Load('my_image_name.png').convert()
        self.idle_frames_left = [my_spritesheet.parse_sprite('angel_idle1.png'),
                                 my_spritesheet.parse_sprite('angel_idle2.png')]
        self.walking_frames_left = [my_spritesheet.parse_sprite('angelwalk1.png'),
                                    my_spritesheet.parse_sprite('angelwalk2.png'),
                                    my_spritesheet.parse_sprite('angelwalk3.png'),
                                    my_spritesheet.parse_sprite('angelwalk4.png'),
                                    my_spritesheet.parse_sprite('angelwalk5.png'),
                                    my_spritesheet.parse_sprite('angelwalk6.png'),
                                    my_spritesheet.parse_sprite('angelwalk7.png'),
                                    my_spritesheet.parse_sprite('angelwalk8.png')]
        self.idle_frames_right = []
        for frame in self.idle_frames_left:
            self.idle_frames_right.append(pygame.transform.flip(frame, True, False))
        self.walking_frames_right = []
        for frame in self.walking_frames_left:
            self.walking_frames_right.append(pygame.transform.flip(frame, True, False))




