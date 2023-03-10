#importem classe i pg
from figura_class import Pilota, Raqueta
import pygame as pg

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")

#definir la tasa de refresc del nostre bucle de fotogrames (fps= fotogrames per segon)
cronometre = pg.time.Clock()

#creem objectes
pilota = Pilota (400,300)
raqueta1 = Raqueta (10,300)
raqueta2 = Raqueta (790,300)

raqueta1.vy = 6
pilota.vx = 4

game_over = False

pantalla_principal.fill((0,130,95)) #pintar pantalla

while not game_over:
    # imprimir els milisegosnq triguen els fotogrames actualment
    vt = cronometre.tick(300) # variable per controlar velicitat entre fotogrames
    # print (vt)

    for eventos in pg.event.get():
        #print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    #pilota.comprovar_xoc (raqueta1, raqueta2)
    pilota.comprovar_xoc_V2 (raqueta1, raqueta2)

    pilota.marcador(pantalla_principal)
    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), width=2) #pintar línia mig

    pilota.dibuixar (pantalla_principal)
    raqueta1.dibuixar (pantalla_principal)
    raqueta2.dibuixar (pantalla_principal)

    raqueta1.moure (pg.K_w,pg.K_s)
    raqueta2.moure (pg.K_UP,pg.K_DOWN)
    pilota.moure ()

    pg.display.flip()