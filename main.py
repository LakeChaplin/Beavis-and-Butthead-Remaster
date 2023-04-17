import pygame
import menu
from room_location import Room
from levels_geometry import Platform

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

# состояние игры
game_state = "main_menu"

# создание объекта комнаты
room = Room(screen, 'graphic/Room(alpha).png')

# кнопки управления персонажами
keys = {
    "left": False,
    "right": False,
    "up": False,
    "down": False
}

active_character = room.beavis

# главный цикл игры
while True:
    # обработчик событий
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            # нажатие кнопки закрытия окна игры
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys["left"] = True
            elif event.key == pygame.K_RIGHT:
                keys["right"] = True
            elif event.key == pygame.K_UP:
                keys["up"] = True
            elif event.key == pygame.K_DOWN:
                keys["down"] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys["left"] = False
            elif event.key == pygame.K_RIGHT:
                keys["right"] = False
            elif event.key == pygame.K_UP:
                keys["up"] = False
            elif event.key == pygame.K_DOWN:
                keys["down"] = False
            elif event.key == pygame.K_z:
                active_character.flip()
            elif event.key == pygame.K_TAB:
                if active_character == room.beavis:
                    active_character = room.butthead
                else:
                    active_character = room.beavis
            elif event.key == pygame.K_SPACE:
                active_character.jump()



    if game_state == "main_menu":
        # отображение главного меню
        next_state = menu.display_main_menu(screen, default_width, default_height, events)

        if next_state == "start_game":
            game_state = "gameplay"
    # отображение самой игры (геймплей)        
    elif game_state == "gameplay":
        dx, dy = 0, 0
        if keys["left"]:
            dx = -1
            if not active_character.fliped:
                active_character.flip()
        if keys["right"]:
            dx = 1
            if active_character.fliped:
                active_character.flip()
        if keys["up"]:
            dy = -1
        if keys["down"]:
            dy = 1
        active_character.move(dx, dy, room.platforms)
        
        active_character.update(room.platforms)
        passive_character = room.beavis if active_character == room.butthead else room.butthead
        passive_character.follow(active_character, 100, room.platforms)
        passive_character.update(room.platforms)
        
        room.display()


    # обновление экрана
    pygame.display.update()
