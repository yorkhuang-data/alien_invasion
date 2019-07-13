
import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""

        self.screen = screen

        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Store a decimal value for the ship's center.
        self.center = None
        self.center_ship()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.center[0]
        self.rect.centery = self.center[1]

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""

        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center[0] += self.ai_settings.ship_speed_factor[0]

        if self.moving_left and self.rect.left > 0:
            self.center[0] -= self.ai_settings.ship_speed_factor[0]

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center[1] += self.ai_settings.ship_speed_factor[1]

        if self.moving_up and self.rect.top > 0:
            self.center[1] -= self.ai_settings.ship_speed_factor[1]

        # Update rect object from self.center.
        self.rect.centerx = self.center[0]
        self.rect.centery = self.center[1]

    def blitme(self):
        """Draw the ship at its current location."""

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = [float(self.screen_rect.centerx), float(self.screen_rect.bottom - self.rect.height / 2.0)]

