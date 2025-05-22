# 🏰 Explorador do Labirinto 2D com Q-Learning

## 📖 Introdução ao Projeto
Bem-vindo ao **Explorador do Labirinto 2D**! Este é um projeto educativo de Machine Learning que utiliza o algoritmo **Q-Learning** para ensinar um robô virtual a navegar em um labirinto 5x5. O objetivo do robô é encontrar um tesouro enquanto evita obstáculos e otimiza seus movimentos. O robô aprende por tentativa e erro, ganhando recompensas ao alcançar o tesouro e penalidades ao encontrar obstáculos ou dar passos desnecessários.

Este projeto é ideal para quem quer entender os conceitos básicos de aprendizado por reforço de forma prática e visual. Ele demonstra como um agente pode aprender a tomar decisões inteligentes em um ambiente simples, aplicando técnicas como exploração vs. exploração e atualização dinâmica de conhecimento.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas
Aqui estão as ferramentas que usamos para construir o projeto:
- **Python 3.x**: Linguagem principal, perfeita para experimentos em ML.
- **Pygame**: Cria a interface gráfica do labirinto, mostrando o robô, tesouro e obstáculos.
- **NumPy**: Gerencia a Q-Table, que armazena o aprendizado do robô.
- **Matplotlib**: Gera gráficos para visualizar o progresso do treinamento.
- **Random**: Permite ações aleatórias durante a exploração inicial.
- **OS e Datetime**: Salva arquivos como logs e a Q-Table.

Essas bibliotecas são amplamente usadas em projetos de ML e são fáceis de instalar.

---

## 🧠 Algoritmos Aplicados
O projeto utiliza dois algoritmos principais para ensinar o robô:
1. **Q-Learning**:
   - Um método de aprendizado por reforço que ajuda o robô a aprender as melhores ações (movimentos) com base em recompensas.
   - Atualiza uma Q-Table dinamicamente, funcionando como uma "memória" do robô sobre o que funciona ou não.
2. **Epsilon-Greedy**:
   - Balanceia **exploração** (tentar ações novas) e **exploração** (usar o que já foi aprendido).
   - No início, o robô explora mais (ações aleatórias); com o tempo, ele confia mais na Q-Table.

Esses algoritmos permitem que o robô reduza incertezas e encontre um caminho eficiente.

---

