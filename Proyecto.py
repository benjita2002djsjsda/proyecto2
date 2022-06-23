# Se usa para los input,display y cargar imagenes y para isntalarlo se ulitiza el comando en vscode: python3 -m pip install -U pygame --user.
import pygame
import ctypes as ct
import random
# Se define las clases, movimientos en sentido de X e Y de el personaje.
nRES = (720, 720)
x = True
pygame.init
pygame.mixer.init()
pygame.font.init()
sonido_juego = pygame.mixer.Sound("Fondomusica.mp3")
pygame.mixer.Sound.set_volume(sonido_juego, 0.1)
pygame.mixer.Sound.play(sonido_juego, -1)
menu = True


class player(ct.Structure):
    _fields_ = [('Xvaquero', ct.c_short), ('Yvaquero', ct.c_short),
                ('clase ', ct.c_short), ('Movimientoizq', ct.c_short),
                ('Movimientoarr', ct.c_short), ('Movimientoaba', ct.c_short),
                ('Movimientoder', ct.c_short)]


class enemigo(ct.Structure):
    _fields_ = [('Xenemigo', ct.c_short), ('Yenemigo', ct.c_short),
                ('Lifeenemigo', ct.c_short), ('Velenemigo', ct.c_short),
                ('Spawnenemigo', ct.c_short), ('Anienemigo', ct.c_short),
                ('dirXenemigo', ct.c_short), ('dirYenemigo', ct.c_short),
                ('Recenemigo', ct.c_short), ('dispenemigo', ct.c_short)]


class bullet(ct.Structure):
    _fields_ = [('Xbala', ct.c_short), ('Ybala', ct.c_short),
                ('DXbala', ct.c_short), ('DYbala', ct.c_short),
                ('Pinbala', ct.c_bool)]


# Entrada:Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida:Retorna el sonido.
def sound_gun():
    pygame.mixer.init()
    sonido_bala = pygame.mixer.Sound("disparoxd.mp3")
    pygame.mixer.Sound.set_volume(sonido_bala, 0.2)
    pygame.mixer.Sound.play(sonido_bala, 0)
    return


# Entrada:Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida:Retorna el sonido.
def sound_pausa():
    pygame.mixer.init()
    sonido_pausa = pygame.mixer.Sound("Pausa.mp3")
    pygame.mixer.Sound.set_volume(sonido_pausa, 0.2)
    pygame.mixer.Sound.play(sonido_pausa, 0)
    return


# Entrada:int sFile,int transp=False.
# Salida:int image,retorna a image.
def Load_Image(sFile, transp=False):
    try:
        image = pygame.image.load(sFile)
    except pygame.error.message:
        raise SystemExit.message
    image = image.convert()
    if transp:
        color = image.get_at((0, 0))
        image.set_colorkey(color)
    return image


# Entrada: Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida: int pygame.display.set_mode(nRES).
def PyGame_Init():
    pygame.init()
    pygame.display.set_caption("Proyecto Benja y Amaro")
    return pygame.display.set_mode(nRES)


# Entrada: Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida: int img, retorna la lista vacia.
def Carga_imagenes():
    img = []
    img.append(Load_Image("farmer3.png", True))
    img.append(Load_Image("ripcarlos.png", True))
    img.append(Load_Image("Suelo.png", False))
    img.append(Load_Image("Suelo1.png", False))
    img.append(Load_Image("Suelo2.png", False))
    img.append(Load_Image("fence.png", False))
    img.append(Load_Image("bullet.png", False))
    img.append(Load_Image("ripcarlos2.png", True))
    img.append(Load_Image("menu.png", False))
    return img


# Entrada:Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida:Inicia a nuestro vaquero(personaje).
def Farmer_Init():
    vaquero.Xvaquero = 360
    vaquero.Yvaquero = 360
    vaquero.clase = 1
    vaquero.MovimientoX = 0
    vaquero.MovimientoY = 0  # Movimiento (derecha, izquierda)
    vaquero.hitbox = (vaquero.Xvaquero + 17, vaquero.Yvaquero + 2, 31, 57)
    return


