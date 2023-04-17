import pygame
from  room_location import Room


# задний фон меню
background = pygame.image.load('graphic/back.jpg')





### Функция отображения главного меню ###
def display_main_menu(screen, width, height, events):
    # Отрисовка фонового изображения
    screen.blit(background, (0, 0))

    # Шрифт текста
    font = pygame.font.Font('freesansbold.ttf', 36)

    # Текстовая надпись с названием игры
    game_title = font.render('Beavis and Butthead Remaster', True, (0, 0, 0))

    # Отрисовка текстовой надписи с названием игры
    title_x = (width - game_title.get_width()) // 2
    title_y = 50
    screen.blit(game_title, (title_x, title_y))

        # координаты кнопок
    button_x = 150
    play_button_y = 300
    options_button_y = 375
    exit_button_y = 450

    # размеры кнопок
    button_width = 150
    button_height = 50

    # цвета кнопок
    button_color = (128, 128, 128)
    highlight_color = (157, 51, 15)

    # текстовая надпись на кнопках
    play_text = font.render('Play', True, (0, 0, 0))
    option_text = font.render('Options', True, (0, 0, 0))
    exit_text = font.render('Exit', True, (0, 0, 0))

    # координаты для центрирования текста на кнопках
    play_text_x = button_x + (button_width - play_text.get_width()) // 2
    options_text_x = button_x + (button_width - option_text.get_width()) // 2
    exit_text_x = button_x + (button_width - exit_text.get_width()) // 2
    play_text_y = play_button_y + (button_height - play_text.get_height()) // 2
    options_text_y = options_button_y + (button_height - option_text.get_height()) // 2
    exit_text_y = exit_button_y + (button_height - exit_text.get_height()) // 2


    # обработка наведения мышью на кнопки
    mouse_position = pygame.mouse.get_pos()

    # Отрисовка кнопки play
    play_button_rect = pygame.Rect(button_x, play_button_y, button_width, button_height)
    if play_button_rect.collidepoint(mouse_position):
        play_text_colored = font.render('Play', True, highlight_color)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return 'start_game'

    else:
        play_text_colored = font.render('Play', True, (0, 0, 0))
    screen.blit(play_text_colored, (play_text_x, play_text_y))

    # отрисовка кнопки Options
    options_button_rect = pygame.Rect(button_x, options_button_y, button_width, button_height)
    if options_button_rect.collidepoint(mouse_position):
        option_text_colored = font.render('Options', True, highlight_color)
    else:
        option_text_colored = font.render('Options', True, (0, 0, 0))
    screen.blit(option_text_colored, (options_text_x, options_text_y))

    # отрисовка кнопки Exit
    exit_button_rect = pygame.Rect(button_x, exit_button_y, button_width, button_height)
    if exit_button_rect.collidepoint(mouse_position):
        exit_text_colored = font.render('Exit', True, highlight_color)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.quit()
                raise SystemExit 
    else:
        exit_text_colored = font.render('Exit', True, (0, 0, 0))
    screen.blit(exit_text_colored, (exit_text_x, exit_text_y))

    return None



    
