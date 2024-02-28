import pygame as pg
from random import randrange
from random import randint
pg.init()
pg.font.init()
WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1,}
score = 0
font = pg.font.Font(None, 36)
def get_colour():
    colours = ['orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    num = randint(0, 5)
    colour = colours[num]
    return colour
#def get_highscore(score):
    with open(r'C:\Users\546003\OneDrive - eastsussexcollegegroup\Python\Term 2\Lesson 6 - Snake\highscore.txt','r') as fr:
        current_hs = fr.read()
        print(current_hs)
    if int(current_hs) < int(score):
        with open(r'C:\Users\546003\OneDrive - eastsussexcollegegroup\Python\Term 2\Lesson 6 - Snake\highscore.txt','a') as fw:
                fw.write(score)


#def display_highscore():
    with open(r'C:\Users\546003\OneDrive - eastsussexcollegegroup\Python\Term 2\Lesson 6 - Snake\highscore.txt','r') as fr:
        lines = fr.read().splitlines()
        last_line = lines[-1]
        return lines
    
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs[pg.K_w]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1,}
            if event.key == pg.K_s and dirs[pg.K_s]:
                snake_dir = (0, TILE_SIZE)
                {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1,}
            if event.key == pg.K_a and dirs[pg.K_a]:
                snake_dir = (-TILE_SIZE, 0)
                {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0,}
            if event.key == pg.K_d and dirs[pg.K_d]:
                snake_dir = (TILE_SIZE, 0)
                {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1,}

    screen.fill('black')
    # check borders and self-eating
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]
        #get_highscore(score)
        score = 0
    # check food
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1
        score += 100
    # draw food
    pg.draw.rect(screen, 'red', food)
    # draw snake
    [pg.draw.rect(screen, get_colour(), segment) for segment in segments]
    # move snake
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    score_text = font.render(f'Score: {score}', True, (255,255,255))
    screen.blit(score_text, (10, 10))
    #hs_current = display_highscore()
    highscore_text = font.render(f'High Score: {score}', True, (255,255,255))
    screen.blit(highscore_text, (1000, 10))
    pg.display.flip()
    clock.tick(30)
