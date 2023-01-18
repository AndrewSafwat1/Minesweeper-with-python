from pygame import display
import pygame as pg
import time
import random
import numpy as np

start_time = time.time()

MINE = 100
CURSOR_ON = (185, 222, 118)
TIME_COLOR = (74, 117, 44)
WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (254, 254, 254)
BLACK = (0, 0, 0)
W_GREEN = (170, 215, 81)
D_GREEN = (140, 197, 33)
RED = (215, 0, 64)
EMPTY_W = (229, 194, 159)
EMPTY_D = (215, 184, 153)

lost = 1

flag_dark = pg.image.load('pictures/flag_dark.png')
flag_dark = pg.transform.scale(flag_dark, (30, 30))

flag_white = pg.image.load('pictures/flag_white.png')
flag_white = pg.transform.scale(flag_white, (30, 30))

bomb = pg.image.load('pictures/bomb.png')
bomb = pg.transform.scale(bomb, (30, 30))

picture1 = pg.image.load('pictures/1.png')
picture1 = pg.transform.scale(picture1, (30, 30))

picture2 = pg.image.load('pictures/2.png')
picture2 = pg.transform.scale(picture2, (30, 30))

picture3 = pg.image.load('pictures/3.png')
picture3 = pg.transform.scale(picture3, (30, 30))

picture4 = pg.image.load('pictures/4.png')
picture4 = pg.transform.scale(picture4, (30, 30))

picture5 = pg.image.load('pictures/5.png')
picture5 = pg.transform.scale(picture5, (30, 30))

picture6 = pg.image.load('pictures/6.png')
picture6 = pg.transform.scale(picture6, (30, 30))

picture7 = pg.image.load('pictures/7.png')
picture7 = pg.transform.scale(picture7, (30, 30))

picture8 = pg.image.load('pictures/8.png')
picture8 = pg.transform.scale(picture8, (30, 30))


pg.init() # now use display and fonts

status = np.zeros(18*14, dtype=np.int64)
status = status.reshape(14, 18)

counter = 1
while(counter <= 40):
    y = random.randrange(0, 14)
    x = random.randrange(0, 18)
    if(status[y][x] == MINE):
        continue
        
    else:
        status[y][x] = MINE 
        counter += 1 

appear = status == 9
flag = status == 9

for i in range(0, 14):
    for j in range(0, 18):
        if(status[i][j] == MINE):
            continue
        else:
            if(i == 0 and j == 0):
                if(status[i + 1][j] == MINE):
                    status[i][j] += 1
                if(status[i + 1][j + 1] == MINE):
                    status[i][j] += 1
                if(status[i][j + 1] == MINE):
                    status[i][j] += 1

            elif(i == 0 and j == 17):
                if(status[i + 1][j] == MINE):
                    status[i][j] += 1
                if(status[i + 1][j - 1] == MINE):
                    status[i][j] += 1
                if(status[i][j - 1] == MINE):
                    status[i][j] += 1
            
            elif(i == 13 and j == 17):
                if(status[i - 1][j] == MINE):
                    status[i][j] += 1
                if(status[i - 1][j - 1] == MINE):
                    status[i][j] += 1
                if(status[i][j - 1] == MINE):
                    status[i][j] += 1

            elif(i == 13 and j == 0):
                if(status[i - 1][j] == MINE):
                    status[i][j] += 1
                if(status[i - 1][j + 1] == MINE):
                    status[i][j] += 1
                if(status[i][j + 1] == MINE):
                    status[i][j] += 1
            
            elif(j == 0):
                if(status[i + 1][j] == MINE):
                    status[i][j] += 1
                if(status[i - 1][j] == MINE):
                    status[i][j] += 1
                if(status[i][j + 1] == MINE):
                    status[i][j] += 1
                if(status[i - 1][j + 1] == MINE):
                    status[i][j] += 1
                if(status[i + 1][j + 1] == MINE):
                    status[i][j] += 1

            elif(j == 17):
                if(status[i + 1][j] == MINE):
                    status[i][j] += 1
                if(status[i - 1][j] == MINE):
                    status[i][j] += 1
                if(status[i][j - 1] == MINE):
                    status[i][j] += 1
                if(status[i - 1][j - 1] == MINE):
                    status[i][j] += 1
                if(status[i + 1][j - 1] == MINE):
                    status[i][j] += 1

            elif(i == 0):
                if(status[i][j - 1] == MINE):
                    status[i][j] += 1
                if(status[i][j + 1] == MINE):
                    status[i][j] += 1
                if(status[i + 1][j - 1] == MINE):
                    status[i][j] += 1
                if(status[i + 1][j + 1] == MINE):
                    status[i][j] += 1
                if(status[i + 1][j] == MINE):
                    status[i][j] += 1

            elif(i == 13):
                if(status[i][j - 1] == MINE):
                    status[i][j] += 1
                if(status[i][j + 1] == MINE):
                    status[i][j] += 1
                if(status[i - 1][j - 1] == MINE):
                    status[i][j] += 1
                if(status[i - 1][j + 1] == MINE):
                    status[i][j] += 1
                if(status[i - 1][j] == MINE):
                    status[i][j] += 1

            else:
                if(status[i - 1][j - 1] == MINE):
                    status[i][j] += 1
                if(status[i - 1][j + 1] == MINE):
                    status[i][j] += 1
                if(status[i - 1][j] == MINE):
                    status[i][j] += 1
                if(status[i][j + 1] == MINE):
                    status[i][j] += 1
                if(status[i][j - 1] == MINE):
                    status[i][j] += 1
                if(status[i + 1][j - 1] == MINE):
                    status[i][j] += 1
                if(status[i + 1][j + 1] == MINE):
                    status[i][j] += 1
                if(status[i + 1][j] == MINE):
                    status[i][j] += 1