# Entrada:Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida:Inicia a los enemigos del videojuego.
def Carlos_Init():
    global Inscreencarlos
    for x in range(Inscreencarlos):
        Malo[x].Xenemigo = -100
        Malo[x].Yenemigo = -100
        Malo[x].Lifeenemigo = 1
        Malo[x].Velenemigo = 1
        Malo[x].Spawnenemigo = random.randint(0, 11)
        Malo[x].Recenemigo = 0
        Malo[x].dispenemigo = 1
    return


# Entrada:Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida:Inicia las balas en las respectivas posiciones retornandolas.
def Bala_Init():
    for x in range(balascantidad):
        Bala[x].DYbala = 0
        Bala[x].DXbala = 0
        Bala[x].Pinbala = True
        Bala[x].Xbala = -20
        Bala[x].Ybala = -20
        Bala[x]
    return


# Entrada:Sn entrada, contiene solamente una única sentencia que es la salida.
# Salida:Pinta el fondo.
def Pinta_Mapa():
    nPx = 45
    nPy = 45
    for f in range(len(aMapa)):
        for c in range(len(aMapa[f])):
            if aMapa[f][c] == 0:  # Base
                inicia.blit(iniciatiles[3], (nPx, nPy))
                nPx += 45
            if aMapa[f][c] == 1:  # Pared
                inicia.blit(iniciatiles[5], (nPx, nPy))
                nPx += 45
            if aMapa[f][c] == 2:  # Start
                inicia.blit(iniciatiles[2], (nPx, nPy))
                nPx += 45
            if aMapa[f][c] == 3:  # Meta
                inicia.blit(iniciatiles[4], (nPx, nPy))
                nPx += 45
        nPx = 45
        nPy += 45
    inicia.blit(inicia, (0, 0))
    return


# Entrada:Sn entrada, contiene solamente una única sentencia que es la salida.
# Salida:Pinta la bala.
def Pinta_balas():
    for x in range(balascantidad):
        if Bala[x].Pinbala == True:
            inicia.blit(iniciatiles[6], (Bala[x].Xbala, Bala[x].Ybala))
    return


# Entrada:Sn entrada, contiene solamente una única sentencia que es la salida.
# Salida:Pinta el vaquero.
def Pinta_vaquero():
    if vaquero.clase == 1:
        inicia.blit(iniciatiles[0], (vaquero.Xvaquero, vaquero.Yvaquero))


# Entrada:Sn entrada, contiene solamente una única sentencia que es la salida.
# Salida:Pinta al enemigo.
def Pinta_Carlos():
    for x in range(Inscreencarlos):
        if Malo[x].Anienemigo == 0:
            inicia.blit(iniciatiles[1],
                        (Malo[x].Xenemigo, Malo[x].Yenemigo))
        if Malo[x].Anienemigo == 1:
            inicia.blit(iniciatiles[7],
                        (Malo[x].Xenemigo, Malo[x].Yenemigo))
    return


