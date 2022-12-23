from figura_class import Pilota, Raqueta
import pygame as pg

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")

pilota = Pilota (400,300)
raqueta1 = Raqueta (300,0)
raqueta2 = Raqueta (775,300)

game_over = False

while not game_over:
    for eventos in pg.event.get():
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    estat_tecles = pg.key.get_pressed()

    if estat_tecles [pg.K_UP] == True:
        raqueta1.pos_y -= 1
    if estat_tecles [pg.K_DOWN] == True:
        raqueta1.pos_y += 1

    pantalla_principal.fill((0,130,95))
    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), width=2)

    pilota.dibuixar (pantalla_principal)
    raqueta1.dibuixar (pantalla_principal)
    raqueta2.dibuixar (pantalla_principal)

""""
    pilota.moure (pantalla_principal)
    raqueta1.moure (pantalla_principal)
    raqueta2.moure (pantalla_principal)
"""
pg.display.flip()

