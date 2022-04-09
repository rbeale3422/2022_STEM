import pygame
import random
import os

#Initialize variables
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong (early iteration)")

FPS = 60
VEL = 5
TARGET_VEL = 4
BALL_VEL = [random.choice([TARGET_VEL, -TARGET_VEL]), 0]
PADDLE_WIDTH, PADDLE_HEIGHT = 150, 100
BALL_DIMENSION = 20

RIGHT_IMAGE= pygame.image.load('./CSP6A/Paddle.png')
RIGHT = pygame.transform.scale(RIGHT_IMAGE, (PADDLE_WIDTH, PADDLE_HEIGHT))

LEFT_IMAGE = pygame.image.load('./CSP6A/Paddle.png')
LEFT = pygame.transform.scale(LEFT_IMAGE, (PADDLE_WIDTH, PADDLE_HEIGHT))

BALL_IMAGE = pygame.image.load('./CSP6A/RedBall.png')
BALL = pygame.transform.scale(BALL_IMAGE, (BALL_DIMENSION, BALL_DIMENSION))
ballcanMove = True
WAIT_TIME = 30

BG_IMAGE = pygame.image.load('./CSP6A/Background.jpg')
BG = pygame.transform.scale(BG_IMAGE, (WIDTH, HEIGHT))

#Functions
# Handles the movement of the right paddle
def rightHandleMove(keys_pressed, right):
  if keys_pressed[pygame.K_UP] and right.y > 0: #RIGHT move up
    right.y -= VEL
  if keys_pressed[pygame.K_DOWN] and right.y < HEIGHT - PADDLE_HEIGHT: #RIGHT move down
    right.y += VEL

# Handles the movement of the left paddle
def leftHandleMove(keys_pressed, left):
  if keys_pressed[pygame.K_w] and left.y > 0: #LEFT move up
    left.y -= VEL
  if keys_pressed[pygame.K_s] and left.y < HEIGHT - PADDLE_HEIGHT: #LEFT move down
    left.y += VEL


# Handles the movement of the ball
def ballMove(ball, left, right):
  global ballcanMove, BALL_VEL

  if ball.x < 0 or ball.x > WIDTH:
    ballcanMove = False
    ball.x = 950/2 - BALL_DIMENSION/2
    ball.y = 500/2 - BALL_DIMENSION/2
    left.y = 500/2 - PADDLE_HEIGHT/2
    right.y = 500/2 - PADDLE_HEIGHT/2
    
  if ballcanMove:
    ball.x += BALL_VEL[0]
    ball.y += BALL_VEL[1]
    
    if ball.x > left.x and ball.x <= left.x+10 and ball.y > left.y and ball.y < left.y + 100:
      BALL_VEL[0] = random.randint(1, TARGET_VEL)
      BALL_VEL[1] = float((TARGET_VEL^2) - (BALL_VEL[0]^2))

    if ball.x-10 < right.x and ball.x > right.x and ball.y > right.y and ball.y < right.y + 100:  
      BALL_VEL[0] = random.randint(-TARGET_VEL, -1)
      BALL_VEL[1] = float((TARGET_VEL^2) - (BALL_VEL[0]^2))

    if ball.y <= 0:
      BALL_VEL[1] = -BALL_VEL[1]

    if ball.y >= 500 - BALL_DIMENSION:
      BALL_VEL[1] = -BALL_VEL[1]

# Draws the window and the items in the window
def draw_window(left, right, ball):
  WIN.blit(BG, (0, 0))
  WIN.blit(RIGHT, (right.x, right.y))
  WIN.blit(LEFT, (left.x, left.y))
  WIN.blit(BALL, (ball.x, ball.y))
  pygame.display.update()

# Keeps the game running until the program is quit
# Also updates the window's state 60 times per second
def main():
  global ballcanMove, WAIT_TIME, goLeft, BALL_VEL
  left = pygame.Rect(100, 200, PADDLE_WIDTH, PADDLE_HEIGHT)
  right = pygame.Rect(750, 200, PADDLE_WIDTH, PADDLE_HEIGHT)
  ball = pygame.Rect(950/2 - BALL_DIMENSION/2, 500/2 - BALL_DIMENSION/2, BALL_DIMENSION, BALL_DIMENSION)
  
  clock = pygame.time.Clock()
  run = True
  while run:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
    
    keys_pressed = pygame.key.get_pressed()
    rightHandleMove(keys_pressed, right)
    leftHandleMove(keys_pressed, left)
    
    if ballcanMove == True:
      ballMove(ball, left, right)
    else:
      WAIT_TIME-=1
      if WAIT_TIME <= 0:
        WAIT_TIME = 30
        ballcanMove = True
        BALL_VEL = [random.choice([TARGET_VEL, -TARGET_VEL]), 0]
            
    draw_window(left, right, ball)

  pygame.quit()

if __name__ == "__main__":
  main()