import pygame
from random import randint
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.left
        self.rect.y = self.rect.centery

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0) or (self.rect.top <= screen_rect.top) or (self.rect.bottom <= screen_rect.bottom)

    def update(self):
        """Move the alien right or left."""
        
        int=randint(-500,500)

        self.x += randint(int,int)
        self.rect.x = self.x

        self.y += randint(int,int)
        self.rect.y = self.y

        self.rect.clamp_ip(self.screen.get_rect())
        
        