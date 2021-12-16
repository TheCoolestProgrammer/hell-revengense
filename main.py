import pygame
import copy

background = pygame.image.load("data/background.png")
# main_menu = Main_menu(40, 40)
running = True
pygame.init()
pygame.display.set_caption('deigstra')
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
fps = 60
clock = pygame.time.Clock()
time_on = False
ticks = 0
speed = 1
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

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (140, 0, 35), (
    screen_width // 2 - menu_button_width // 2, screen_height // 3 // 2, menu_button_width, menu_button_height))
    text = font.render(("story mode"), True, (240, 100, 0))
    screen.blit(text, (screen_width // 2 - menu_button_width // 2, screen_height // 3 // 2))
    pygame.draw.rect(screen, (140, 0, 35), (
    screen_width // 2 - menu_button_width // 2, screen_height // 3 + menu_button_height // 2, menu_button_width,
    menu_button_height))
    text = font.render(("multiplayer mode"), True, (240, 100, 0))
    screen.blit(text, (screen_width // 2 - menu_button_width // 2, screen_height // 3 + menu_button_height // 2))
    pygame.draw.rect(screen, (140, 0, 35), (
    screen_width // 2 - menu_button_width // 2, screen_height // 3 * 2, menu_button_width, menu_button_height))
    text = font.render(("mortal tower mode"), True, (240, 100, 0))
    screen.blit(text, (screen_width // 2 - menu_button_width // 2, screen_height // 3 * 2))
    pygame.display.flip()
    clock.tick(fps)
#updated messenge
