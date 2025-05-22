# Explorador do Labirinto 2D com Q-Learning

## Introdução ao Projeto
Bem-vindo ao **Explorador do Labirinto 2D**! Este é um projeto simples de Machine Learning que usa o algoritmo **Q-Learning**, um tipo de aprendizado por reforço, para ensinar um robô virtual a navegar por um labirinto 5x5. O objetivo do robô é encontrar um tesouro enquanto evita obstáculos e minimiza o número de movimentos. Imagine um jogo onde o robô aprende com tentativa e erro, ganhando pontos por encontrar o tesouro e perdendo pontos por bater em obstáculos ou dar passos desnecessários. Este projeto é uma introdução prática aos conceitos de inteligência artificial, mostrando como um agente pode aprender a tomar decisões inteligentes em um ambiente desconhecido.

## Tecnologias e Bibliotecas Utilizadas
Para criar este projeto, utilizamos as seguintes ferramentas e bibliotecas:
- **Python 3.x**: A linguagem de programação principal, fácil de usar e poderosa para ML.
- **Pygame**: Uma biblioteca para criar a interface gráfica do labirinto, mostrando o robô, o tesouro e os obstáculos em tempo real.
- **NumPy**: Usada para manipular a Q-Table, uma tabela que armazena o conhecimento do robô sobre o labirinto.
- **Matplotlib**: Responsável por gerar gráficos que mostram como o aprendizado evolui ao longo do tempo.
- **Random**: Ajuda o robô a explorar o labirinto de forma aleatória no início.
- **OS e Datetime**: Utilizadas para salvar arquivos e registrar o progresso do treinamento.

Essas bibliotecas são populares na comunidade de ML e tornam o projeto acessível para quem quer experimentar.

## Algoritmos Aplicados
Este projeto utiliza dois algoritmos principais:
1. **Q-Learning**: Um método de aprendizado por reforço onde o robô aprende a escolher as melhores ações (movimentos) com base em recompensas e penalidades. Ele atualiza uma Q-Table dinamicamente, que funciona como uma "memória" do que deu certo ou errado em cada posição do labirinto.
2. **Epsilon-Greedy**: Uma estratégia para balancear **exploração** (tentar movimentos novos) e **exploração** (usar o que já foi aprendido). No início, o robô explora mais; com o tempo, ele confia mais na Q-Table.

Esses algoritmos juntos ajudam o robô a reduzir incertezas e encontrar o caminho mais eficiente.

## Cálculos e Fórmulas Utilizados
O aprendizado do robô é baseado em algumas fórmulas matemáticas simples, mas poderosas. Aqui estão os principais cálculos:
1. **Atualização da Q-Table**:
   \[
   Q(s, a) \leftarrow Q(s, a) + \alpha \cdot \left( r + \gamma \cdot \max Q(s', a') - Q(s, a) \right)
   \]
   - \( s \): Posição atual do robô (ex.: (0,0)).
   - \( a \): Ação (cima, baixo, esquerda, direita).
   - \( s' \): Próxima posição.
   - \( r \): Recompensa (ex.: +20 por encontrar o tesouro, -10 por obstáculos, -0.2 por cada passo).
   - \( \alpha = 0.1 \): Taxa de aprendizado, controla quanto o robô ajusta sua memória.
   - \( \gamma = 0.95 \): Fator de desconto, dá mais peso a recompensas futuras.

2. **Ajuste da Taxa de Exploração**:
   \[
   \epsilon \leftarrow \max(0.05, \epsilon \cdot 0.99)
   \]
   - \( \epsilon \): Começa em 1.0 (100% de exploração) e decai até 0.05 (5% de exploração), incentivando o robô a usar o que aprendeu com o tempo.

Essas fórmulas são o coração do aprendizado, permitindo que o robô melhore a cada tentativa.

## Como Executar o Projeto
Quer experimentar o projeto? Siga esses passos simples:
1. **Pré-requisitos**:
   - Baixe e instale o Python 3.x em [python.org](https://www.python.org/downloads/).
   - Instale as bibliotecas necessárias com o comando:
     ```bash
     pip install pygame numpy matplotlib
Obtenha o Código:
Baixe o arquivo explorador_labirinto_2d.py deste repositório.
Execute o Código:
Abra o terminal (ex.: PowerShell no Windows) e navegue até a pasta do projeto:
powershell

Copiar
cd C:\caminho\para\RotaPerfeita
Rode o programa:
powershell

Copiar
python explorador_labirinto_2d.py
Interaja com o Labirinto:
Durante o treinamento, o Pygame mostrará o robô se movendo a cada 100 episódios.
No teste interativo:
Pressione Espaço para pausar ou retomar.
Pressione r para reiniciar o robô.
Feche a janela para encerrar.
Após o treinamento, gráficos serão exibidos. Salve-os como graficos_treinamento.png se desejar.
Explore os Resultados:
Veja o caminho final no console (ex.: [(0,0), (1,0), (2,0), (3,0), (4,0), (4,1), (4,2), (4,3), (4,4)]).
Confira o arquivo log_treino.txt para detalhes e a Q-Table em q_table.npy.
É fácil de rodar e ótimo para aprender na prática!

Resultados e Comentários Finais
Resultados Obtidos
O robô aprendeu a navegar o labirinto 5x5 com sucesso! Após 1500 episódios de treinamento:

Caminho Otimizado: O robô alcança o tesouro em cerca de 9 passos, seguindo um caminho como [(0,0), (1,0), (2,0), (3,0), (4,0), (4,1), (4,2), (4,3), (4,4)].
Recompensas: A recompensa inicial era negativa (ex.: -46.40 no episódio 0), mas estabilizou perto de +18 a +20, refletindo o sucesso ao encontrar o tesouro (+20) menos o custo dos passos (-0.2 por movimento).
Passos: Reduziu de quase 150 (limite máximo) para cerca de 9, mostrando eficiência.
Exploração: A taxa de exploração (( \epsilon )) caiu de 1.0 para 0.05, indicando que o robô passou a confiar no aprendizado.
Apresentação Visual Obrigatória
Confira as visualizações abaixo para entender o progresso:

Labirinto no Início:
Mostra o robô (círculo azul) em (0,0), com tesouro (dourado) em (4,4), obstáculos (vermelhos) em (1,1), (2,3), (3,2), e paredes (cinza). A recompensa de -46.40 e 36 passos indicam exploração inicial com penalidades.
Gráficos de Treinamento:
Três gráficos: Recompensas (azul) sobem de -400 para ~0, Passos (laranja) caem de 140 para ~9, e ( \epsilon ) (verde) decai de 1.0 para 0.05, mostrando o aprendizado ao longo de 1500 episódios.
Comentários Finais
Este projeto é uma introdução prática ao aprendizado por reforço. O robô aprende a reduzir incertezas (exploração vs. exploração), atualiza sua Q-Table dinamicamente, ajusta a taxa de exploração e responde a recompensas e penalidades. As dificuldades, como ajustar o tamanho do labirinto (de 6x6 para 5x5) e lidar com a falta de sprites, foram superadas com soluções como verificação de Q-Table e fallback para círculos. Para quem está começando em ML, é um exemplo claro e visual de como os algoritmos funcionam. Sugerimos melhorias futuras, como adicionar sprites, sons ou níveis mais complexos, para torná-lo ainda mais interativo!

Obrigado por explorar o projeto! Se tiver dúvidas, sinta-se à vontade para perguntar ou contribuir no repositório.