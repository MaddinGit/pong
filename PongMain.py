import pygame

SPEED = 120
WHITE = 255, 255, 255
BLACK = 0, 0, 0

size = width, height = 1000, 800

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

ball = pygame.Surface((20, 20), pygame.SRCALPHA)
ballPosition = [400, 500]
ballMoveDirection = [1, 6]
paddlePlayer1Pos = 250
paddlePlayer2Pos = 250

paddlePlayer1 = pygame.Surface((20, 300), pygame.SRCALPHA)
paddlePlayer2 = pygame.Surface((20, 300), pygame.SRCALPHA)
rectPaddelPlayer1 = pygame.Rect(0, 0, 20, 300)
rectPaddelPlayer2 = pygame.Rect(0, 0, 20, 300)
pygame.draw.rect(paddlePlayer1, WHITE, rectPaddelPlayer1, 20)
pygame.draw.rect(paddlePlayer2, WHITE, rectPaddelPlayer2, 20)

pygame.key.set_repeat(50, 50)

pygame.draw.circle(ball, WHITE, [10, 10], 10)
done = False
while not done:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and paddlePlayer1Pos < 500:
            paddlePlayer1Pos += 20
        if keys[pygame.K_w] and paddlePlayer1Pos > 0:
            paddlePlayer1Pos -= 20
        if keys[pygame.K_DOWN] and paddlePlayer2Pos < 500:
            paddlePlayer2Pos += 20
        if keys[pygame.K_UP] and paddlePlayer2Pos > 0:
            paddlePlayer2Pos -= 20
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            done = True

    clock.tick(SPEED)

    ballPosition[0] += ballMoveDirection[0]
    ballPosition[1] += ballMoveDirection[1]

    if ballPosition[0] > 780 or ballPosition[0] < 0:
        ballMoveDirection[0] = -ballMoveDirection[0]
    if ballPosition[1] > 980 or ballPosition[1] < 0:
        ballMoveDirection[1] = -ballMoveDirection[1]

    screen.fill(BLACK)
    screen.blit(ball, [ballPosition[1], ballPosition[0]])
    screen.blit(paddlePlayer1, [30, paddlePlayer1Pos])
    screen.blit(paddlePlayer2, [950, paddlePlayer2Pos])
    pygame.display.flip()



