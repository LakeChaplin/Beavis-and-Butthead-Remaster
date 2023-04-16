import pygame 

# инициализация pygame 
pygame.init()


# расширение по умолчанию
default_width = 1280
default_height = 720



# создание экрана 
screen = pygame.display.set_mode((default_width, default_height))

# установка заголовка экрана (название игры)
pygame.display.set_caption('Beavis and Butthead Remaster')

# установка иконки для окна игры
icon = pygame.image.load('graphic/dispaly_icon.png')
pygame.display.set_icon(icon)

# главный цикл игры
while True:
    # обработчик событий 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # нажатие кнопки закрытия окна игры
            pygame.quit()
            raise SystemExit
        

    # обнавление экрана
    pygame.display.update()            
