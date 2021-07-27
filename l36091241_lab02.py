import pygame
import time

# setup the window
WIN_WIDTH = 1024
WIN_HEIGHT = 600
FPS = 1

# create the variables containing images
map_image = pygame.image.load("Map.png")
enemy_image = pygame.image.load('enemy.png')
start_button = pygame.image.load('continue.png')
pause_button = pygame.image.load('pause.png')
sound_button = pygame.image.load('sound.png')
mute_button = pygame.image.load('muse.png')
hp_image = pygame.image.load('hp.png')
hp_grey_image = pygame.image.load('hp_gray.png')

# transform image into the right size
enemy_image_small = pygame.transform.scale(enemy_image, (50, 50))
hp_image_small = pygame.transform.scale(hp_image, (40, 40))
hp_grey_small = pygame.transform.scale(hp_grey_image, (40, 40))

# initialization
pygame.init()

# set up the font used later for time block
font = pygame.font.SysFont('comicsansms', 44)
# create window surface
# window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# set window caption
pygame.display.set_caption("My first game")
# clock
clock = pygame.time.Clock()

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

run = True

# set up the start time, which will minus the endtime to get the running time
start_time = time.time()
minute = 0


while run:
    clock.tick(FPS)
    # event loop (user action)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        win.fill((0, 0, 0))
    # draw the background
    win.blit(map_image, (0, 0))

    # draw black banner on top of the screen
    pygame.draw.rect(win, (0, 0, 0), [0, 0, 1024, 100])

    # draw other objects
    win.blit(enemy_image_small, (18, 270))
    win.blit(pause_button, (930, 15))
    win.blit(start_button, (850, 15))
    win.blit(sound_button, (770, 15))
    win.blit(mute_button, (690, 15))

    # draw the hp on screen, maybe can be solve by loop, will look smarter
    win.blit(hp_image_small, (460, 7))
    win.blit(hp_image_small, (500, 7))
    win.blit(hp_image_small, (420, 7))
    win.blit(hp_image_small, (540, 7))
    win.blit(hp_image_small, (580, 7))
    win.blit(hp_image_small, (420, 50))
    win.blit(hp_image_small, (460, 50))
    win.blit(hp_grey_small, (500, 50))
    win.blit(hp_grey_small, (540, 50))
    win.blit(hp_grey_small, (580, 50))

# decide what time it is
    end_time = time.time()
    duration = int(end_time - start_time)

# make sure that the minute is counting as second goes to 59
    if duration > 10:
        start_time = time.time()
        duration = 0
        minute += 1

# display time and the region on the window
    second_text = font.render(str(duration).zfill(2), False, (255, 255, 255))
    minute_text = font.render(str(minute) + ':', True, (255, 255, 255))
    pygame.draw.rect(win, (0, 0, 0), [0, 540, 103, 60])
    win.blit(second_text, (45, 538))
    win.blit(minute_text, (5, 538))


# draw a rectangle representing the HP
    pygame.draw.rect(win, (255, 0, 0), [25, 260, 36, 4])
    pygame.display.update()

# uninitialize all the pygame module
pygame.quit()
