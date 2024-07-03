from pygame import *
from classes import Button,GameObject,Ball


Game = True
win = display.set_mode((1000,600))

b = Ball(win,(60,60),200,200,1)


def Game(win):
    pass

def updates():
    global b
    b.update()

def App():
    global Game
    global win
    clock = time.Clock()
    display.set_caption("ZUMA")
    while Game:
        events = event.get()
        for e in events:
            if e.type == QUIT:
                Game = False
        updates()
        display.update()
        clock.tick(60)