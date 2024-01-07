import pygame
from settings import *

def draw_text(surface, text, pos, color, font=FONT["medium"], pos_mode="top_left",
                shadow=False, shadow_color=(0,0,0), shadow_offset=2):
    label = font.render(text, 1, color)
    label_rect = label.get_rect()
    if pos_mode == "top_left":
        label_rect.x, label_rect.y = pos
    elif pos_mode == "center":
        label_rect.center = pos

    if shadow: # make the shadow
        label_shadow = font.render(text, 1, shadow_color)
        surface.blit(label_shadow, (label_rect.x - shadow_offset, label_rect.y + shadow_offset))

    surface.blit(label, label_rect) # draw the text



def button(surface, pos_y, text=None, click_sound=None):
    rectangel = pygame.Rect((SCREEN_WIDTH//2 - BUTTONS_SIZES[0]//2, pos_y), BUTTONS_SIZES)

    on_button = False
    if rectangel.collidepoint(pygame.mouse.get_pos()):
        color = COLORS["buttons"]["mouse"]
        on_button = True
    else:
        color = COLORS["buttons"]["default"]

    pygame.draw.rect(surface, color, rectangel) # draw the rectangle
    # draw the text
    if text is not None:
        draw_text(surface, text, rectangel.center, COLORS["buttons"]["text"], pos_mode="center",
                    shadow=True, shadow_color=COLORS["buttons"]["shadow"])

    if on_button and pygame.mouse.get_pressed()[0]: # if the user press on the button
        if click_sound is not None:
            click_sound.play()
        return True
