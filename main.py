import pygame

pygame.init()

window = pygame.display.set_mode([700, 500])
clock = pygame.time.Clock()

background_img = pygame.image.load("photo/background.jpg")
background_img = pygame.transform.scale(background_img, [700, 500])

cyborg_png = pygame.image.load("photo/cyborg.png")
cyborg_png = pygame.transform.scale(cyborg_png, [50, 50])

hero_png = pygame.image.load("photo/hero.png")
hero_png = pygame.transform.scale(hero_png, [50, 50])

treasure_png = pygame.image.load("photo/treasure.png")
treasure_png = pygame.transform.scale(treasure_png, [50, 50])

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    window.fill([123, 123, 123])
    window.blit(background_img, [0,0])
    window.blit(cyborg_png, [50, 50])
    window.blit(hero_png, [250, 50])
    window.blit(treasure_png, [500, 50])
    pygame.display.flip()
    clock.tick(60)