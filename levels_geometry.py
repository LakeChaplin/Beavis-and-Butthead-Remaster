import pygame 
### Создание класса геометрии ###
class Platform:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color # Тут будем менять на текстуры, но пока так.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


