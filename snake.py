import pygame

# Initialize
pygame.init()

# Screen
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Game loop
score=0
speed = 10
clock = pygame.time.Clock()
running = True
import random
food_x = random.randrange(0, WIDTH, 20)
food_y = random.randrange(0, HEIGHT, 20)
RED = (255, 0, 0)
body=[(300,300),(280,300),(260,300)]
h_x=body[0][0]
h_y=body[0][1]
dir="right"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and dir!="right":
        dir="left"
    if keys[pygame.K_RIGHT] and dir!="left":
        dir="right"
    if keys[pygame.K_UP] and dir!="down":
        dir="up"
    if keys[pygame.K_DOWN] and dir!="up":
        dir="down"
    if dir == "left":
        body.insert(0, (h_x - 20, h_y))
        body.pop()
        h_x = body[0][0]
        h_y = body[0][1]
    if dir == "right":
        body.insert(0, (h_x + 20, h_y))
        body.pop()
        h_x = body[0][0]
        h_y = body[0][1]
    if dir == "up":
        body.insert(0, (h_x, h_y - 20))
        body.pop()
        h_x = body[0][0]
        h_y = body[0][1]
    if dir == "down":
        body.insert(0, (h_x, h_y + 20))
        body.pop()
        h_x = body[0][0]
        h_y = body[0][1]
    if (h_x, h_y) in body[1:]:
        running = False
    if h_x >= WIDTH:
        h_x = 0
    if h_x < 0:
        h_x = WIDTH - 20
    if h_y >= HEIGHT:
        h_y = 0
    if h_y < 0:
        h_y = HEIGHT - 20
    screen.fill(BLACK)
    # Draw food
    pygame.draw.rect(screen, RED, (food_x, food_y, 20, 20))

    # Check if snake ate food
    if h_x == food_x and h_y == food_y:
        food_x = random.randrange(0, WIDTH, 20)
        food_y = random.randrange(0, HEIGHT, 20)
        score += 1
        speed+=1
        if body[-1][0]==body[-2][0]:
            if body[-1][1]>body[-2][1]:
                body.append((body[-1][0],body[-1][1]+20))
            else:
                body.append((body[- 1][0], body[- 1][1] - 20))
        else:
            if body[-1][0]>body[-2][0]:
                body.append((body[- 1][0]+20, body[- 1][1]))
            else:
                body.append((body[- 1][0]-20, body[- 1][1]))
     #  body[len(body)+1]=(body[0][0], body[0][1])
    for i in body:
        pygame.draw.rect(screen, GREEN, (i[0], i[1], 20, 20))
    font = pygame.font.SysFont(None, 35)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(speed)  # 10 frames per second
screen.fill(BLACK)
font = pygame.font.SysFont(None, 60)
text = font.render(f"GAME OVER! Score: {score}", True, RED)
screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2))
pygame.display.flip()
pygame.time.wait(3000)  # wait 3 seconds
pygame.quit()