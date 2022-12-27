import pygame as pg

class Pilota:
    def __init__(self, pos_x, pos_y, radio=20, color=(255,255,255), vx=1, vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radio = radio
        self.color = color
        self.vx = vx
        self.vy = vy

    def dibuixar (self,pantalla):
        pg.draw.circle (pantalla, self.color, (self.pos_x, self.pos_y), self.radio)

    def moure (self, xmax=800, ymax=600):
        self.pos_x += self.vx
        self.pos_y += self.vy
        #canviem pq si es maca gol a un costat reboti exactament pel sentit contari

        #la pilota desapareix uns pocs segons quan fa gol (límit de y)
        if self.pos_x >= xmax+self.radio*10 or self.pos_x < 0+self.radio*10:
            #contar gol
            
            self.vx *= -1 
            self.yx *= -1 

"""
        if self.pos_x >= xmax-self.radio or self.pos_x < 0+self.radio:
            self.vx *= -1 

        if self.pos_y >= ymax-self.radio or self.pos_y < 0+self.radio:
            self.vy *= -1 
"""

class Raqueta:
    def __init__(self, pos_x, pos_y, w=20, h=100, color=(255,255,255), vx=1, vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy

    def dibuixar (self,pantalla):
        pg.draw.rect (pantalla, self.color, (self.pos_x-(self.w/2), self.pos_y-(self.h/2), self.w, self.h))

    def moure (self, tecla_up, tecla_down, ymax=600, ymin=0):
        estat_tecles = pg.key.get_pressed() #retorna llista de tecles -> funció q indica l'estat del teclat

        if estat_tecles [tecla_up] == True and self.pos_y > (ymin+self.h//2):
            self.pos_y -= 1
        if estat_tecles [tecla_down] == True and self.pos_y < (ymax-self.h//2):
            self.pos_y += 1

"""       
        if estat_tecles [tecla_up] == True:
            self.pos_y -= self.vy
        
        if self.pos_y < self.h // 2:
            self.pos_y = self.h // 2

        if estat_tecles [tecla_down] == True:
            self.pos_y += self.vy
        
        if self.pos_y < self.h // 2:
            self.pos_y = self.h // 2
"""

