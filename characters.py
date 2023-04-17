import pygame
from levels_geometry import Platform

# Создание общего класса главных персонажей
class Character:
    def __init__(self, x, y, width, height, color, max_health, max_energy, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.health = max_health
        self.max_health = max_health
        self.energy = max_energy
        self.max_energy = max_energy
        self.inventory = [None] * 5
        self.velocity = 2
        self.jump_height = 10
        self.is_jumping = False
        self.action_key = False
        self.image = pygame.image.load(image_path)
        self.fliped_image = pygame.transform.flip(self.image, True, False)
        self.fliped = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    # функция отрисокви персонажа
    def draw(self, screen):
        if self.fliped:
            screen.blit(self.fliped_image, (self.x, self.y))
        else:
            screen.blit(self.image, (self.x, self.y))
    
    # Функуия проверки коллизий с другими объектами 
    def check_collision(self, platforms, dx, dy):
        next_rect = pygame.Rect(self.x + dx, self.y + dy, self.width, self.height)

        for platform in platforms:
            if next_rect.colliderect(platform.rect):
                return True
        return False
    # Ограничение персонажей для движения по оси Y
    def check_y_bounds(self, dy):
        new_y = self.y + dy * self.velocity
        lower_limit = 0
        upper_limit = 321 - self.height
        return lower_limit <= new_y <= upper_limit 
    
    # Фунция, разворачивающая персонажа по оси x
    def flip(self):
        self.fliped = not self.fliped
    
    # функция, отвечающая за передвижение персонажей
    def move(self, dx, dy, platforms):
        # проверка на положение персонажа по оси Y
        if self.check_y_bounds(dy):
            if not self.check_collision(platforms, 0, dy * self.velocity):
                self.y += dy * self.velocity
        if not self.check_collision(platforms, dx * self.velocity, 0):
            self.x += dx * self.velocity

        # Добавьте следующий код для вызова flip() при изменении направления
        if dx > 0 and self.fliped:
            self.flip()
        elif dx < 0 and not self.fliped:
            self.flip()


    
    # функция реализующая прыжок
    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True

    def interact(self):
        self.action_key = True

    def update(self, platforms):
         self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
         if self.is_jumping:
            # Реализация прыжка (с учетом гравитации)
            self.vertical_velocity = -self.jump_height
            self.is_jumping = False

        # Обновление вертикальной скорости из-за гравитации
            self.vertical_velocity += self.gravity

            # Проверка столкновений с платформами
            if self.check_collision(platforms):
                self.vertical_velocity = 0
            else:
                self.rect.y += self.vertical_velocity

            if self.action_key:
                # Реализация взаимодействия с объектами
                pass           
            
        
            if self.is_jumping:
                # Реализация прыжка (с учетом гравитации)
                pass

            self.action_key = False


    # Функция слежения одного персонажа за другим
    def follow(self, target, distance, platforms):
        dx, dy = 0, 0
        if abs(self.x - target.x) > distance:
            dx = 1 if self.x < target.x else -1
        if abs(self.y - target.y) > distance:
            dy = 1 if self.y < target.y else -1
        self.move(dx, dy, platforms)




    # функция получения урона
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    # функция регенерация энергии
    def regenerate_energy(self, amount):
        self.energy += amount
        if self.energy > self.max_energy:
            self.energy = self.max_energy

class Beavis(Character):
    def __init__(self, x, y):
        super().__init__(x, y, 36, 72, (100, 100, 100), 100, 100, 'graphic/beavis_image.png')
        self.image = pygame.image.load('graphic/beavis_image.png')
    

    # def move(self, dx, dy):
    #     self.x += dx
    #     self.y += dy

    def fart(self):
        # Реализация пукания
        pass

class Butthead(Character):
    def __init__(self, x, y):
        super().__init__(x, y, 36, 72, (150, 150, 150), 100, 100, 'graphic/butthead_image.png')
        self.image = pygame.image.load('graphic/butthead_image.png')

    # def move(self, dx, dy):
    #     self.x += dx
    #     self.y += dy

    def burp(self):
        # Реализация рыгания
        pass
