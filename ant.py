import pygame
import random
import time
import image
from settings import *

class Ant:
    def __init__(self):
        # size
        random_size_value = random.uniform(ANT_SIZE_RANDOMIZER[0], ANT_SIZE_RANDOMIZER[1])
        size = (int(ANT_SIZES[0] * random_size_value), int(ANT_SIZES[1] * random_size_value))
        # moving direction
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0] // 1.4, size[1] // 1.4)

        # Load the original image without any initial rotation
        original_image = image.load("Assets/Ant/Ant-removebg-preview.png", size=size)

        # Rotate the image based on the movement direction
        if moving_direction == "left":
            self.images = [original_image]
        elif moving_direction == "right":
            self.images = [pygame.transform.flip(original_image, True, False)]
        elif moving_direction == "down":
            self.images = [pygame.transform.rotate(original_image, 90)]
        elif moving_direction == "up":
            self.images = [pygame.transform.rotate(original_image, -90)]

        self.current_frame = 0
        self.animation_timer = 0

    def define_spawn_pos(self, size):  # define the start pos and moving velocity of the ant
        velocity = random.uniform(ANT_MOVE_SPEED["min"], ANT_MOVE_SPEED["max"])
        moving_direction = random.choice(("left", "right", "up", "down"))
        if moving_direction == "right":
            start_pos = (-size[0], random.randint(size[1], SCREEN_HEIGHT - size[1]))
            self.velocity = [velocity, 0]
        if moving_direction == "left":
            start_pos = (SCREEN_WIDTH + size[0], random.randint(size[1], SCREEN_HEIGHT - size[1]))
            self.velocity = [-velocity, 0]
        if moving_direction == "up":
            start_pos = (random.randint(size[0], SCREEN_WIDTH - size[0]), SCREEN_HEIGHT + size[1])
            self.velocity = [0, -velocity]
        if moving_direction == "down":
            start_pos = (random.randint(size[0], SCREEN_WIDTH - size[0]), -size[1])
            self.velocity = [0, velocity]
        return moving_direction, start_pos

    def move(self):
        self.rect.move_ip(self.velocity)

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)

    def draw(self, surface):
        image.draw(surface, self.images[self.current_frame], self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)

    def kill(self, ant_list):  # remove the ant from the list
        ant_list.remove(self)
        return 1
