import numpy as np
import pygame
import matplotlib.pyplot as plt
import random
import os
from datetime import datetime

# Configuração do Pygame
LARGURA, ALTURA = 500, 500  # Ajustado para 5x5
TAMANHO_CELULA = 100
pygame.init()
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Explorador do Labirinto 2D")
FONTE = pygame.font.SysFont('arial', 20)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (150, 150, 150)

# Carrega sprites (imagens PNG)
try:
    ROBO = pygame.transform.scale(pygame.image.load("robo.png"), (80, 80))
    TESOURO = pygame.transform.scale(pygame.image.load("tesouro.png"), (80, 80))
    FOGO = pygame.transform.scale(pygame.image.load("fogo.png"), (80, 80))
except FileNotFoundError:
    print("Erro: Arquivos de imagem (robo.png, tesouro.png, fogo.png) não encontrados. Usando círculos como fallback.")
    ROBO = TESOURO = FOGO = None

# Configuração do labirinto
TAMANHO_LABIRINTO = 5  # Ajustado para 5x5
ROBO_POS = (0, 0)
TESOURO_POS = (4, 4)  # Ajustado para caber no grid 5x5
OBSTACULOS = [(1, 1), (2, 3), (3, 2)]  # Ajustado para caber no grid 5x5
PAREDES = [(0, 2), (1, 2), (2, 1), (3, 3)]  # Ajustado para caber no grid 5x5
ACOES = ['cima', 'baixo', 'esquerda', 'direita']
MOVIMENTOS = {
    'cima': (-1, 0), 'baixo': (1, 0),
    'esquerda': (0, -1), 'direita': (0, 1)
}

# Parâmetros do Q-Learning
ALPHA = 0.1
GAMMA = 0.95
EPSILON = 1.0
DECAIMENTO_EPSILON = 0.99
EPSILON_MIN = 0.05
EPISODIOS = 1500
MAX_PASSOS = 150
Q_TABLE_ARQUIVO = "q_table.npy"

# Funções do ambiente
def proxima_posicao(estado, acao):
    linha, coluna = estado
    delta_linha, delta_coluna = MOVIMENTOS[acao]
    nova_linha = linha + delta_linha
    nova_coluna = coluna + delta_coluna
    nova_pos = (nova_linha, nova_coluna)
    if (0 <= nova_linha < TAMANHO_LABIRINTO and 0 <= nova_coluna < TAMANHO_LABIRINTO
        and nova_pos not in PAREDES):
        return nova_pos
    return estado

def recompensa(estado):
    if estado == TESOURO_POS:
        return 20.0
    if estado in OBSTACULOS:
        return -10.0
    return -0.2

def escolher_acao(estado, epsilon):
    if random.random() < epsilon:
        return random.choice(ACOES)
    linha, coluna = estado
    return ACOES[np.argmax(q_table[linha, coluna])]

