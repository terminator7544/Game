from pygame import *

#https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
class Button():
    def __init__(self,imag,size,dest,win,ctl,command=''):
        self.size = size
        self.bt_img = transform.scale(image.load(imag),self.size)
        self.rect = self.bt_img.get_rect()
        self.dest = dest
        self.win = win
        self.command = command
        self.ctl = ctl
    def update(self):
        self.win.blit(self.bt_img,self.dest)
    def activate(self,events):
        mouse_pos = mouse.get_pos()
        for e in events:
            if mouse_pos[0] > self.dest[0]:
                if mouse_pos[1] > self.dest[1]:
                    if mouse_pos[0]< self.dest[0]+self.size[0]:
                        if mouse_pos[1] < self.dest[1]+self.size[1]:
                            if e.type == MOUSEBUTTONDOWN:
                                if self.command != '':
                                    if self.ctl:
                                        self.command(self.win)
                                    else:
                                        self.command()


class Text():
    def __init__(self,name,size,color,dest,win,text):
        self.name = name
        self.size = size
        self.text = text
        self.color = color
        self.dest = dest
        self.win = win
        self.f = font.SysFont(self.name, self.size, False)
        self.t = self.f.render(self.text, 1, self.color)
    def update(self):
        self.win.blit(self.t,self.dest)

class Input_Field(Text):
    def __init__(self,name,size,color,dest,win,text='',size_l =(10,10),limit =7):
        Text.__init__(self,name,size,color,dest,win,text)
        self.is_active = False
        self.size_l = size_l
        self.limit = limit
        self.c_limit = 0
    def update(self):
        self.t = self.f.render(self.text, 0, self.color)
        self.win.blit(self.t, self.dest)
    def activate(self,events):
        mouse_pos = mouse.get_pos()
        for e in events:
            if mouse_pos[0] > self.dest[0]:
                if mouse_pos[1] > self.dest[1]:
                    if mouse_pos[0]< self.dest[0]+self.size_l[0]:
                        if mouse_pos[1] < self.dest[1]+self.size_l[1]:
                            if e.type == MOUSEBUTTONDOWN:
                                self.is_active = not self.is_active
                                print(self.is_active)
            if self.is_active:
                if self.c_limit < self.limit:
                    if e.type == TEXTINPUT:
                        self.c_limit += 1
                        self.text += e.text
                if self.c_limit > 0:
                    if e.type == KEYUP:
                        if e.key == 8:
                            self.text = self.text[0:len(self.text) - 1]
                            self.c_limit -= 1



class GameObject(sprite.Sprite):
    def __init__(self,win,imagem,size,x,y):
        super().__init__()
        self.win = win
        self.size = size
        self.image = transform.scale(image.load(imagem),self.size)
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.win.blit(self.image,(self.rect.x,self.rect.y))

class Ball(GameObject):
    colors = ['blue.png','green.png','red.png','violet.png','white.png','yellow.png']
    def __init__(self,win,size,x,y,color=1):
        self.color = color
        imagem = 'resources/bals/'+Ball.colors[self.color]
        super().__init__(win,imagem,size,x,y)

