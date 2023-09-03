##
## required version
##   python 3.10
##   pygame 2.4.0
##
from pygame.locals import *
import pygame
import sys
import os
import time
import glob
from enum import Enum
import re
import random

BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
GREEN = (0, 255, 0)
BLUE = (0, 0, 123)
WHITE = (255, 255, 255)

WINDOWSIZE = (640,480)




class Display:
    def __init__(self,char="こんにちは"):
        self.font = pygame.font.SysFont('yugothicuisemibold', 70)
        self.charSurfaceObj = self.font.render(char, True, GREEN, BLUE)
        self.charRectObj = self.charSurfaceObj.get_rect()
        self.charRectObj.center = (300, 300)

    def draw(self):
        DISPLAYSURF.blit(self.charSurfaceObj,self.charRectObj)


class FontDisplay(Display):
    def __init__(self):
        super().__init__()

    def change(self,char):
        self.charSurfaceObj = self.font.render(f"{char}", True, GREEN, BLUE)
        self.charRectObj = self.charSurfaceObj.get_rect()
        self.charRectObj.center = (300, 300)


class CountDisplay(Display):
    def __init__(self):
        super().__init__()
        self.count = 0

    def change(self,char):
        self.charSurfaceObj = self.font.render(f"{char}", True, GREEN, BLUE)
        self.charRectObj = self.charSurfaceObj.get_rect()
        self.charRectObj.center = (300, 300)

    def draw(self):
        for i in range(3,0,-1):
            print(i)
            time.sleep(1)

class Status(Enum):
    WAIT = 0,
    COUNTDOWN = 1,
    RECEIVE = 2,
    ANSWER = 3

def do_countdown():
    WIDTH = 180
    pygame.draw.rect(DISPLAYSURF,GRAY,pygame.Rect(0,0,WIDTH,WINDOWSIZE[1]))
    pygame.draw.rect(DISPLAYSURF,GRAY,pygame.Rect(WINDOWSIZE[0]-WIDTH,0,WIDTH,WINDOWSIZE[1]))

class GameState:
    def _halt(self):
        pygame.quit()
        sys.exit()

    def input_key(self):
        keyname = None
        shift = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._halt()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._halt()
                else:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        shift = True
                    keyname = pygame.key.name(event.key)
        return keyname,shift

    def do(self):
        return True
    

class WaitState(GameState):
    def __init__(self):
        fontObj = pygame.font.SysFont('yugothicuisemibold', 40)
        self.textSurfaceObj = fontObj.render("なにがとおったでしょうゲーム", True, GREEN, BLUE)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (300, 200)

        self.fontd = FontDisplay()
        #self.countd = CountDisplay()
        #self.state = Status.COUNTDOWN

    def do(self):
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(self.textSurfaceObj,self.textRectObj)

        keyname,shift = self.input_key()
        if keyname is None:
            pass
        else:
            return False
        return True

class CountdownState(GameState):
    def __init__(self):
        fontObj = pygame.font.SysFont('yugothicuisemibold', 40)
        self.textSurfaceObj = fontObj.render("なにがとおったでしょうゲーム", True, GREEN, BLUE)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (300, 200)

        self.fontd = FontDisplay()
        #self.countd = CountDisplay()
        #self.state = Status.COUNTDOWN

    def do(self):
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(self.textSurfaceObj,self.textRectObj)

        keyname,shift = self.input_key()
        if keyname is None:
            pass
        else:
            if keyname == 'space':
                print("========space")
                pass
            elif keyname == 'return':
                print("========return")
            else:
                print(f"key={keyname}")


if __name__ == '__main__':
    pygame.init()
    flags = pygame.FULLSCREEN
    #DISPLAYSURF = pygame.display.set_mode(size=WINDOWSIZE, display=0, depth=32, flags=pygame.FULLSCREEN)
    DISPLAYSURF = pygame.display.set_mode(size=WINDOWSIZE, display=0, depth=32)
    pygame.display.set_caption('Kana Speed')
    clock = pygame.time.Clock()
    state = Status.WAIT

    g = WaitState()
    while True:
        if state == Status.WAIT:
            pass
        elif Status.COUNTDOWN:
            pass
        elif Status.RECEIVE:
            pass
        elif Status.ANSWER:
            pass
        clock.tick(30)
        pygame.display.flip()

