import pygame

window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption("Futebol I")
win = pygame.image.load("parabens.png")
campo = pygame.image.load("campo.png")
jogador_um = pygame.image.load("jogador_1.png")
placar_1 = 0
placar_1_img = pygame.image.load('0.png')
placar_2 = 0
placar_2_img = pygame.image.load('0.png')
jogador_um_y = 310
jogador_um_movUp = False
jogador_um_movDown = False
jogador_dois = pygame.image.load("jogador_2.png")
jogador_dois_y = 310
bola = pygame.image.load("bola.png")
bola_x = 617
bola_y = 337
bola_dir = -3
bola_dir_y = 1


def bola_jogo():
    global bola_x
    global bola_y
    global bola_dir
    global bola_dir_y
    global placar_1
    global placar_2
    global placar_1_img
    global placar_2_img
    bola_x += bola_dir
    bola_y += bola_dir_y

    if bola_x < 120:
        if jogador_um_y < bola_y + 23:
            if jogador_um_y + 146 > bola_y:
                bola_dir *= -1
    if bola_x > 1100:
        if jogador_dois_y < bola_y + 23:
            if jogador_dois_y + 146 > bola_y:
                bola_dir *= -1
    if bola_y > 685:
        bola_dir_y *= -1
    elif bola_y <= 0:
        bola_dir_y *= -1
    if bola_x < -50:
        bola_x = 617
        bola_y = 337
        bola_dir_y *= -1
        bola_dir *= -1
        placar_2 += 1
        placar_2_img = pygame.image.load(f"{placar_2}.png")
    elif bola_x > 1320:
        bola_x = 617
        bola_y = 337
        bola_dir_y *= -1
        bola_dir *= -1
        placar_1 += 1
        placar_1_img = pygame.image.load(f"{placar_1}.png")


def acao_jogador():
    global jogador_um_y

    if jogador_um_movUp:
        jogador_um_y -= 5
    else:
        jogador_um_y += 0
    if jogador_um_movDown:
        jogador_um_y += 5
    else:
        jogador_um_y += 0
    if jogador_um_y <= 0:
        jogador_um_y = 0
    elif jogador_um_y >= 575:
        jogador_um_y = 575


def acao_jogador2():
    global jogador_dois_y
    jogador_dois_y = bola_y


def imagem():
    if placar_1 or placar_2 < 2:
        window.blit(campo, (0, 0))
        window.blit(jogador_um, (50, jogador_um_y))
        window.blit(jogador_dois, (1150, jogador_dois_y))
        window.blit(bola, (bola_x, bola_y))
        window.blit(placar_1_img, (500, 50))
        window.blit(placar_2_img, (710, 50))
        bola_jogo()
        acao_jogador()
        acao_jogador2()
    else:
        window.blit(win, (300, 330))

if __name__ == '__main__':
    loop = True
    while loop:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                loop = False
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_w:
                    jogador_um_movUp = True
                if events.key == pygame.K_s:
                    jogador_um_movDown = True
            if events.type == pygame.KEYUP:
                if events.key == pygame.K_w:
                    jogador_um_movUp = False
                if events.key == pygame.K_s:
                    jogador_um_movDown = False

        imagem()
        pygame.display.update()