# Entrada:Sn entrada, contiene solamente una única sentencia que es la salida.
# Salida:Se Actualizan todos los datos del enemigo.
def Update_Carlos():
    global Inscreencarlos
    for x in range(Inscreencarlos):
        a = random.randint(0, 2)
        if Malo[x].Lifeenemigo == 0:
            Malo[x].dispenemigo = 1
            Malo[x].Xenemigo = -100
            Malo[x].Lifeenemigo = 1

        if Malo[x].Recenemigo == 0:
            Malo[x].Recenemigo = random.randint(15, 20)

            if Malo[x].Anienemigo == 0:
                Malo[x].Anienemigo = 1
            elif Malo[x].Anienemigo == 1:
                Malo[x].Anienemigo = 0

            if vaquero.Xvaquero <= Malo[x].Xenemigo:
                if vaquero.Yvaquero <= Malo[x].Yenemigo:
                    if a == 0:
                        Malo[x].dirYenemigo = -1
                        Malo[x].dirXenemigo = 0
                    if a == 1:
                        Malo[x].dirYenemigo = -1
                        Malo[x].dirXenemigo = -1
                    if a == 2:
                        Malo[x].dirYenemigo = 0
                        Malo[x].dirXenemigo = -1
            if vaquero.Xvaquero <= Malo[x].Xenemigo:
                if vaquero.Yvaquero >= Malo[x].Yenemigo:
                    if a == 0:
                        Malo[x].dirYenemigo = 1
                        Malo[x].dirXenemigo = 0
                    if a == 1:
                        Malo[x].dirYenemigo = 1
                        Malo[x].dirXenemigo = -1
                    if a == 2:
                        Malo[x].dirYenemigo = 0
                        Malo[x].dirXenemigo = -1
            if vaquero.Xvaquero >= Malo[x].Xenemigo:
                if vaquero.Yvaquero <= Malo[x].Yenemigo:
                    if a == 0:
                        Malo[x].dirYenemigo = -1
                        Malo[x].dirXenemigo = 0
                    if a == 1:
                        Malo[x].dirYenemigo = -1
                        Malo[x].dirXenemigo = 1
                    if a == 2:
                        Malo[x].dirYenemigo = 0
                        Malo[x].dirXenemigo = 1
            if vaquero.Xvaquero >= Malo[x].Xenemigo:
                if vaquero.Yvaquero >= Malo[x].Yenemigo:
                    if a == 0:
                        Malo[x].dirYenemigo = 1
                        Malo[x].dirXenemigo = 0
                    if a == 1:
                        Malo[x].dirYenemigo = 1
                        Malo[x].dirXenemigo = 1
                    if a == 2:
                        Malo[x].dirYenemigo = 0
                        Malo[x].dirXenemigo = 1
        if Malo[x].Xenemigo > -50 and Malo[x].Yenemigo > -50:
            if Malo[x].Xenemigo < 45:
                Malo[x].Xenemigo += 1
            if Malo[x].Xenemigo > 675:
                Malo[x].Xenemigo -= 1
            if Malo[x].Yenemigo < 45:
                Malo[x].Yenemigo += 1
            if Malo[x].Yenemigo > 675:
                Malo[x].Yenemigo -= 1

            Malo[x].Xenemigo += Malo[x].Velenemigo * Malo[x].dirXenemigo
            Malo[x].Yenemigo += Malo[x].Velenemigo * Malo[x].dirYenemigo
            Malo[x].Recenemigo -= 1
    return


# Entrada:Sn entrada, contiene solamente una única sentencia que es la salida.
# Salida:Retorna al for que recorre la bala.
def Update_Bala():
    for x in range(balascantidad):
        if Bala[x].Pinbala == True:
            Bala[x].Xbala += Bala[x].DXbala * 4
            Bala[x].Ybala += Bala[x].DYbala * 4
        if Bala[x].Xbala < 90 or Bala[x].Xbala > 630 or Bala[x].Ybala < 90 or Bala[x].Ybala > 630:
            Bala[x].Pinbala = False
    return


# Entrada:hola
# Salida:mata al enemigo con el rectangulo que se le puso de fondo, utilizando collidepoint
# para que colisione con el rectangulo y desaparesca.
def Matar_carlos(hola):
    global Inscreencarlos
    for x in range(Inscreencarlos):
        for y in range(0, balascantidad):
            if hola[x].collidepoint(Bala[y].Xbala + 3, Bala[y].Ybala + 3):
                Bala[y].Pinbala = False
                Bala[y].Xbala = -20
                Malo[x].Lifeenemigo -= 1
                return


# Entrada:int hola,int alo.
# Salida:te lleva al menu si te toca un enemigo y mueres.
def Morir(hola, alo):
    global Inscreencarlos
    for x in range(0, Inscreencarlos):
        if alo.colliderect(hola[x]):
            Inicio()
            Farmer_Init()
            Carlos_Init()


# Entrada:int c,int d.
# Salida:retorna al for balascantidad,retorna el pinbala.
def Dispara(c, d):
    for x in range(balascantidad):
        if Bala[x].Pinbala == False:
            Bala[x].Xbala = vaquero.Xvaquero + 4
            Bala[x].Ybala = vaquero.Yvaquero + 15
            Bala[x].Pinbala = True
            Bala[x].DXbala = c
            Bala[x].DYbala = d
            return
    return


