#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the constant file for Prison Escape

# screen
import pygame


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
MIDDLE_X = SCREEN_WIDTH / 2
MIDDLE_Y = SCREEN_HEIGHT / 2
DRAGON_WIDTH = 370
DRAGON_HEIGHT = 219
PORTAL = 120
PORTALW = 140
PRISONER_SIZE = (38 * 2, 39 * 2)
SPARTA_S = (40 * 2, 45 * 2)
WITCH_S = (38 * 2, 43 * 2)
MUSH_S = (17 * 4, 18 * 4)

# images
PRISONER_IMAGE = "Sprites/prisoners/prisoner.png"
GOLEM_IMAGE = "Sprites/golems/golem-walk.png"
DRAGON_IMAGE = "Sprites/Dragon.png"
CELL_IMAGE = "Sprites/cell.png"
DOOR_IMAGE = "Doors/Door1.png"
WIRE_IMAGE = "Sprites/barbed-wire.png"
CASTLE_DOOR_IMAGE = "Doors/castle_door.png"
CHEST_IMAGE = "Sprites/chest-closed.png"
KEY_IMAGE = "Sprites/goldenkey.png"
SHADOW_IMAGE = "Sprites/Shadows/shadow(14).png"
SHIP_IMAGE = "Sprites/ship.png"
SHIP_TWO_IMAGE = "Sprites/ship_two.png"
BULLET_IMAGE = "Sprites/laser.png"
DOOR_THREE = "Doors/door3.png"
CHEST_OPEN = "Sprites/chest-open.png"
prisoners = [
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner2.png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner3.png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner4.png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner5.png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner6.png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner7.png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner8.png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner9.png"), PRISONER_SIZE),
]
prisoners_left = [
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner2.png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner3.png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner4.png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner5.png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner6.png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner7.png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner8.png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner9.png"), PRISONER_SIZE), True, False),
]

red_prisoners = [
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner.png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (1).png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (2).png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (3).png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (4).png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (5).png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (6).png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (7).png"), PRISONER_SIZE),
]
red_prisoners_left = [
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner.png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (1).png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (2).png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (3).png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (4).png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (5).png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (6).png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner (7).png"), PRISONER_SIZE), True, False)
]

sparta_prisoners = [
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner.png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (1).png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (2).png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (3).png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (4).png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (5).png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (6).png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (7).png"), SPARTA_S)
]
sparta_prisoner_left = [
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner.png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (1).png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (2).png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (3).png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (4).png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (5).png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (6).png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner (7).png"), SPARTA_S), True, False)
]

viking_prisoners = [
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner.png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (1).png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (2).png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (3).png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (4).png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (5).png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (6).png"), SPARTA_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (7).png"), SPARTA_S)
]
viking_prisoners_left = [
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner.png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (1).png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (2).png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (3).png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (4).png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (5).png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (6).png"), SPARTA_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner (7).png"), SPARTA_S), True, False),
]

white_prisoners = [
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner.png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (1).png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (2).png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (3).png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (4).png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (5).png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (6).png"), PRISONER_SIZE),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (7).png"), PRISONER_SIZE)
]
white_prisoners_left = [
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner.png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (1).png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (2).png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (3).png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (4).png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (5).png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (6).png"), PRISONER_SIZE), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner (7).png"), PRISONER_SIZE), True, False)
]

witch_prisoners = [
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner.png"), WITCH_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (1).png"), WITCH_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (2).png"), WITCH_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (3).png"), WITCH_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (4).png"), WITCH_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (5).png"), WITCH_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (6).png"), WITCH_S),
    pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (7).png"), WITCH_S)
]
witch_prisoners_left = [
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner.png"), WITCH_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (1).png"), WITCH_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (2).png"), WITCH_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (3).png"), WITCH_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (4).png"), WITCH_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (5).png"), WITCH_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (6).png"), WITCH_S), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner (7).png"), WITCH_S), True, False),
]

one_prisoner = pygame.transform.scale(pygame.image.load("Sprites/prisoners/prisoner.png"), (PRISONER_SIZE[0], PRISONER_SIZE[1] + 8))
red_one_prisoner = pygame.transform.scale(pygame.image.load("Sprites/prisoners/red_prisoner_stand.png"), (PRISONER_SIZE[0], PRISONER_SIZE[1] + 8))
sparta_one_prisoner = pygame.transform.scale(pygame.image.load("Sprites/prisoners/sparta_prisoner_stand.png"), (SPARTA_S[0], SPARTA_S[1] + 8))
viking_one_prisoner = pygame.transform.scale(pygame.image.load("Sprites/prisoners/viking_prisoner_stand.png"), (SPARTA_S[0], SPARTA_S[1] + 8))
white_one_prisoner = pygame.transform.scale(pygame.image.load("Sprites/prisoners/white_prisoner_stand.png"), (PRISONER_SIZE[0], PRISONER_SIZE[1] + 8))
witch_one_prisoner = pygame.transform.scale(pygame.image.load("Sprites/prisoners/witch_prisoner_stand.png"), (WITCH_S[0], WITCH_S[1] + 8))

portal_list = [
    pygame.transform.scale(pygame.image.load("Doors/portals/portals.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals1.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals2.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals3.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals4.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals5.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals6.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals7.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals8.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals9.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals10.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals11.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals12.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals13.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals14.png"), (PORTALW, PORTAL)),
    pygame.transform.scale(pygame.image.load("Doors/portals/portals15.png"), (PORTALW, PORTAL))
]

