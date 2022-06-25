# This Python file uses the following encoding: utf-8
import pygame
import time
import random
import winsound

math = pygame.math
start = time.time()
pygame.init()

x = 1
s = True
# -- colors --
white = (255, 255, 255)
black = (0, 0, 0)

# -- font --
score_l = "0"
score_r = "0"
pygame.font.init()
myfont = pygame.font.SysFont("f1", 100)
startfont = pygame.font.SysFont("F2", 80)

# -- width\height --
game_width = 800
game_height = 500

p1_x = 50
p1_height = 50

p2_x = game_width-50
p2_height = 50

# -- movement direction --
LeftUp = False
LeftDown = False
RightUp = False
RightDown = False

# -- ball --
random_x = random.choice([1, -1])
random_y = random.choice([1, -1])
ball_x = 400
ball_y = 250
ball_speed_y = 2 * random_x
ball_speed_x = 2 * random_y

# -- paddle speed --
pspeed = 5

# -- game lab --
lab = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("pong")


# -- movement function --
def move():
    """
    this function decide the computer player movement
    """
    global p2_height, p1_height, ball_x, ball_y
    time.sleep(0.01)
    if LeftUp:
        p1_height -= pspeed
    if LeftDown:
        p1_height += pspeed
    if (p2_height + 25) < ball_y:
        p2_height += (pspeed - 1)
    if (p2_height + 25) > ball_y:
        p2_height -= (pspeed - 1)

    ball_x += ball_speed_x
    ball_y += ball_speed_y


# -- if there is one player --
def one(one):
    global p1_height, p2_height, ball_speed_y, ball_speed_x, LeftUp, LeftDown, RightDown,\
        RightUp, x, ball_x, ball_y, score_r, score_l

    beep = winsound.Beep(400, 30)  # the beep noise
    while True:
        # -- font --
        text_l = myfont.render(score_l, False, white)
        text_r = myfont.render(score_r, False, white)

        lab.fill(black)
        lab.blit(text_l, (200, 150))
        lab.blit(text_r, (game_width - 200, 150))

        # -- limit --
        if p1_height <= 0:
            p1_height = 1
        elif (p1_height + 50) >= game_height:
            p1_height = game_height-51
        if p2_height <= 0:
            p2_height = 1
        elif (p2_height + 50) >= game_height:
            p2_height = game_height-51

        # -- middle line --
        pygame.draw.line(lab, white, [game_width/2, 50], [game_width/2, game_height-50])

        # -- paddle1 left --
        pygame.draw.line(lab, white, [p1_x, p1_height], [p1_x, p1_height+50], 10)

        # -- paddle2 right --
        pygame.draw.line(lab, white, [p2_x, p2_height], [p2_x, p2_height+50], 10)

        # -- ball --
        pygame.draw.circle(lab, white, [int(ball_x), int(ball_y)], 4)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    LeftUp = True
                if event.key == pygame.K_s:
                    LeftDown = True
                if event.key == pygame.K_UP:
                    RightUp = True
                if event.key == pygame.K_DOWN:
                    RightDown = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    LeftUp = False
                if event.key == pygame.K_s:
                    LeftDown = False
                if event.key == pygame.K_DOWN:
                    RightDown = False
                if event.key == pygame.K_UP:
                    RightUp = False
        if one:
            move()
        else:
            # -- movement --
            time.sleep(0.01)
            if LeftUp:
                p1_height -= pspeed
            if LeftDown:
                p1_height += pspeed
            if RightUp:
                p2_height -= pspeed
            if RightDown:
                p2_height += pspeed

            ball_x += ball_speed_x
            ball_y += ball_speed_y

        if ball_y <= 0:
            ball_speed_y *= -1
            winsound.Beep(400, 30)
        if ball_y >= game_height:
            ball_speed_y *= -1
            winsound.Beep(400, 30)

        if (p2_x+5 >= (ball_x + 4) >= p2_x) and ((p2_height+50) >= ball_y >= p2_height):
            ball_speed_x *= -1
            x += 1
            winsound.Beep(400, 30)
        if (p1_x-5) <= (ball_x - 4) <= p1_x and ((p1_height+50) >= ball_y >= p1_height):
            ball_speed_x *= -1
            x += 1
            winsound.Beep(400, 30)
        if x % 6 == 0:
            ball_speed_x += 1 * (ball_speed_x / abs(ball_speed_x))
            ball_speed_y += 1 * (ball_speed_y / abs(ball_speed_y))
            x += 1
        print(x)
        print(ball_speed_x)
        if x % 6 == 0:
            ball_speed_x += 1 * (ball_speed_x / abs(ball_speed_x))
            ball_speed_y += 1 * (ball_speed_y / abs(ball_speed_y))
            x += 1
        if ball_x < 0:
            score_r = str(int(score_r) + 1)
            again()
        if ball_x > game_width:
            score_l = str(int(score_l) + 1)
            again()
        if ball_x < 0:
            score_r = str(int(score_r) + 1)
            again()
        if ball_x > game_width:
            score_l = str(int(score_l) + 1)
            again()


# -- start again --
def again():
    global ball_x, ball_y, ball_speed_y, ball_speed_x, x, random_x, random_y
    random_x = random.choice([1, -1])
    random_y = random.choice([1, -1])
    ball_x = 400
    ball_y = 250
    x = 1
    ball_speed_y = 2 * random_y
    ball_speed_x = 2 * random_x


# -- start function --
def start_state():
    while True:
        # lab.fill(white)
        start_text = startfont.render("how many players? 1 / 2", False, white)
        lab.blit(start_text, (int(0), 0))
        print(2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            print(4)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    one(True)
                elif event.key == pygame.K_2:
                    one(False)


# -- main loop --
start_state()