# Entrada:Sn entrada, contiene solamente una única sentencia que es la salida.
# Salida:Disparo a enemigos.
def Mete_Carlos():
    global Inscreencarlos
    count = 0
    for x in range(0, Inscreencarlos):
        if count != 6:
            if Malo[x].dispenemigo == 1:
                if Malo[x].Spawnenemigo == 0:
                    Malo[x].Xenemigo = 45
                    Malo[x].Yenemigo = 315

                elif Malo[x].Spawnenemigo == 1:
                    Malo[x].Xenemigo = 45
                    Malo[x].Yenemigo = 360

                elif Malo[x].Spawnenemigo == 2:
                    Malo[x].Xenemigo = 45
                    Malo[x].Yenemigo = 405

                elif Malo[x].Spawnenemigo == 3:
                    Malo[x].Xenemigo = 315
                    Malo[x].Yenemigo = 45

                elif Malo[x].Spawnenemigo == 4:
                    Malo[x].Xenemigo = 360
                    Malo[x].Yenemigo = 45

                elif Malo[x].Spawnenemigo == 5:
                    Malo[x].Xenemigo = 405
                    Malo[x].Yenemigo = 45

                elif Malo[x].Spawnenemigo == 6:
                    Malo[x].Xenemigo = 315
                    Malo[x].Yenemigo = 630

                elif Malo[x].Spawnenemigo == 7:
                    Malo[x].Xenemigo = 360
                    Malo[x].Yenemigo = 630

                elif Malo[x].Spawnenemigo == 8:
                    Malo[x].Xenemigo = 405
                    Malo[x].Yenemigo = 630

                elif Malo[x].Spawnenemigo == 9:
                    Malo[x].Xenemigo = 630
                    Malo[x].Yenemigo = 315

                elif Malo[x].Spawnenemigo == 10:
                    Malo[x].Xenemigo = 630
                    Malo[x].Yenemigo = 360

                elif Malo[x].Spawnenemigo == 11:
                    Malo[x].Xenemigo = 630
                    Malo[x].Yenemigo = 405

                Malo[x].Spawnenemigo = random.randint(0, 11)
                Malo[x].dispenemigo = 0
                count += 1
    return


# Entrada:Sn entrada, contiene solamente una única sentencia que es la salida.
# Salida:Pinta un rectangulo debajo de cada enemigo.
def hitbox_vaquero():
    return pygame.draw.rect(inicia, (255, 255, 0),
                            (vaquero.Xvaquero + 11, vaquero.Yvaquero + 3, 20, 28))


# Entrada:Sn entrada, contiene solamente una única sentencia que es la salida.
# Salida:retorna a las lista vacia hola.
def hitbox_carlos():
    global Inscreencarlos
    hola = []
    for x in range(Inscreencarlos):
        hola.append(pygame.draw.rect(inicia, (255, 255, 0),
                                     (Malo[x].Xenemigo + 8, Malo[x].Yenemigo + 4, 10, 30)))
    return hola


# Entrada:Sn entrada, contiene solamente una única sentencia que es la salida.
# Salida:crea el menu y el pausa.
def Inicio():
    p = True
    while p:
        inicia.blit(iniciatiles[8], (0, 0))
        color_marcador = (255, 255, 255)
        fuente_marcador = pygame.font.SysFont("Arial Black", 20)
        moverse = fuente_marcador.render(
            "-Movimientos del personaje: A W S D", 0, color_marcador)
        disparo = fuente_marcador.render(
            "-Teclas disparo: J I K L", 0, color_marcador)
        empezar = fuente_marcador.render(
            "-Oprime solo la tecla 0 para comenzar", 0, color_marcador)
        morir = fuente_marcador.render(
            "-Intenta sobrevivir lo mas posible contra tus enemigo", 0, color_marcador)
        salir = fuente_marcador.render(
            "-Oprime ESC para salir", 0, color_marcador)
        inicia.blit(moverse, (10, 100))
        inicia.blit(disparo, (10, 200))
        inicia.blit(morir, (10, 300))
        inicia.blit(empezar, (10, 630))
        inicia.blit(salir, (400, 650))
        pygame.display.update()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                quit()
            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_d:
                    vaquero.Movimientoder = 0
                if ev.key == pygame.K_a:
                    vaquero.Movimientoizq = 0
                if ev.key == pygame.K_s:
                    vaquero.Movimientoaba = 0
                if ev.key == pygame.K_w:
                    vaquero.Movimientoarr = 0
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_0:
                    p = False
                elif ev.key == pygame.K_ESCAPE:
                    quit()


