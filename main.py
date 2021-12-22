import pygame
import copy

class Background():
    def load_background(self,level):
        if level==0:
            self.background = pygame.image.load("data/background2.png")
        self.position_x = 0
        self.position_y = 0
        self.speed = 1
    def bliting(self):
        screen.blit(self.background, (self.position_x, self.position_y))

background = Background()
background.load_background(0)
background_position_x = 0
background_position_y = 0
background_speed = 1
running = True
pygame.init()
pygame.display.set_caption('deigstra')
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
fps = 60
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 40)
menu_button_width = 500
menu_button_height = 100

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        background.position_x += background.speed
    elif keys[pygame.K_RIGHT]:
        background.position_x -= background.speed


    screen.fill((0, 0, 0))
    background.bliting()
    pygame.display.update((0,0,screen_width,screen_height))
    clock.tick(fps)
#updated messenge
