import pygame
import sys

pygame.init()

W, H=900, 700 #width and Height
scrn=pygame.display.set_mode((W, H))
tile=40
clock=pygame.time.Clock()
world=[
    "111111111111"
    "100000000001"
    "100111011001"
    "100111011011"
    "100111000011"
    "100000000001"
    "111111111111"
]

player_pos=pygame.Vector2(W//2, H//2)
player_spd=4
player_sz=40
player_hp=100


zombie_pos=pygame.Vector2(100, 100)
zombie_spd=2
zombie_sz=40

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    ky = pygame.key.get_pressed()
    m = pygame.Vector2(0, 0)

    if ky[pygame.K_UP]:
        m.y=-1
    if ky[pygame.K_DOWN]:
        m.y=1
    if ky[pygame.K_LEFT]:
        m.x=-1
    if ky[pygame.K_RIGHT]:
        m.x=1

    if m.length() !=0:
        m=m.normalize()

    player_pos+=m*player_spd

    direction=player_pos-zombie_pos
    if direction.length() !=0:
        direction=direction.normalize()

    zombie_pos+=direction*zombie_spd

    player_pos.x=max(0, min(W-player_sz, player_pos.x))
    player_pos.y=max(0, min(H-player_sz, player_pos.y))

    scrn.fill((30, 30, 30))
    pygame.draw.rect(scrn, (0,200, 0), (player_pos.x, player_pos.y, player_sz, player_sz))
    pygame.draw.rect(scrn, (200, 0, 0), (zombie_pos.x, zombie_pos.y, zombie_sz, zombie_spd))
    pygame.display.update()
    clock.tick(60)