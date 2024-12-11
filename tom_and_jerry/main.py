import pygame

pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("tom and jerry")

class Tom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tom = pygame.image.load("images/tom.jpg")
        self.rect = self.image.get_rect()
    
    def move_tom(self,keys_pressed):
        if keys_pressed[pygame.K_w]:
            self.rect.move_ip(0,-5)
        if keys_pressed[pygame.K_a]:
            self.rect.move_ip(-5,0)
        if keys_pressed[pygame.K_s]:
            self.rect.move_ip(0,5)
        if keys_pressed[pygame.K_d]:
            self.rect.move_ip(5,0)

sprite_group = pygame.sprite.Group()

class Jerry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.jerry = pygame.image.load("images/jerry.jpg")
        self.rect = self.image.get_rect()
    
    def move_jerry(self,keys_pressed):
        if keys_pressed[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if keys_pressed[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if keys_pressed[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

sprite_group = pygame.sprite.Group()

def start_game():
    cat = Tom()
    mouse = Jerry
    sprite_group.add(cat)
    sprite_group.add(mouse)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        cat.move_tom(keys_pressed)
        mouse.move_jerry(keys_pressed)
        screen.fill((255,255,255))
        sprite_group.draw(screen)
        pygame.display.update()


        if event in pygame.event.get = True
start_game()



