class Enemies(object):
    walkRight = ['pygame.image.load('')']
    walkLeft = ['pygame.image.load('')']

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.velocity = 2

    def move(self):
        if self.velocity > 0:
            if self.x < self.path[1] + self.velocity:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.x += self.velocity
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.velocity:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.x += self.velocity
                self.walkCount = 0

    def draw(self, display):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.velocity > 0:
            display.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            display.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1