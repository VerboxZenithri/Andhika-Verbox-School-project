import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
square = pygame.Rect(100, 100, 50, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        square.y -= 25
    if keys[pygame.K_DOWN]:
        square.y += 25
    if keys[pygame.K_LEFT]:
        square.x -= 25
    if keys[pygame.K_RIGHT]:
        square.x += 25
    # clamp
    square.x = max(0, min(screen.get_width() - square.width, square.x))
    square.y = max(0, min(screen.get_height() - square.height, square.y))

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), square)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()