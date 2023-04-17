import pygame
from characters import Beavis, Butthead

### Инициация класса комнаты Бивиса и Баттхеда"""
class Room:
    def __init__(self, screen, background_image) -> None:
        self.screen = screen
        self.background_image = pygame.image.load(background_image)
        self.beavis = Beavis(100, 100)
        self.butthead = Butthead(200, 200)

        # координаты персонажей
        self.beavis_x = 100
        self.beavis_y = 100
        self.butthead_x = 100
        self.butthead_y = 100

        # размеры персонажей в локации
        self.player_width = 50
        self.player_height = 50

        # цвет персонажей (!ЗАМЕНИТЬ НА АНИМАЦИИ!)
        self.beavis_color = (100, 100, 100)
        self.butthead_color = (150, 150, 150)

    def display(self):
        # Отображение фона комнаты
        self.screen.blit(self.background_image, (0, 0))

        # Отображение персонажей
        self.beavis.draw(self.screen)
        self.butthead.draw(self.screen)
    def update(self):
        # Обновление персонажей(пока не используется)
        pass


