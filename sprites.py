import pygame

helicopter_1 = pygame.image.load('sprites/helicopter_11.png')
helicopter_2 = pygame.image.load('sprites/helicopter_22.png')
helicopter_crash_1 = pygame.image.load('sprites/helicopter_crash_11.png')
helicopter_crash_2 = pygame.image.load('sprites/helicopter_crash_22.png')
helicopter_crash_3 = pygame.image.load('sprites/helicopter_crash_33.png')
helicopter_crash_4 = pygame.image.load('sprites/helicopter_crash_44.png')
helicopter_damaged_1 = pygame.image.load('sprites/helicopter_damaged_11.png')
helicopter_damaged_2 = pygame.image.load('sprites/helicopter_damaged_22.png')

enemy_helicopter_1 = pygame.image.load('sprites/enemy_helicopter_11.png')
enemy_helicopter_2 = pygame.image.load('sprites/enemy_helicopter_22.png')

boat1 = pygame.image.load('sprites/boat1.png')

helicopter_list = [helicopter_1, helicopter_2]
damaged_helicopter_list = [helicopter_damaged_1, helicopter_damaged_2]
enemy_helicopter_list = [enemy_helicopter_1, enemy_helicopter_2]

balloon = pygame.image.load('sprites/balloon1.png')

spaceship = pygame.image.load('sprites/spaceship1.png')

icon = pygame.image.load('sprites/icon.png')
background1 = pygame.image.load('sprites/background1.png')
cloud = pygame.image.load('sprites/cloud1.png')

all_sprites = [helicopter_1, helicopter_2, helicopter_damaged_1, helicopter_damaged_2, enemy_helicopter_1,
               enemy_helicopter_2, helicopter_crash_1, helicopter_crash_2, helicopter_crash_3, helicopter_crash_4,
               boat1, balloon, spaceship, icon, background1, cloud]
