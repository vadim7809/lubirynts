import pygame

class BaseSprite():
    def __init__(self, x, y, texture, speed, w, h):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [w, h])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def draw(self, window):
        window.blit(self.texture, self.hitbox)


class Hero(BaseSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and hero.hitbox.x < 650:
            self.hitbox.x += self.speed
        if keys[pygame.K_a] and hero.hitbox.x > 0:
            self.hitbox.x -= self.speed
        if keys[pygame.K_w] and hero.hitbox.y > 0:
            self.hitbox.y -= self.speed
        if keys[pygame.K_s] and hero.hitbox.y < 450:
            self.hitbox.y += self.speed


class Wall():
    def __init__(self, x, y, color, w, h):
        self.hitbox = pygame.Rect(x, y, w, h)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)


pygame.init()

window = pygame.display.set_mode([700, 500])
clock = pygame.time.Clock()

background_img = pygame.image.load("photo/background.jpg")
background_img = pygame.transform.scale(background_img, [700, 500])

hero = Hero(50, 450, "photo/hero.png", 2, 50, 50)

walls = [

    Wall(120, 100, [250, 0, 0], 10, 400),
    Wall(214, 0, [250, 0, 0], 10, 430),
    Wall(308, 0, [250, 0, 0], 10, 251),
    Wall(308, 321, [250, 0, 0], 10, 300),
    Wall(396, 0, [250, 0, 0], 10, 310),
    Wall(396, 380, [250, 0, 0], 10, 150),
    Wall(489, 0, [250, 0, 0], 10, 90),
    Wall(489, 140, [250, 0, 0], 10, 400),


]

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    hero.update()

    window.fill([123, 123, 123])
    window.blit(background_img, [0, 0])

    for wall in walls:
        wall.draw(window)

    hero.draw(window)

    pygame.display.flip()
    clock.tick(60)