## 📊 Cálculos e Fórmulas Utilizados
O aprendizado do robô é baseado em cálculos matemáticos simples. Aqui estão as fórmulas principais:
1. **Atualização da Q-Table**:
   \[
   Q(s, a) \leftarrow Q(s, a) + \alpha \cdot \left( r + \gamma \cdot \max Q(s', a') - Q(s, a) \right)
   \]
   - \( s \): Posição atual (ex.: (0,0)).
   - \( a \): Ação (cima, baixo, esquerda, direita).
   - \( s' \): Próxima posição.
   - \( r \): Recompensa (+20 por tesouro, -10 por obstáculos, -0.2 por passo).
   - \( \alpha = 0.1 \): Taxa de aprendizado.
   - \( \gamma = 0.95 \): Fator de desconto (valoriza recompensas futuras).

2. **Ajuste da Taxa de Exploração**:
   \[
   \epsilon \leftarrow \max(0.05, \epsilon \cdot 0.99)
   \]
   - \( \epsilon \): Taxa de exploração, começa em 1.0 (100% de ações aleatórias) e decai até 0.05 (5%), incentivando o robô a usar o aprendizado.

Essas fórmulas guiam o robô para melhorar suas decisões a cada tentativa.

---

## 🚀 Como Executar o Projeto
Siga estes passos para rodar o projeto e ver o robô em ação:

1. **Pré-requisitos**:
   - Instale o Python 3.x: [python.org](https://www.python.org/downloads/).
   - Instale as bibliotecas necessárias:
     ```bash
     pip install pygame numpy matplotlib
Baixe o Código:
Faça o download do arquivo explorador_labirinto_2d.py deste repositório.
Execute o Programa:
Abra o terminal e navegue até a pasta do projeto:
powershell

Copiar
cd caminho/para/RotaPerfeita
Rode o código:
powershell

Copiar
python explorador_labirinto_2d.py
Interaja com o Labirinto:
Durante o treinamento (1500 episódios), o Pygame mostra o robô a cada 100 episódios.
No modo interativo (após o treinamento):
Espaço: Pausa/retoma a animação.
r: Reinicia o robô na posição inicial (0,0).
Feche a janela para encerrar.
Gráficos serão exibidos ao final. Salve-os como graficos_treinamento.png (clique no ícone de disquete no Matplotlib).
Verifique os Resultados:
O caminho final aparece no console, ex.: [(0,0), (1,0), (2,0), (3,0), (4,0), (4,1), (4,2), (4,3), (4,4)].
Veja o arquivo log_treino.txt para métricas e q_table.npy para a Q-Table salva.
É simples e interativo, perfeito para aprender na prática!

📈 Resultados e Comentários Finais
Resultados Obtidos
Após 1500 episódios de treinamento, o robô aprendeu a navegar o labirinto com eficiência:

Caminho Final:
text

Copiar
[(0,0), (1,0), (2,0), (3,0), (4,0), (4,1), (4,2), (4,3), (4,4)]
O robô alcança o tesouro em 9 passos, evitando obstáculos e paredes.
Recompensa: Começa negativa (ex.: -46.40 no episódio 0) e estabiliza entre +18 e +20, refletindo o sucesso (+20 por tesouro, menos -0.2 por passo).
Passos: Reduz de ~140 para ~9, mostrando eficiência.
Exploração (( \epsilon )): Cai de 1.0 para 0.05, indicando que o robô passou a confiar no aprendizado.
Visualização do Labirinto
Episódio 0 (Início do Treinamento):
O robô (círculo azul) está em (0,0), tesouro (dourado) em (4,4), obstáculos (vermelhos) em (1,1), (2,3), (3,2), e paredes (cinza).
Recompensa: -46.40, Passos: 36. Mostra a exploração inicial, com penalidades por obstáculos (-10) e passos (-0.2 cada).
Gráficos de Treinamento
Evolução do Aprendizado:
Recompensas (azul): Sobem de -400 (exploração inicial) para ~0, indicando aprendizado.
Passos (laranja): Caem de 140 para ~9, mostrando eficiência.
Epsilon (verde): Decai de 1.0 para 0.05, reduzindo ações aleatórias.
Comentários Finais
Este projeto demonstra os fundamentos do aprendizado por reforço de forma clara e visual:

Conceitos Aplicados:
Redução de incertezas (exploração vs. exploração com epsilon-greedy).
Atualização dinâmica (Q-Table ajustada a cada ação).
Recompensas e penalidades (+20 por tesouro, -10 por obstáculos, -0.2 por passo).
Visualização do comportamento aprendido (labirinto e gráficos).
Dificuldades:
Ajustar o labirinto de 6x6 para 5x5 devido a erros na Q-Table.
Fallback para círculos, já que sprites não foram fornecidos.
Sugestões de Melhorias:
Adicionar sprites para um visual mais rico.
Incluir sons (ex.: som de vitória ao alcançar o tesouro).
Criar níveis mais complexos ou obstáculos dinâmicos.
O Explorador do Labirinto 2D é uma ótima introdução ao Q-Learning e aprendizado por reforço. Se você está começando em ML, este projeto é um ponto de partida prático e divertido. Explore, modifique e aprenda! 🚀

ℹ️ Sobre a Pasta do Projeto
A pasta RotaPerfeita contém:

explorador_labirinto_2d.py: Código-fonte completo.
README.md: Este arquivo com documentação.
q_table.npy: Q-Table salva.
log_treino.txt: Log do treinamento.
Imagens: labirinto_inicio.png e graficos_treinamento.png.
Se tiver dúvidas ou sugestões, sinta-se à vontade para contribuir no repositório!