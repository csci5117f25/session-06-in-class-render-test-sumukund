from itertools import cycle
import random
import sys
import pygame
from pygame.locals import *

FPS = 30
SCREENWIDTH = 288
SCREENHEIGHT = 512
PIPEGAPSIZE = 100  ## gap between upper and lower part of pipe
BASEY = SCREENHEIGHT * 0.79
## image and hitmask  dicts
IMAGES, HITMASKS = {}, {}

## list of all possible players (tuple of 3 positions of flap)
PLAYERS_LIST = (
    ## red bird
    (
        "data/sprites/devi-closed.png",
        "data/sprites/devi-maa.png",
        "data/sprites/devi-tongue.png",
    ),
    ## blue bird
    (
        "data/sprites/bluebird-upflap.png",
        "data/sprites/bluebird-midflap.png",
        "data/sprites/bluebird-downflap.png",
    ),
    ## yellow bird
    (
        "data/sprites/yellowbird-upflap.png",
        "data/sprites/yellowbird-midflap.png",
        "data/sprites/yellowbird-downflap.png",
    ),
)

## list of backgrounds
BACKGROUNDS_LIST = (
    "data/sprites/background.png",
)

## list of pipes
PIPES_LIST = (
    "data/sprites/pipe-green.png",
    "data/sprites/pipe-red.png",
)