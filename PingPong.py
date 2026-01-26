import pygame
pygame.init()

# ====================
# CONFIGURAÇÃO DO JOGO
# ====================

LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong 2 Jogadores")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# ------------------ ELEMENTOS ------------------
# Bola
bola = pygame.Rect(LARGURA//2 - 10, ALTURA//2 - 10, 20, 20)
vel_bola_x = 5
vel_bola_y = 5

# Jogadores
player1 = pygame.Rect(50, ALTURA//2 - 50, 10, 100)
player2 = pygame.Rect(LARGURA - 60, ALTURA//2 - 50, 10, 100)
VEL_PLAYER = 6

# Placar
Fonte = pygame.font.SysFont("Arial", 48)
pontos1 = 0
pontos2 = 0

# ------------------ FUNÇÕES ------------------
def reset_bola():
    global vel_bola_x, vel_bola_y
    bola.center = (LARGURA//2, ALTURA//2)
    vel_bola_x *= -1
    vel_bola_y = 5 if vel_bola_y > 0 else -5

def desenhar():
    tela.fill(PRETO)
    pygame.draw.rect(tela, BRANCO, player1)
    pygame.draw.rect(tela, BRANCO, player2)
    pygame.draw.ellipse(tela, BRANCO, bola)
    pygame.draw.aaline(tela, BRANCO, (LARGURA//2, 0), (LARGURA//2, ALTURA))

    texto = Fonte.render(f"{pontos1}   {pontos2}", True, BRANCO)
    tela.blit(texto, (LARGURA//2 - texto.get_width()//2, 20))

# ------------------ LOOP PRINCIPAL ------------------
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Controles
    teclas = pygame.key.get_pressed()
    # Jogador 1
    if teclas[pygame.K_w] and player1.top > 0:
        player1.y -= VEL_PLAYER
    if teclas[pygame.K_s] and player1.bottom < ALTURA:
        player1.y += VEL_PLAYER
    # Jogador 2
    if teclas[pygame.K_UP] and player2.top > 0:
        player2.y -= VEL_PLAYER
    if teclas[pygame.K_DOWN] and player2.bottom < ALTURA:
        player2.y += VEL_PLAYER

    # Movimento da bola
    bola.x += vel_bola_x
    bola.y += vel_bola_y

    # Colisão com topo e base
    if bola.top <= 0 or bola.bottom >= ALTURA:
        vel_bola_y *= -1

    # Colisão com raquetes
    if bola.colliderect(player1) or bola.colliderect(player2):
        vel_bola_x *= -1

    # Pontuação
    if bola.left <= 0:
        pontos2 += 1
        reset_bola()
    if bola.right >= LARGURA:
        pontos1 += 1
        reset_bola()

    # Desenhar
    desenhar()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
