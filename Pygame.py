import pygame
import random
# Initialize the pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))


def main():
    # Set Windowns Configurations
    set_windown()
    # Parameters player and enemy
    player_move_x = 370
    player_move_y = 480
    change_player_move_x = 0

    enemy_move_x = random.randint(0, 800)
    enemy_move_y = random.randint(0, 400)
    change_enemy_move_x = 0.3
    change_enemy_move_y = 0.3
    
    # Game loop
    running = True
    while running:
        screen.fill((255, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_player_move_x = -0.1
                if event.key == pygame.K_RIGHT:
                    change_player_move_x = 0.1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    change_player_move_x = 0
        player_move_x += change_player_move_x
        if player_move_x < -3:
            player_move_x = 720
        elif player_move_x >= 720:
            player_move_x = 0

        enemy_move_x += change_enemy_move_x
        if enemy_move_x < -3:
            change_enemy_move_x = 0.3
        elif enemy_move_x >= 720:
            enemy_move_x = -0.3


        player(player_move_x, player_move_y)
        enemy(enemy_move_x, enemy_move_y)
        pygame.display.update()


def set_windown():
    icon = pygame.image.load("icons8-ficção-científica-80.png")
    pygame.display.set_caption("Space Invaders")
    pygame.display.set_icon(icon)


def player(player_x, player_y):
    player_img = pygame.image.load("icons8-foguete-lançado-96.png")
    screen.blit(player_img, (player_x, player_y))


def enemy(enemy_x, enemy_y):
    enemy_img = pygame.image.load("icons8-agente-smith-96.png")
    screen.blit(enemy_img, (enemy_x, enemy_y))


main()