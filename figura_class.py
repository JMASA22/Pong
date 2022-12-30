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
            #reapareixi pilota a centre després de gol
            self.pos_x = xmax//2
            self.pos_y = ymax//2
            #pq reboti
            self.vx *= -1 
            self.vy *= -1 
            
        if self.pos_x < 0+self.radio*10: #límit esq
            self.contadorDrt += 1
            #reapareixi pilota a centre després de gol
            self.pos_x = xmax//2
            self.pos_y = ymax//2
            #pq reboti
            self.vx *= -1 
            self.vy *= -1 

    def marcador (self,pantalla_principal):
        marcadorEsq = self.font.render("jugador 1"+str(self.contadorDrt), 0, (255,255,0))
        marcadorDrt = self.font.render("jugador 2"+str(self.contadorEsq), 0, (255,255,0))

        pantalla_principal.blit(marcadorDrt,(200,50))
        pantalla_principal.blit(marcadorEsq,(600,50))
    
    @property #pq la funció actui com a variable 
    def Esq (self):
        return self.pos_x - self.radio
    @property
    def Drt (self):
        return self.pos_x + self.radio
    @property
    def Up (self):
        return self.pos_y - self.radio
    @property
    def Down (self):
        return self.pos_y + self.radio

    def comprovar_xoc (self,r1, r2): #lògica de xoc
        if self.Drt >= r2.Esq and \
        self.Esq <= r2.Drt and \
        self.Down >= r2.Up and \
        self.Up <= r2.Down:
            self.vx *= -1

        if self.Drt >= r1.Esq and \
        self.Esq <= r1.Drt and \
        self.Down >= r1.Up and \
        self.Up <= r1.Down:
            self.vx *= -1

    def comprovar_xoc_V2 (self,*raquetes): #lògica de xoc V2 / * significa q ho imprimirà com una array d'objectes
       for r in raquetes:
            if self.Drt >= r.Esq and \
               self.Esq <= r.Drt and \
               self.Down >= r.Up and \
               self.Up <= r.Down:
                    self.vx *= -1
                    return #acabar sentencia "for" (tmb es pot fer amb break)
 
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

    @property
    def Up (self):
        return self.pos_y - self.h//2
    @property
    def Down (self):
        return self.pos_y + self.h//2
    @property  
    def Esq (self):
        return self.pos_x - self.w//2
    @property  
    def Drt (self):
        return self.pos_x + self.w//2

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