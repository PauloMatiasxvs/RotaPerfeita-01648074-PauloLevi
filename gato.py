import numpy as np
import matplotlib.pyplot as plt
import pygame
import random
import os
from datetime import datetime

# Configuração do quintal
TAMANHO_QUINTAL = 5
GATO = (0, 0)
RATO = (4, 4)
ARMADILHAS = [(1, 1), (2, 2), (3, 3)]
ACOES = ['cima', 'baixo', 'esquerda', 'direita']
MOVIMENTOS = {
    'cima': (-1, 0), 'baixo': (1, 0),
    'esquerda': (0, -1), 'direita': (0, 1)
}

# Parâmetros do Q-Learning
ALPHA = 0.1  # Taxa de aprendizado
GAMMA = 0.9  # Fator de desconto
EPSILON = 1.0  # Exploração inicial
DECAIMENTO_EPSILON = 0.995
EPSILON_MIN = 0.1
EPISODIOS = 1000
MAX_PASSOS = 100
Q_TABLE_ARQUIVO = "q_table.npy"

# Configuração do Pygame
TAMANHO_CELULA = 100
LARGURA = TAMANHO_QUINTAL * TAMANHO_CELULA
ALTURA = TAMANHO_QUINTAL * TAMANHO_CELULA + 100  # Espaço extra pra texto
CORES = {
    'fundo': (255, 255, 255),
    'grade': (0, 0, 0),
    'gato': (0, 0, 255),
    'rato': (0, 255, 0),
    'armadilha': (255, 0, 0)
}

# Inicializa Pygame
pygame.init()
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Gato Caçador")
FONTE = pygame.font.SysFont('arial', 20)

# Funções do ambiente
def proxima_posicao(estado, acao):
    linha, coluna = estado
    delta_linha, delta_coluna = MOVIMENTOS[acao]
    nova_linha = linha + delta_linha
    nova_coluna = coluna + delta_coluna
    if 0 <= nova_linha < TAMANHO_QUINTAL and 0 <= nova_coluna < TAMANHO_QUINTAL:
        return (nova_linha, nova_coluna)
    return estado

def recompensa(estado):
    if estado == RATO:
        return 10.0
    if estado in ARMADILHAS:
        return -5.0
    return -0.1

def escolher_acao(estado, epsilon):
    if random.random() < epsilon:
        return random.choice(ACOES)
    linha, coluna = estado
    return ACOES[np.argmax(q_table[linha, coluna])]

# Desenha o quintal no Pygame
def desenhar_quintal(gato_pos, episodio, recompensa_atual, passos):
    TELA.fill(CORES['fundo'])
    # Desenha a grade
    for i in range(TAMANHO_QUINTAL):
        for j in range(TAMANHO_QUINTAL):
            pygame.draw.rect(TELA, CORES['grade'],
                            (j * TAMANHO_CELULA, i * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA), 1)
            if (i, j) in ARMADILHAS:
                pygame.draw.rect(TELA, CORES['armadilha'],
                                (j * TAMANHO_CELULA + 10, i * TAMANHO_CELULA + 10, 80, 80))
            if (i, j) == RATO:
                pygame.draw.rect(TELA, CORES['rato'],
                                (j * TAMANHO_CELULA + 10, i * TAMANHO_CELULA + 10, 80, 80))
    # Desenha o gato
    pygame.draw.rect(TELA, CORES['gato'],
                    (gato_pos[1] * TAMANHO_CELULA + 10, gato_pos[0] * TAMANHO_CELULA + 10, 80, 80))
    # Texto informativo
    texto = FONTE.render(f"Episódio: {episodio} | Recompensa: {recompensa_atual:.2f} | Passos: {passos}", True, CORES['grade'])
    TELA.blit(texto, (10, TAMANHO_QUINTAL * TAMANHO_CELULA + 10))
    pygame.display.flip()

# Inicializa Q-Table
if os.path.exists(Q_TABLE_ARQUIVO):
    print("Carregando Q-Table salva...")
    q_table = np.load(Q_TABLE_ARQUIVO)
else:
    q_table = np.zeros((TAMANHO_QUINTAL, TAMANHO_QUINTAL, len(ACOES)))

# Treinamento
recompensas = []
passos_por_episodio = []
epsilons = []
log = open("log_treino.txt", "w", encoding="utf-8")
log.write(f"Treinamento iniciado em {datetime.now()}\n")
epsilon = EPSILON

for episodio in range(EPISODIOS):
    estado = GATO
    total_recompensa = 0
    passos = 0
    caminho = [estado]
    
    # Mostra o treinamento no Pygame (apenas a cada 100 episódios pra não travar)
    if episodio % 100 == 0:
        desenhar_quintal(estado, episodio, total_recompensa, passos)
    
    while passos < MAX_PASSOS:
        acao = escolher_acao(estado, epsilon)
        proximo_estado = proxima_posicao(estado, acao)
        r = recompensa(proximo_estado)
        total_recompensa += r
        caminho.append(proximo_estado)

        # Atualiza Q-Table
        linha, coluna = estado
        prox_linha, prox_coluna = proximo_estado
        idx_acao = ACOES.index(acao)
        q_table[linha, coluna, idx_acao] += ALPHA * (
            r + GAMMA * np.max(q_table[prox_linha, prox_coluna]) - q_table[linha, coluna, idx_acao]
        )

        estado = proximo_estado
        passos += 1
        if episodio % 100 == 0:
            desenhar_quintal(estado, episodio, total_recompensa, passos)
            pygame.time.wait(50)
        if estado == RATO:
            break
    
    recompensas.append(total_recompensa)
    passos_por_episodio.append(passos)
    epsilons.append(epsilon)
    epsilon = max(EPSILON_MIN, epsilon * DECAIMENTO_EPSILON)
    
    # Log de métricas
    log.write(f"Episódio {episodio}: Recompensa={total_recompensa:.2f}, Passos={passos}, Epsilon={epsilon:.3f}\n")
    
    # Processa eventos do Pygame durante o treino
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            log.close()
            exit()

# Salva Q-Table
np.save(Q_TABLE_ARQUIVO, q_table)
log.write(f"Treinamento finalizado em {datetime.now()}\n")
log.close()

# Gráficos com Matplotlib
plt.figure(figsize=(15, 10))
plt.subplot(3, 1, 1)
plt.plot(recompensas, color='#1f77b4')
plt.title('Recompensas por Episódio')
plt.xlabel('Episódio')
plt.ylabel('Recompensa Total')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(passos_por_episodio, color='#ff7f0e')
plt.title('Passos até o Rato por Episódio')
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

# Teste do caminho aprendido com animação interativa
estado = GATO
caminho = [estado]
rodando = True
pausado = False
recompensa_atual = 0
passos = 0
clock = pygame.time.Clock()

while rodando and estado != RATO:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pausado = not pausado
            elif event.key == pygame.K_r:
                estado = GATO
                caminho = [estado]
                recompensa_atual = 0
                passos = 0
    
    if not pausado:
        linha, coluna = estado
        acao = ACOES[np.argmax(q_table[linha, coluna])]
        proximo_estado = proxima_posicao(estado, acao)
        recompensa_atual += recompensa(proximo_estado)
        caminho.append(proximo_estado)
        estado = proximo_estado
        passos += 1
        desenhar_quintal(estado, "Teste", recompensa_atual, passos)
        clock.tick(5)
        pygame.time.wait(200)

print("Caminho Final do Gato:", caminho)
pygame.quit()