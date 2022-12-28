#k8 2:27:45

import pygame as pg

class Pilota:
    def __init__(self, pos_x, pos_y, radio=20, color=(255,255,255), vx=1, vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radio = radio
        self.color = color
        self.vx = vx
        self.vy = vy
        self.contadorDrt = 0
        self.contadorEsq = 0
        font = pg.font.Font(None,40) 

        
    def dibuixar (self,pantalla):
        pg.draw.circle (pantalla, self.color, (self.pos_x, self.pos_y), self.radio)

    def moure (self, xmax=800, ymax=600):
        self.pos_x += self.vx
        self.pos_y += self.vy

        print ("posició X:",self.pos_x+self.radio)
        print ("posició Y:",self.pos_y+self.radio)

        #canviem pq si es maca gol a un costat reboti exactament pel sentit contari
        if self.pos_y >= ymax-self.radio or self.pos_y < 0+self.radio:
            self.vy *= -1

        #la pilota desapareix uns pocs segons quan fa gol (límit de y)
        if self.pos_x >= xmax+self.radio*10: #límit dr
            self.contadorEsq += 1
            self.vx *= -1 
            self.yx *= -1 

        if self.pos_x < 0+self.radio*10: #límit esq
            self.contadorDrt += 1
            self.vx *= -1 
            self.yx *= -1 

    def marcador (self,pantalla_principal):
        marcadorEsq = self.font.render("jugador 1"+str(self.contadorDrt), 0, (255,255,0))
        marcadorDrt = self.font.render("jugador 2"+str(self.contadorEsq), 0, (255,255,0))

        pantalla_principal.blit(marcadorDrt,(200,50))
        pantalla_principal.blit(marcadorEsq,(600,50))

    def posX (self):
        return self.pos_x+self.radio
    def posY (self):
        return self.pos_y+self.radio
   
    def Esq (self):
        if self.pos_x < 400:
            return True
        return False
   
    def Drt (self):
        if self.pos_x > 400:
            return True
        return False

    def Up (self):
        if self.pos_y < 300:
            return True
        return False  

    def Down (self):
        if self.pos_y > 300:
            return True
        return False  

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