# Funções de renderização
def desenhar_labirinto(robo_pos, episodio, recompensa_atual, passos):
    TELA.fill(BRANCO)
    # Desenha grid e paredes
    for i in range(TAMANHO_LABIRINTO):
        for j in range(TAMANHO_LABIRINTO):
            pos = (i, j)
            rect = (j * TAMANHO_CELULA, i * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
            pygame.draw.rect(TELA, PRETO, rect, 1)
            if pos in PAREDES:
                pygame.draw.rect(TELA, CINZA, (rect[0] + 5, rect[1] + 5, rect[2] - 10, rect[3] - 10))
    # Desenha obstáculos
    for (linha, coluna) in OBSTACULOS:
        pos_x, pos_y = coluna * TAMANHO_CELULA + TAMANHO_CELULA // 2, linha * TAMANHO_CELULA + TAMANHO_CELULA // 2
        if FOGO:
            TELA.blit(FOGO, (pos_x - 40, pos_y - 40))
        else:
            pygame.draw.circle(TELA, (255, 0, 0), (pos_x, pos_y), 30)
    # Desenha tesouro
    pos_x, pos_y = TESOURO_POS[1] * TAMANHO_CELULA + TAMANHO_CELULA // 2, TESOURO_POS[0] * TAMANHO_CELULA + TAMANHO_CELULA // 2
    if TESOURO:
        TELA.blit(TESOURO, (pos_x - 40, pos_y - 40))
    else:
        pygame.draw.circle(TELA, (255, 215, 0), (pos_x, pos_y), 30)
    # Desenha robô
    pos_x, pos_y = robo_pos[1] * TAMANHO_CELULA + TAMANHO_CELULA // 2, robo_pos[0] * TAMANHO_CELULA + TAMANHO_CELULA // 2
    if ROBO:
        TELA.blit(ROBO, (pos_x - 40, pos_y - 40))
    else:
        pygame.draw.circle(TELA, (0, 0, 255), (pos_x, pos_y), 30)
    # Desenha texto
    texto = FONTE.render(f"Episódio: {episodio} | Recompensa: {recompensa_atual:.2f} | Passos: {passos}", True, PRETO)
    TELA.blit(texto, (10, ALTURA - 30))
    pygame.display.flip()

# Inicializa Q-Table com verificação de tamanho
expected_shape = (TAMANHO_LABIRINTO, TAMANHO_LABIRINTO, len(ACOES))
if os.path.exists(Q_TABLE_ARQUIVO):
    print("Carregando Q-Table salva...")
    q_table = np.load(Q_TABLE_ARQUIVO)
    if q_table.shape != expected_shape:
        print(f"Q-Table salva tem formato {q_table.shape}, mas o esperado é {expected_shape}. Recriando Q-Table...")
        q_table = np.zeros(expected_shape)
else:
    q_table = np.zeros(expected_shape)

# Treinamento
recompensas = []
passos_por_episodio = []
epsilons = []
log = open("log_treino.txt", "w", encoding="utf-8")
log.write(f"Treinamento iniciado em {datetime.now()}\n")
epsilon = EPSILON

for episodio in range(EPISODIOS):
    estado = ROBO_POS
    total_recompensa = 0
    passos = 0
    caminho = [estado]
    
    if episodio % 100 == 0:
        desenhar_labirinto(estado, episodio, total_recompensa, passos)
    
    while passos < MAX_PASSOS:
        acao = escolher_acao(estado, epsilon)
        proximo_estado = proxima_posicao(estado, acao)
        r = recompensa(proximo_estado)
        total_recompensa += r
        caminho.append(proximo_estado)

        linha, coluna = estado
        prox_linha, prox_coluna = proximo_estado
        idx_acao = ACOES.index(acao)
        q_table[linha, coluna, idx_acao] += ALPHA * (
            r + GAMMA * np.max(q_table[prox_linha, prox_coluna]) - q_table[linha, coluna, idx_acao]
        )

        estado = proximo_estado
        passos += 1
        if episodio % 100 == 0:
            desenhar_labirinto(estado, episodio, total_recompensa, passos)
            pygame.time.wait(50)
        if estado == TESOURO_POS:
            break
    
    recompensas.append(total_recompensa)
    passos_por_episodio.append(passos)
    epsilons.append(epsilon)
    epsilon = max(EPSILON_MIN, epsilon * DECAIMENTO_EPSILON)
    log.write(f"Episódio {episodio}: Recompensa={total_recompensa:.2f}, Passos={passos}, Epsilon={epsilon:.3f}\n")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            log.close()
            exit()

np.save(Q_TABLE_ARQUIVO, q_table)
log.write(f"Treinamento finalizado em {datetime.now()}\n")
log.close()

# Gráficos
plt.figure(figsize=(15, 10))
plt.subplot(3, 1, 1)
plt.plot(recompensas, color='#1f77b4')
plt.title('Recompensas por Episódio')
plt.xlabel('Episódio')
plt.ylabel('Recompensa Total')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(passos_por_episodio, color='#ff7f0e')
plt.title('Passos até o Tesouro por Episódio')
plt.xlabel('Episódio')
plt.ylabel('Passos')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(epsilons, color='#2ca02c')
plt.title('Taxa de Exploração (Epsilon) por Episódio')
plt.xlabel('Episódio')
plt.ylabel('Epsilon')
plt.grid(True)

plt.tight_layout()
plt.show()

# Teste interativo
estado = ROBO_POS
caminho = [estado]
rodando = True
pausado = False
recompensa_atual = 0
passos = 0
clock = pygame.time.Clock()

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pausado = not pausado
            elif event.key == pygame.K_r:
                estado = ROBO_POS
                caminho = [estado]
                recompensa_atual = 0
                passos = 0
    
    if not pausado and estado != TESOURO_POS:
        linha, coluna = estado
        acao = ACOES[np.argmax(q_table[linha, coluna])]
        proximo_estado = proxima_posicao(estado, acao)
        recompensa_atual += recompensa(proximo_estado)
        caminho.append(proximo_estado)
        estado = proximo_estado
        passos += 1
    
    desenhar_labirinto(estado, "Teste", recompensa_atual, passos)
    clock.tick(5)
    pygame.time.wait(150)

print("Caminho Final do Robô:", caminho)
pygame.quit()