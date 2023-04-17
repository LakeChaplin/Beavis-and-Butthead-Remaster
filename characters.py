import pygame

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
        self.velocity = 5
        self.jump_height = 10
        self.is_jumping = False
        self.action_key = False
        self.image = pygame.image.load(image_path)
        self.fliped_image = pygame.transform.flip(self.image, True, False)
        self.fliped = False
    # функция отрисокви персонажа
    def draw(self, screen):
        if self.fliped:
            screen.blit(self.fliped_image, (self.x, self.y))
        else:
            screen.blit(self.image, (self.x, self.y))

    
    # Фунция, разворачивающая персонажа по оси x
    def flip(self):
        self.fliped = not self.fliped
    
    # функция, отвечающая за передвижение персонажей
    def move(self, dx, dy):
        self.x += dx * self.velocity
        self.y += dy * self.velocity
    
    # функция реализующая прыжок
    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True

    def interact(self):
        self.action_key = True

    def update(self):
        if self.is_jumping:
            # Реализация прыжка (с учетом гравитации)
            pass

        if self.action_key:
            # Реализация взаимодействия с объектами
            pass

        self.action_key = False

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
    

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def fart(self):
        # Реализация пукания
        pass

class Butthead(Character):
    def __init__(self, x, y):
        super().__init__(x, y, 36, 72, (150, 150, 150), 100, 100, 'graphic/butthead_image.png')
        self.image = pygame.image.load('graphic/butthead_image.png')

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def burp(self):
        # Реализация рыгания
        pass
