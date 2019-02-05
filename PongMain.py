import pygame

SPEED = 100
BALL_COLOR = 255, 255, 255
BACKGROUND_COLOR = 0, 0, 0

size = width, height = 1000, 800

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

circle = pygame.Surface((20, 20), pygame.SRCALPHA)
position = [0, 0]
moveDirection = [1, 6]

paddle = pygame.Surface((9, 100), pygame.SRCALPHA)
rect = pygame.Rect(0,0,80,90)
pygame.draw.rect(paddle, BALL_COLOR, rect, 10)

pygame.draw.circle(circle, BALL_COLOR, [10, 10], 10)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    clock.tick(SPEED)

    position[0] += moveDirection[0]
    position[1] += moveDirection[1]

    if position[0] > 780 or position[0] < 0:
        moveDirection[0] = -moveDirection[0]
    if position[1] > 980 or position[1] < 0:
        moveDirection[1] = -moveDirection[1]

    screen.fill(BACKGROUND_COLOR)
    screen.blit(circle, [position[1], position[0]])
    screen.blit(paddle, [30, 30])
    pygame.display.flip()



