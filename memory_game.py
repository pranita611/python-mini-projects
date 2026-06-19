import pygame, random
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Memory Game")
font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 60)
clock = pygame.time.Clock()
values = [1, 2, 3, 4] * 2
random.shuffle(values)
cards = []
revealed = []
matched = []
flip_time = None
for i in range(8):
    x = (i % 4) * 90 + 20
    y = (i // 4) * 90 + 20
    cards.append(pygame.Rect(x, y, 80, 80))
running = True
while running:
    screen.fill((50, 50, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(revealed) < 2 and flip_time is None:
                for i, r in enumerate(cards):
                    if r.collidepoint(event.pos):
                        if i not in revealed and i not in matched:
                            revealed.append(i)
    for i, r in enumerate(cards):
        if i in revealed or i in matched:
            pygame.draw.rect(screen, (150, 200, 250), r)
            t = font.render(str(values[i]), True, (0, 0, 0))
            screen.blit(t, t.get_rect(center=r.center))
        else:
            pygame.draw.rect(screen, (200, 200, 200), r)
    if len(revealed) == 2 and flip_time is None:
        flip_time = pygame.time.get_ticks()
    if flip_time and pygame.time.get_ticks() - flip_time > 700:
        a, b = revealed
        if values[a] == values[b]:
            matched.extend(revealed)
        revealed.clear()
        flip_time = None
    if len(matched) == len(cards):
        win = big_font.render("YOU WIN!", True, (255, 255, 255))
        screen.blit(win, win.get_rect(center=(200, 200)))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
