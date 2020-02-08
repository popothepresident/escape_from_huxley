"""Import pygame module."""
import pygame as pg


class Player(object):
    """Player object."""

    def __init__(self, x, y, width, height, weapon):
        """Construct."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.weapon = weapon
        # set player's speed
        self.velocity = 4
        self.floor = False
        self.isJump = False
        self.gravity = 10
        self.jumpCount = self.gravity

    def draw(self, display, image):
        """Draw the player."""
        display.blit(image, (self.x, self.y))

    def setVelocity(self, velocity):
        """Set the velocity of the player."""
        self.velocity = velocity

    def moveLeft(self):
        """Move the player left."""
        if self.x > 0:
            self.x -= self.velocity

    def moveRight(self, max):
        """Move the player right."""
        if self.x + self.width < max:
            self.x += self.velocity

    def setFloor(self, floor):
        """Set floor to true or false"""
        self.floor = floor

    def fall(self, max, gravity):
        """Make the player fall."""
        if not self.floor:
            self.y += 10

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -self.gravity:
                if self.jumpCount < 0: #going downwards
                    if not(self.floor):
                        self.y -= (self.jumpCount ** 2) * 0.5 * -1
                    else: #reset stuff if hits floor
                        self.isJump = False
                        self.jumpCount = 10
                else: ## going upwards
                    self.y -= (self.jumpCount ** 2) * 0.5 * 1
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
        else:
            self.isJump = True
            #right, left walkcount sets