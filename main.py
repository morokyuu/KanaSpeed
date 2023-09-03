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
FRAME_RATE = 30




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




class Status(Enum):
    WAIT = 0,
    COUNTDOWN = 1,
    RECEIVE = 2,
    ANSWER = 3


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
        return False


class ReceiveState(GameState):
    def __init__(self):
        self.countd = CountDisplay()
        self.count = 0

    def do(self):
        DISPLAYSURF.fill(WHITE)
        self.count += 1
        self.countd.change(self.count)
        if self.count > 5000:
            return True

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
        return False

class CountdownState(GameState):
    def __init__(self):
        self.fontd = FontDisplay()
        self.timer = 0
        self.msg = ['はじめ','1','2','3']

    def do_fontdown(self):
        WIDTH = 180
        pygame.draw.rect(DISPLAYSURF, GRAY, pygame.Rect(0, 0, WIDTH, WINDOWSIZE[1]))
        pygame.draw.rect(DISPLAYSURF, GRAY, pygame.Rect(WINDOWSIZE[0] - WIDTH, 0, WIDTH, WINDOWSIZE[1]))

    def do(self):
        DISPLAYSURF.fill(WHITE)

        if self.timer % FRAME_RATE == 0:
            if self.msg:
                char = self.msg.pop()
                self.fontd.change(char)
            else:
                return True

        self.timer += 1
        self.fontd.draw()

        keyname,shift = self.input_key()
        return False

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
            return True
        return False

    def transition(self):
        return CountdownState()



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
        if g.do():
            g = g.transition()
        clock.tick(FRAME_RATE)
        pygame.display.flip()