dragon_list = [
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/dragons/dragon1.png"), (DRAGON_WIDTH, DRAGON_HEIGHT)), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/dragons/dragon2.png"), (DRAGON_WIDTH, DRAGON_HEIGHT)), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/dragons/dragon3.png"), (DRAGON_WIDTH, DRAGON_HEIGHT)), True, False),
    pygame.transform.flip(pygame.transform.scale(pygame.image.load("Sprites/dragons/dragon4.png"), (DRAGON_WIDTH, DRAGON_HEIGHT)), True, False)
]

mushroom_list = [
    pygame.transform.scale(pygame.image.load("Sprites/mushrooms/mushroom.png"), MUSH_S),
    pygame.transform.scale(pygame.image.load("Sprites/mushrooms/mushroom (1).png"), MUSH_S),
    pygame.transform.scale(pygame.image.load("Sprites/mushrooms/mushroom (2).png"), MUSH_S),
    pygame.transform.scale(pygame.image.load("Sprites/mushrooms/mushroom (3).png"), MUSH_S),
    pygame.transform.scale(pygame.image.load("Sprites/mushrooms/mushroom (4).png"), MUSH_S)
]

# backgrounds
SPLASH_SCREEN = "Backgrounds/Splash-Screen.png"
START_SCREEN = "Backgrounds/StartScreen.png"
SCENE_ONE = "Backgrounds/Game-Scene 1.png"
SCENE_TWO = "Backgrounds/Game-Scene 2.png"
SCENE_THREE = "Backgrounds/Game-Scene 3.png"

# sounds
START_SOUND = "Sounds/adventure.mp3"
GAME_SOUND = "Sounds/battle_in_the_winter.mp3"
LASER_SOUND = "Sounds/laser.mp3"
HIT_SOUND = "Sounds/impact.ogg"
ELECTRIC_SOUND = "Sounds/electrocute.flac"
KEY_SOUND = "Sounds/key.mp3"
EAT = "Sounds/eat.mp3"
DOOR_SOUND = "Sounds/door.wav"
WARP = "Sounds/warp.wav"

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (209, 209, 224)
LIGHT_BLUE = (102, 153, 255)
GREEN = (179, 255, 218)
LIGHT_RED = (255, 112, 77)
RED = (255, 0, 0)
ANOTHER_GRAY = (100, 120, 60)
LIGHT_GREEN = (153, 255, 153)
YELLOW = (255,215,0)
MINT = (3, 252, 165)
SKY_BLUE = (30,144,255)
ROYAL_BLUE = (65,105,225)
LAVENDAR = (176,166,222)
PURPLE = (123,104,238)

# speed
PRISONER_X_SPEED = 20
PRISONER_Y_SPEED = 20
GOLEM_SPEED = (10, 0)
BULLET_X_SPEED = 0
BULLET_Y_SPEED = 13
SHADOW_X_SPEED = 0
SHADOW_Y_SPEED = -1
SHIP_X_SPEED = 6
SHIP_Y_SPEED = 0

# size
DOUBLE_SIZE = 2
BULLET_WIDTH = 10
BULLET_HEIGHT = 30


# button & text
TITLE_SIZE = 80
TITLE_FONT = "arialblack"
TITLE_Y = 50
FONT_CORBEL = "corbel"
FONT_COMIC = "comicsansms"
BUTTON_OUTLINE = 5
BACK_BUTTON_X = 80
BACK_BUTTON_Y = 600
BACK_BUTTON_WIDTH = 150
BACK_BUTTON_HEIGHT = 80
BACK_BUTTON_TEXT = "Back"
BACK_BUTTON_TEXT_SIZE = 50
RE_BUTTON_TEXT = "Menu"
ABOUT_TEXT = (
    "This game is created on 2021 June 18th,\n"
    "by Sean McLeod."
    "\n\nAvoid obstacles and escape prison to WIN!"
)
CREDIT_TEXT = (
    "DESIGN:\n"
    "made by https://www.freepik.com https://www.flaticon.com/title=Flaticon>www.flaticon.com\n"
    "Prisoner https://opengameart.org/users/balmer\n"
    "Dragon https://opengameart.org/users/redshrike"
    "Golem https://opengameart.org/content/lpc-golem\n"
    "Ships https://opengameart.org/content/space-ship-construction-kit\n\n"
    "PROGRAMMING:\n"
    "Sean McLeod\n\n"
    "SOUNDS:\n"
    "hit_sound https://opengameart.org/users/starninjas\n"
    "Ice and Electricity Magic by Iwan 'qubodup' Gabovitch http://opengameart.org/users/qubodup\n"
    "laser sound https://opengameart.org/users/dklon\n"
    "start music https://opengameart.org/users/syncopika\n"
    "Game sound https://opengameart.org/users/jobromedia"
)

# distance
SHADOW_DISTANCE = 90

# angle
RIGHT_ANGLE = 90
ROTATE_THREE_TIMES = 270

# position
SHADOW_X = 0
SHADOW_Y = SCREEN_HEIGHT + 126
GOLEM_ONE_X = 100
GOLEM_ONE_Y = 100
GOLEM_TWO_X = 800
GOLEM_TWO_Y = 200
DRAGON_X = 340
DRAGON_Y = 430
FIRST_DOOR_X = 213
FIRST_DOOR_Y = 0
SECOND_DOOR_X = 125
SECOND_DOOR_Y = 0
CHEST_X = 390
CHEST_Y = 380
KEY_X = 400
KEY_Y = 290
SHIP_X = SCREEN_WIDTH / 2 + 200
SHIP_Y = 10
DOOR_THREE_X = MIDDLE_X - 60
DOOR_THREE_Y = 0

# number
SHADOW_NUMBER = 11
BULLET_WAIT = -4

# rate
CLOCK_TICK = 30
WAIT = 1000
BULLET_SHOOT_RATE = 37
MAX_BULLETS = 3
