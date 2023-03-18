import numpy as np
import math 
import pygame as pg
import sys
import keyboard
from pygame.locals import *

def foo():
     for i in pg.event.get():
         
         if i.type == QUIT:
             pg.quit()
             sys.exit()
         if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1 :
                matrix[round((i.pos[1]-20)/40)][round((i.pos[0]-20)/40)] = 1
                matrix1[round((i.pos[1]-20)/40)][round((i.pos[0]-20)/40)] = 1
                
                vivod(round((i.pos[0]-20)/40),round((i.pos[1]-20)/40))
                pg.display.update()

def vivod(x,y):
     if matrix1[y][x] == 1:
                    pg.draw.rect(sc, (LIGHT_BLUE), 
                                 (x*40+2,y*40+2, 38, 38))
     if matrix1[y][x] == 0:
                    pg.draw.rect(sc, (BLACK), 
                                 (x*40+2,y*40+2, 38, 38))
     

def proverka(xpx,ypx):
     col_pix = 0
     if matrix[ypx][xpx-1] == 1:
          col_pix +=1
     if matrix[ypx][xpx+1] == 1:
          col_pix +=1
     if matrix[ypx-1][xpx] == 1:
          col_pix +=1
     if matrix[ypx+1][xpx] == 1:
          col_pix +=1
     if matrix[ypx-1][xpx-1] == 1:
          col_pix +=1
     if matrix[ypx+1][xpx-1] == 1:
          col_pix +=1
     if matrix[ypx-1][xpx+1] == 1:
          col_pix +=1
     if matrix[ypx+1][xpx+1] == 1:
          col_pix +=1
     return col_pix

def clear():
     xl,yl = 0,0
     sc.fill(BLACK)
     for i in range(25):
          pg.draw.line(sc, WHITE, 
                 [xl, yl], 
                 [xl, yl+H], 2)
          xl += 40

     xl,yl = 0,0
     for j in range(16):
          pg.draw.line(sc, WHITE, 
                 [xl, yl], 
                 [xl+W, yl], 2)
          yl += 40

matrix = np.zeros((16,16))
matrix1 = np.zeros((16,16))

W,H = 600,600
xl,yl,xm,ym = 0,0,0,0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

pg.init()
sc = pg.display.set_mode((W,H))
pg.display.set_caption('Game of Life')

clear()

col_pix = 0

while True: 
     keys = pg.key.get_pressed()
     if keys[pg.K_SPACE]:
          clear()
          x,y = 0,0
          for i in range(15):
               for j in range(15):
                    col_pix = proverka(x,y)
                    if matrix[y][x] == 0:
                         if col_pix >= 3:
                              matrix1[y][x] = 1
                         if col_pix < 3:
                              matrix1[y][x] = 0
                    if matrix[y][x] == 1:
                         if col_pix == 3 or col_pix == 2:
                              matrix1[y][x] = 1
                         if col_pix != 3 and col_pix != 2:
                              matrix1[y][x] = 0
                    vivod(x,y)
                    x += 1
                    pg.time.delay(3)
               y += 1
               x = 0
          matrix = matrix1
          matrix1 = np.zeros((16,25))
          pg.display.update()
     foo()
     if keys[pg.K_r]:
          x,y = 0,0
          matrix = np.zeros((16,16))
          matrix1 = np.zeros((16,16))
          for i in range(15):
               for j in range(15):
                    vivod(x,y)
                    x += 1
               x = 0
               y += 1
