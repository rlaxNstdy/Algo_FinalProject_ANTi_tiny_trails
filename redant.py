import pygame
import random
import image
from settings import *
from ant import Ant

class Redant(Ant):
    def __init__(self):
        #size
        random_size_value = random.uniform(REDANT_SIZE_RANDOMIZER[0], REDANT_SIZE_RANDOMIZER[1])
        size = (int(REDANT_SIZES[0] * random_size_value), int(REDANT_SIZES[1] * random_size_value))
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        original_image = image.load("Assets/Red_ant/redant.png", size=size)

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
        self.current_frame = 0
        self.animation_timer = 0 
        

    def kill(self,ant): # remove the ant from the list
        ant.remove(self)
        return -REDANT_PENALITY
