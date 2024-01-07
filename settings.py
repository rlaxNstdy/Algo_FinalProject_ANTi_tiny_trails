import pygame

WINDOW_NAME = "ANTi tiny trails"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 850

FPS = 120
DRAW_FPS = True

# fonts
pygame.font.init()
FONT = {}
FONT["small"] = pygame.font.Font(None, 45)
FONT["medium"] = pygame.font.Font(None, 75)
FONT["big"] = pygame.font.Font(None, 120)

# sizes
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (70, 90)
ANT_SIZES = (60, 48)
ANT_SIZE_RANDOMIZER = (2,3) # for each new ant, it will multiply the size with an random value beteewn X and Y
REDANT_SIZES = (60, 60)
REDANT_SIZE_RANDOMIZER = (2, 3)

# drawing
DRAW_HITBOX = False # will draw all the hitbox


# difficulty
GAME_DURATION = 60 # the game will last 60sec
ANT_SPAWN_TIME = 1
ANT_MOVE_SPEED = {"min": 2, "max": 5}
REDANT_PENALITY = 1 # will remove 1 point of the score of the player (if he kills a redant )

# colors
COLORS = {"title": (0, 153, 75), "score": (38, 204, 102), "timer": (0, 255, 128),
            "buttons": {"default": (0, 102, 51), "mouse":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)}} 

# sounds
SOUNDS_VOLUME = 1


