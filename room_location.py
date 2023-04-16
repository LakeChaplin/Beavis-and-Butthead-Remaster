import pygame

### Инициация класса комнаты Бивиса и Баттхеда"""
class Room:
    def __init__(self, screen, background_image) -> None:
        self.screen = screen
        self.background_image = pygame.image.load('graphic/Room(alpha).png')


        # координаты персонажей
        self.beavis_x = 100
        self.beavis_y = 100
        self.butthead_x = 100
        self.butthead_y =100

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
        pygame.draw.rect(self.screen, self.beavis_color, pygame.Rect(self.beavis_x, self.beavis_y, self.player_width, self.player_height))
        pygame.draw.rect(self.screen, self.butthead_color, pygame.Rect(self.butthead_x, self.butthead_y, self.player_width, self.player_height))

    def update(self):
        # Обновление персонажей(пока не используется)
        pass


pygame.init()
screen = pygame.display.set_mode((1280, 720))
room = Room(screen, 'graphic/Room(alpha).png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    room.display()
    pygame.display.update()
