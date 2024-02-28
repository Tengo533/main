import pygame
from pygame.locals import *
import random

def get_highscore(speed):
    with open("Term 2\Lesson 7\Car_Game\highscore","r") as fr:
        highscore = fr.read()
    if float(highscore) < speed:
        with open("Term 2\Lesson 7\Car_Game\highscore", "w") as fw:
            fw.write(str(speed))
            print("You got a new high score!")

def display_highscore(speed):
    with open("Term 2\Lesson 7\Car_Game\highscore","r") as fr:
        highscore = fr.read()
        highscore = round(int(highscore),1)
    return highscore

size = width, height = (800, 800)
road_w = int(width / 1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1


pygame.init()
running = True
# set window size
screen = pygame.display.set_mode((size))
# set title
pygame.display.set_caption("Car Game")
# set background colour
screen.fill((60, 220, 0))
# draw graphics
pygame.draw.rect(    #  ROAD
    screen, 
    (50, 50, 50,), # colour
    (width/2-road_w/2, 0, road_w, height) # co-oridnates
)

pygame.draw.rect(    # YELLOW CENTRAL LINE
    screen,
    (255, 240, 60), # colour
    (width/2 - roadmark_w, 0, roadmark_w, height) # co-oridnates
)

pygame.draw.rect(    # LEFT SIDE WHITE LINE
    screen,
    (255, 255, 255), # colour
    (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height) # co-oridnates
)

pygame.draw.rect(     # RIGHT SIDE WHITE LINE
    screen,
    (255, 255, 255), # colour
    (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height) # co-oridnates
)

# appy changes
pygame.display.update()

# load images

# load player vehicle
car = pygame.image.load("Term 2\Lesson 7\Car_Game\car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8

# load enemy vehicle
car2 = pygame.image.load("Term 2\Lesson 7\Car_Game\otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

counter = 0

# game loop
while running:
    counter += 1
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("Level up, Speed: ",round(speed,1))
    # animate enemy vehicle
    car2_loc[1] += speed
    if car2_loc[1] > height:
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
    # end game
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        get_highscore(speed)
        print("Game Over! You crashed!")
        break

    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])
    pygame.draw.rect(    #  ROAD
    screen, 
    (50, 50, 50,), # colour
    (width/2-road_w/2, 0, road_w, height) # co-oridnates
    )

    pygame.draw.rect(    # YELLOW CENTRAL LINE
        screen,
        (255, 240, 60), # colour
        (width/2 - roadmark_w, 0, roadmark_w, height) # co-oridnates
    )

    pygame.draw.rect(    # LEFT SIDE WHITE LINE
        screen,
        (255, 255, 255), # colour
        (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height) # co-oridnates
    )

    pygame.draw.rect(     # RIGHT SIDE WHITE LINE
        screen,
        (255, 255, 255), # colour
        (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height) # co-oridnates
    )

    
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
   # highscore_text = font.render(f'High Score: {hs_current}', True, (255,255,255))
    pygame.display.update()


pygame.quit()