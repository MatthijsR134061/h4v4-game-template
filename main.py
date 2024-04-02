#
# BREAKOUT GAME 
#

import pygame, time

#
# define constants 
#

FPS = 30 # Frames Per Second
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BALL_WIDTH = 16
BALL_HEIGHT = 16

#
# define global variables
#

ball_x = 0
ball_speed_x = 6

ball_y = 0
ball_speed_y = 6

#
# init game
#

pygame.init()
font = pygame.font.SysFont('default', 64)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
fps_clock = pygame.time.Clock()

#
# read images
#

spritesheet = pygame.image.load('Breakout_Tile_Free.png').convert_alpha() # convert_alpha increases speed of blit and keeps transparancy of .png

ball_img = pygame.Surface((64, 64)) # create new image
ball_img.blit(spritesheet, (0, 0), (1403, 652, 64, 64))  # copy part of sheet to image
ball_img = pygame.transform.scale(ball_img, (BALL_WIDTH, BALL_HEIGHT)) # resize image

#
# game loop
#

print('mygame is running')
running = True
while running:
    # read all events
    # to end programme when GUI is closed and to read keys using pygame.get.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # move ball
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y
    # bounce ball against edges of screen
    if ball_x < 0 or ball_x + BALL_WIDTH > SCREEN_WIDTH:
      ball_speed_x = ball_speed_x * -1

    # clear screen
    screen.fill('black') 

    # draw ball
    screen.blit(ball_img, (ball_x, ball_y))

    # show screen
    pygame.display.flip() 

    # Sleep the remaining time of this frame
    fps_clock.tick(FPS) 

print('mygame stopt running')
