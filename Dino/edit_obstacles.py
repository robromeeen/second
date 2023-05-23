from classes import Odstacle
from random import randint
from random import choice

def creat_odstacles(count, files_path, speed, x, dino_bottom):
    obstacles = []
    for i in range(1, count):
        obstacle = Odstacle(speed, f"{files_path}{i}.png", x, dino_bottom, i == count - 1)
        obstacles.append(obstacle)
    return obstacles


def add_obstacle_to_empty_list(obstacles, WIDTH):
    new_obstacle = choice(obstacles)
    new_obstacle.rect.left = randint(WIDTH, WIDTH + 100)
    return [new_obstacle]

def add_obstacle_to_not_empty_list(current_obstacles, obstacles_rects, WIDTH):
    last_obstacle = current_obstacles[-1]
    if WIDTH - last_obstacle.rect.right > 400:
        new_obstacles = choice(obstacles_rects)
        while new_obstacles in current_obstacles:
            new_obstacles = choice(obstacles_rects)
        new_obstacles.rect.left = randint(WIDTH, WIDTH + 100)
        current_obstacles.append(new_obstacles)
    return current_obstacles

def check_new_obstacles(current_obstacles, obstacles, WIDTH):
    if current_obstacles:
        current_obstacles = add_obstacle_to_not_empty_list(current_obstacles, obstacles, WIDTH)
    else:
        current_obstacles = add_obstacle_to_empty_list(obstacles, WIDTH)
    return current_obstacles

def delete_first_obstacle(obstacles):
    if obstacles:
        first_obstacle = obstacles[0]
        if first_obstacle.rect.right < 0:
            obstacles.pop(0)
    return obstacles