font = pg.font.Font('font/Roboto-Bold.ttf', 20)

text = font.render('Time : ', True, WHITE)
textRect = text.get_rect()
textRect.left = (15)
textRect.top = (5)

lose = font.render('You have lost', True, RED)
loseRect = lose.get_rect()
loseRect.center = (270, 15)

win = font.render('You have won', True, WHITE)
winRect = win.get_rect()
winRect.center = (270, 15)


def check(row, column): #if a space was clicked, free all spaces around it
    if(column > 17 or column < 0 or row > 13 or row < 0 or appear[row][column] == True):
        return

    elif(status[row][column] != 0):
        appear[row][column] = True
        return

    else:
        appear[row][column] = True
        check(row - 1, column)
        check(row, column + 1)
        check(row + 1, column)
        check(row, column - 1)

window = display.set_mode((540, 450))
pg.display.set_caption("Minesweeper")
pygame_icon = pg.image.load('pictures/icon.png')
pg.display.set_icon(pygame_icon)

 

clock = pg.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    pg.draw.rect(window, TIME_COLOR, pg.Rect(0, 0, 540, 30))
    # window.fill(TIME_COLOR)

    
    window.blit(text, textRect)

    if(lost):
        ingame_time = font.render(str(int(time.time() - start_time)), True, WHITE)

    timeRect = ingame_time.get_rect()
    timeRect.left = (75)
    timeRect.top = (5)

    window.blit(ingame_time, timeRect)

    counter = -1



# for printing the board
    for i in range(30, 450, 30):
        for j in range(0, 540, 30):
            if(counter == 1 and appear[(i - 30) // 30][j // 30] == False and flag[(i - 30) // 30][j // 30] == False): #normal board
                pg.draw.rect(window, W_GREEN, pg.Rect(j, i, 30, 30))

            elif (counter == -1 and appear[(i - 30) // 30][j // 30] == False and flag[(i - 30) // 30][j // 30] == False):
                pg.draw.rect(window, D_GREEN, pg.Rect(j, i, 30, 30))

            elif(counter == 1 and appear[(i - 30) // 30][j // 30] == False and flag[(i - 30) // 30][j // 30]): #for flag
                window.blit(flag_white, (j, i))

            elif(counter == -1 and appear[(i - 30) // 30][j // 30] == False and flag[(i - 30) // 30][j // 30]):
                window.blit(flag_dark, (j, i))

            elif(status[(i - 30) // 30][j // 30] == MINE): #bomb
                window.blit(bomb, (j, i))
                # pg.time.wait(0.25)
                lost = 0
                window.blit(lose, loseRect)
                

            elif(counter == 1 and status[(i - 30) // 30][j // 30] == 0): #empty 
                pg.draw.rect(window, EMPTY_W, pg.Rect(j, i, 30, 30))

            elif(counter == -1 and status[(i - 30) // 30][j // 30] == 0): #empty 
                pg.draw.rect(window, EMPTY_D, pg.Rect(j, i, 30, 30))
            
            elif(status[(i - 30) // 30][j // 30] == 1): #1 
                window.blit(picture1, (j, i))

            elif(status[(i - 30) // 30][j // 30] == 2): #2 
                window.blit(picture2, (j, i))

            elif(status[(i - 30) // 30][j // 30] == 3): #3 
                window.blit(picture3, (j, i))

            elif(status[(i - 30) // 30][j // 30] == 4): #4 
                window.blit(picture4, (j, i))

            elif(status[(i - 30) // 30][j // 30] == 5): #5
                window.blit(picture5, (j, i))

            elif(status[(i - 30) // 30][j // 30] == 6): #6 
                window.blit(picture6, (j, i))

            elif(status[(i - 30) // 30][j // 30] == 7): #7 
                window.blit(picture7, (j, i))

            elif(status[(i - 30) // 30][j // 30] == 8): #8 
                window.blit(picture8, (j, i))
            
            elif(np.count_nonzero(appear == False) == 40):
                lost = 0
                window.blit(win, winRect)       


            if (j // 30 != 17):
                counter *= -1

    cursor = pg.mouse.get_pos()
    cursor_x = cursor[0] - cursor[0] % 30
    cursor_y = cursor[1] - cursor[1] % 30

    if (((cursor_y - 30) // 30 < 14) and cursor[1] >= 40 and appear[(cursor_y - 30) // 30][cursor_x // 30] == False and lost and flag[(cursor_y - 30) // 30][cursor_x // 30] == False):
            pg.draw.rect(window, CURSOR_ON, pg.Rect(cursor_x, cursor_y, 30, 30))

    left_click = pg.mouse.get_pressed()[0]
    right_click = pg.mouse.get_pressed()[2]
    # click = event.type == pg.MOUSEBUTTONUP //i think it is better
    if(left_click and cursor[1] >= 40 and (cursor_y - 30) // 30 < 14 and status[(cursor_y - 30) // 30][cursor_x // 30] == 0 and lost): #if space
            # check for other spaces
            check((cursor_y - 30) // 30, cursor_x // 30)

    elif(left_click and cursor[1] >= 40 and (cursor_y - 30) // 30 < 14 and lost):
            appear[(cursor_y - 30) // 30][cursor_x // 30] = True
    
    elif(right_click and cursor[1] >= 40 and (cursor_y - 30) // 30 < 14 and lost):
        flag[(cursor_y - 30) // 30][cursor_x // 30] = True




    pg.display.flip()    
