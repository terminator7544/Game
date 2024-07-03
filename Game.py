from pygame import *
Game = True

def Game(win):
    pass

def App():
    global Game
    clock = time.Clock()
    win = display.set_mode((1000,600))
    display.set_caption("ZUMA")
    while Game:
        events = event.get()
        for e in events:
            if e.type == QUIT:
                Game = False
        display.update()
        clock.tick(60)