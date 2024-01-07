import pygame
import time
import random
from settings import *
from background import Background
from hand import Hand
from hand_tracking import HandTracking
from ant import Ant
from redant import Redant
import cv2
import ui

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()

        # Load camera
        self.cap = cv2.VideoCapture(0)

        self.sounds = {}
        self.sounds["slap"] = pygame.mixer.Sound(f"Assets/Sounds/slap.wav")
        self.sounds["slap"].set_volume(SOUNDS_VOLUME)
        self.sounds["screaming"] = pygame.mixer.Sound(f"Assets/Sounds/ouch redant.wav")
        self.sounds["screaming"].set_volume(SOUNDS_VOLUME)

    def load_camera(self):
        _, self.frame = self.cap.read()


    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.rect.center = (x, y)


    def reset(self): 
        self.game_start_time = time.time()
        self.hand = Hand()
        self.hand_tracking = HandTracking()
        self.insects = []
        self.insects_spawn_timer = 0
        self.score = 0
        


    def spawn_insects(self):
        t = time.time()
        if t > self.insects_spawn_timer:
            self.insects_spawn_timer = t + ANT_SPAWN_TIME

            # to make the probility that the ant more  appearing than the redant
            nb = (GAME_DURATION-self.time_left)/GAME_DURATION * 100  / 2  
            if random.randint(0, 100) < nb:
                self.insects.append(Redant())
            else:
                self.insects.append(Ant())

            # spawn a other red ant after the half of the game
            if self.time_left < GAME_DURATION/2:
                self.insects.append(Ant())

    def draw(self):
        # draw the background
        self.background.draw(self.surface)
        # draw the insects
        for insect in self.insects:
            insect.draw(self.surface)
        # draw the hand
        self.hand.draw(self.surface)
        # draw the score
        ui.draw_text(self.surface, f"Score : {self.score}", (5, 5), COLORS["score"], font=FONT["medium"],
                    shadow=True, shadow_color=(255,255,255))
        # draw the time left
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"] # change the text color if less than 5 s left
        ui.draw_text(self.surface, f"Time left : {self.time_left}", (SCREEN_WIDTH//2, 5),  timer_text_color, font=FONT["medium"],
                    shadow=True, shadow_color=(255,255,255))


    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)



    def update(self):

        self.load_camera()
        self.set_hand_position()
        self.game_time_update()

        self.draw()

        if self.time_left > 0:
            self.spawn_insects() 
            (x, y) = self.hand_tracking.get_hand_center()  # Get the current hand position
            self.hand.rect.center = (x, y)  # Update the position of the game's hand sprite to the current hand position
            self.hand.left_click = self.hand_tracking.hand_closed  # Update the state of hand click based on hand tracking
            print("Hand closed", self.hand.left_click)  # Print a message indicating whether the hand is closed (clicked) or not
            
            if self.hand.left_click:
                # If the hand is closed (clicked)
                self.hand.image = self.hand.image_smaller.copy()  # Set the hand image to a smaller version
            else:
                # If the hand is not closed (not clicked)
                self.hand.image = self.hand.orig_image.copy()  # Set the hand image to the original image
            self.score = self.hand.kill_insects(self.insects, self.score, self.sounds)  # Update the score by checking for insect collisions with the hand
            
            for insect in self.insects:
                insect.move()  # Move each insect in the game


        else: # after the game 
            if ui.button(self.surface, 540, "Continue", click_sound=self.sounds["slap"]):
                return "menu"


        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)