aMapa = [[1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 2, 0, 0, 0, 3, 0, 0, 0, 2, 3, 0, 1],
         [1, 0, 0, 0, 2, 0, 0, 0, 0, 2, 3, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
         [1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [2, 0, 2, 2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 2],
         [2, 0, 2, 0, 3, 2, 3, 0, 0, 0, 0, 0, 0, 2],
         [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
         [1, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 2, 2, 0, 0, 2, 2, 0, 0, 3, 3, 0, 1],
         [1, 0, 2, 0, 3, 0, 0, 0, 0, 0, 3, 3, 0, 1],
         [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1],
         ]


z = 0
wat = random.randint(100, 150)
balascantidad = 10
Inscreencarlos = 40
vaquero = player()
Malo = [enemigo() for x in range(0, Inscreencarlos)]
Bala = [bullet() for x in range(0, balascantidad)]
Bala_Init()
Farmer_Init()
Carlos_Init()
inicia = PyGame_Init()
iniciatiles = Carga_imagenes()
Fps = pygame.time.Clock()
Inicio()

# While manejo de eventos.
while x:
    eventos = pygame.event.get()
    for ev in eventos:
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                x = False
            if ev.key == pygame.K_d:
                vaquero.Movimientoder += 2
            if ev.key == pygame.K_a:
                vaquero.Movimientoizq += -2
            if ev.key == pygame.K_s:
                vaquero.Movimientoaba += 2
            if ev.key == pygame.K_w:
                vaquero.Movimientoarr += -2
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_d:
                vaquero.Movimientoder = 0
            if ev.key == pygame.K_a:
                vaquero.Movimientoizq = 0
            if ev.key == pygame.K_s:
                vaquero.Movimientoaba = 0
            if ev.key == pygame.K_w:
                vaquero.Movimientoarr = 0
        if ev.type == pygame.QUIT:
            x = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                x = False
            if ev.key == pygame.K_p:
                inicia.fill((0, 0, 0))
                sound_pausa()
                Inicio()

    if vaquero.Xvaquero < 80:
        vaquero.Xvaquero += 2
    if vaquero.Xvaquero > 600:
        vaquero.Xvaquero -= 2
    if vaquero.Yvaquero < 80:
        vaquero.Yvaquero += 2
    if vaquero.Yvaquero > 600:
        vaquero.Yvaquero -= 2

    vaquero.Xvaquero += vaquero.Movimientoizq + vaquero.Movimientoder
    vaquero.Yvaquero += vaquero.Movimientoarr + vaquero.Movimientoaba

    keys = pygame.key.get_pressed()
    if z == 0:
        if keys[pygame.K_j] and keys[pygame.K_k]:
            c = -1
            d = 1
            Dispara(c, d)
            sound_gun()
        elif keys[pygame.K_j] and keys[pygame.K_i]:
            c = -1
            d = -1
            Dispara(c, d)
            sound_gun()
        elif keys[pygame.K_l] and keys[pygame.K_k]:
            c = 1
            d = 1
            Dispara(c, d)
            sound_gun()
        elif keys[pygame.K_l] and keys[pygame.K_i]:
            c = 1
            d = -1
            Dispara(c, d)
            sound_gun()
        elif keys[pygame.K_j]:
            c = -1
            d = 0
            Dispara(c, d)
            sound_gun()
        elif keys[pygame.K_j] and keys[pygame.K_k]:
            c = -1
            d = 1
            Dispara(c, d)
            sound_gun()
        elif keys[pygame.K_l]:
            c = 1
            d = 0
            Dispara(c, d)
            sound_gun()
        elif keys[pygame.K_k]:
            c = 0
            d = 1
            Dispara(c, d)
            sound_gun()
        elif keys[pygame.K_i]:
            c = 0
            d = -1
            Dispara(c, d)
            sound_gun()
        z = 1
    # Llamamos a las funciones.
    if z != 0:
        z += 1
    if z == 40:
        z = 0
    hit_carlos = hitbox_carlos()
    hit_vaquero = hitbox_vaquero()
    inicia.fill((0, 0, 0))
    wat -= 1
    if wat == 0:
        Mete_Carlos()
        wat = random.randint(350, 450)
    Pinta_Mapa()
    Update_Bala()
    Pinta_balas()
    Pinta_vaquero()
    Pinta_Carlos()
    Matar_carlos(hit_carlos)
    Morir(hit_carlos, hit_vaquero)
    Update_Carlos()
    pygame.display.flip()
    Fps.tick(60)
pygame.quit
