import pygame
from random import choice, randint
import edit_obstacles
import classes
import display
import game_settings


#Параметры игрового поля и fps
WIDTH, HEIGHT = 1500, 600
start_fps = 50
fps = start_fps
score = 0
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

display.add_background_music("music/background.mp3")

dino = classes.Dino("images/dino/dino_1.png", HEIGHT, "music/jump_sound.ogg", "music/landing_sound.ogg", "music/crash_sound.ogg")
ground = classes.Ground("images/world/ground.png", dino.rect.y + dino.rect.size[0] - 0, 0)
clouds = display.create_clouds(5, WIDTH, 100, "images/world/cloud.png", 0)
OBSTACLES_COUNT = 11
OBSTACLES_SPEED = 10
obstacles = edit_obstacles.creat_odstacles(OBSTACLES_COUNT, "images/enemies/cactus_", 0, WIDTH, dino.rect.bottom)
current_obstacles = []

while True:
    # Выход по нажатию крестика
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if game_settings.check_start(ground.speed):
        score = 0
        dino.crash = True
        ground.speed = OBSTACLES_SPEED
        fps = start_fps
        current_obstacles = []
        for obstacle in obstacles:
            obstacle.speed = OBSTACLES_SPEED
        for cloud in clouds:
            cloud.speed = OBSTACLES_SPEED // 3

    display.draw_world(sc, ground, clouds, score, WIDTH)
    dino.draw(sc)
    ground.move(WIDTH)

    for obstacle in current_obstacles:
        obstacle.draw(sc)
        obstacle.move()

    for cloud in clouds:
        cloud.draw(sc)
        cloud.move(WIDTH, 200)
    dino.jump()
    dino.sat_down()
    current_obstacles = edit_obstacles.check_new_obstacles(current_obstacles, obstacles, WIDTH)
    current_obstacles = edit_obstacles.delete_first_obstacle(current_obstacles)


    if game_settings.check_game_over(dino, current_obstacles):
        ground.speed = 0
        for obstacle in obstacles:
            obstacle.speed = 0
        for cloud in clouds:
            cloud.speed = 0
        font = pygame.font.SysFont(None, 100)
        text = font.render("GAME OVER", True, pygame.Color("grey"))
        sc.blit(text, (WIDTH / 2 - 230, HEIGHT / 4))



    score = game_settings.increase_score(score, fps, ground.speed)
    pygame.display.flip()
    clock.tick(fps + score // 10)