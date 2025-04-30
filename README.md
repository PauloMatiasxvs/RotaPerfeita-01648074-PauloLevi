🤖 Robô Coletor de Recursos com Q-Learning 🚀
🎯 Introdução ao Projeto
Oi, galera! Esse projeto é uma baita demonstração de Aprendizado por Reforço com Q-Learning! Nele, um robô virtual aprende a coletar moedas 💰 em um grid 10x10, desviando de paredes 🧱. O ambiente é um Processo de Decisão de Markov (MDP), com estados, ações (cima, baixo, esquerda, direita) e recompensas bem definidas. Fiz tudo em JavaScript, HTML e CSS, sem bibliotecas externas, pra rodar direitinho no navegador e ser implantado no Vercel. 🌐
O projeto cumpre todos os requisitos:

Exploração vs. Exploração: Política ε-greedy com decaimento.
Atualização Dinâmica: Q-Table atualizada a cada passo.
Recompensas/Penalidades: +100 por moeda, -10 por parede, e mais.
Visualização: Grade de divs e tabela de recompensas.

🛠️ Tecnologias e Bibliotecas

HTML5: Estrutura com grade de divs e tabela.
CSS3: Estilo vibrante com animações.
JavaScript (puro): Toda a lógica, do Q-Learning à renderização.
Nenhuma biblioteca externa! Tudo feito na raça! 💪

🧠 Algoritmos Aplicados
Q-Learning
O coração do projeto é o Q-Learning, que atualiza a Q-Table com:[ Q(s, a) \leftarrow Q(s, a) + \alpha \cdot (r + \gamma \cdot \max Q(s', a') - Q(s, a)) ]

( \alpha = 0.1 ): Taxa de aprendizado, pra ajustar o quanto o robô "absorve" cada experiência.
( \gamma = 0.9 ): Fator de desconto, pra valorizar recompensas futuras.
( s ): Estado (posição do robô).
( a ): Ação (cima, baixo, esquerda, direita).
( r ): Recompensa.
( s' ): Próximo estado.

Política ε-Greedy
Pra balancear exploração (tentar ações novas) e exploração (usar o que já sabe):

Com probabilidade ( \epsilon ), escolhe uma ação aleatória.
Com probabilidade ( 1 - \epsilon ), escolhe a ação com maior Q.
( \epsilon ) começa em 1.0 (100% aleatório) e decai pra 0.1 (quase sempre a melhor ação).

📝 Cálculos e Fórmulas

Q-Table: Uma matriz gigante de 100 estados (10x10) x 4 ações, toda zerada no início:[ Q(s, a) = 0 \text{ para } s \in {0, ..., 99}, a \in {0, 1, 2, 3} ]
Estado: Calculado como:[ s = \text{linha} \cdot 10 + \text{coluna} ]Exemplo: Posição (5,5) → ( s = 5 \cdot 10 + 5 = 55 ).
Recompensas:
Coletar moeda: +100 💰
Bater em parede: -10 🧱
Cada movimento: -1 🚶
Tentar sair do grid: -5 🚫


Atualização da Q-Table:[ Q(s, a) \leftarrow Q(s, a) + 0.1 \cdot (r + 0.9 \cdot \max Q(s', a') - Q(s, a)) ]
Decaimento de ε:[ \epsilon \leftarrow \max(0.1, \epsilon \cdot 0.995) ]

🚀 Como Executar o Projeto

Clonar o Repositório:
git clone <URL_DO_REPOSITORIO>
cd robo-coletor-qlearning


Rodar Localmente:

Com servidor (recomendado):npm install -g http-server
http-server

Acesse http://localhost:8080 no navegador.
Sem servidor:Abra index.html direto no navegador (pode ter restrições de CORS).


Interagir:

Clique em Iniciar Treinamento ▶️ pra ver o robô aprender.
Clique em Pausar Treinamento ⏸️ pra dar uma pausa.
Clique em Exibir Métricas 📊 pra ver o progresso.
Abra o console (F12) pra logs detalhados.


Implantar no Vercel:

Crie um repositório Git:git init
git add .
git commit -m "Projeto Robô Coletor"
git remote add origin <URL>
git push origin main


No Vercel, importe o repositório, configure como projeto estático, e implante.



📊 Resultados e Comentários

O que rolou:

Após 1000 episódios, o robô vira ninja e coleta moedas rapidinho, desviando das paredes.
As recompensas sobem na tabela HTML, mostrando que o aprendizado tá funcionando.
O ε cai de 1.0 pra 0.1, provando que o robô tá ficando esperto.


Métricas:

Episódio Atual: Até 1000.
Recompensa Total: Soma de todas as recompensas.
Taxa de Exploração (ε): Cai pra 0.1, indicando ações otimizadas.


Visualização:

Grade de Divs: Mostra o robô (azul), moedas (dourado) e paredes (vermelho) com animações.
Tabela HTML: Lista as recompensas por episódio, atualizada ao vivo.
Métricas: Episódio, recompensa total e ε na interface.


Dificuldades:

Balancear Recompensas: Tive que testar várias vezes pra achar valores que fizessem o robô aprender sem desanimar (tipo, -100 era muito pesado).
Atualizar a Grade: Garantir que os divs mudassem direitinho sem travar foi um desafio.
Debugging: Adicionei um monte de logs pra caçar erros, porque às vezes o treinamento não iniciava.


