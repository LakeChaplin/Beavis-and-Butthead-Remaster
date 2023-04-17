import pygame
from characters import Beavis, Butthead
from levels_geometry import Platform

### Инициация класса комнаты Бивиса и Баттхеда"""
class Room:
    def __init__(self, screen, background_image) -> None:
        self.screen = screen
        self.background_image = pygame.image.load(background_image)
        self.beavis = Beavis(100, 100)
        self.butthead = Butthead(200, 200)
        
        # Создание геометрии пола в комнате (пока только пола) 
        self.platforms = [
            Platform(0, 500, 1280, 20, (255, 255, 255))
        ]

    def display(self):
        # Отображение фона комнаты
        self.screen.blit(self.background_image, (0, 0))

        # Отображение платформы 
        for platform in self.platforms:
            platform.draw(self.screen)

        # Отображение персонажей
        self.beavis.draw(self.screen)
        self.butthead.draw(self.screen)


