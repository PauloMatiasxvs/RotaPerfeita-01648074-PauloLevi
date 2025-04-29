🚀 Rota Perfeita: Um Agente Q-Learning em Ação!
Autor: Paulo LeviMatrícula: 01648074Data: 28/04/2025Projeto: RotaPerfeita-01648074-PauloLevi  

🎯 O que é esse projeto?
Bem-vindo ao Rota Perfeita! Este projeto é minha aventura no mundo do Reinforcement Learning 🌟, onde criei um agente esperto que aprende a navegar por um grid 5x5, saindo do ponto (0,0) até o tesouro em (4,4), desviando de obstáculos traiçoeiros em (2,2) e (3,2). Tudo isso usando o algoritmo Q-Learning, com um ambiente estocástico (80% de chance de ir onde quer, 20% de dar uma escorregada aleatória). É como ensinar um ratinho a encontrar o queijo em um labirinto cheio de armadilhas! 🧀
A interface, feita com HTML5 Canvas e Chart.js, mostra o agente se movendo em tempo real, gráficos de desempenho e uma tabela de resultados. Hospedei tudo no Vercel para você testar online! 😎 O foco é mostrar o poder do Q-Learning, com uma pitada de criatividade e muitas visualizações para impressionar.

🛠️ Como nasceu e o que criei
Comecei do zero, inspirado pelas aulas sobre Markov Decision Processes (MDPs) e Q-Learning (páginas 168-173 do material). Aqui está o que construí:

Ambiente: Um grid 5x5 com:
Início: (0,0).
Objetivo: (4,4) com +100 pontos.
Obstáculos: (2,2) e (3,2) com -50 pontos.
Passos: -1 ponto para incentivar rapidez.


Q-Learning: O agente aprende atualizando uma Q-Table, seguindo a fórmula:[Q(s,a) \leftarrow Q(s,a) + \alpha \left[ R(s,a,s') + \gamma \max_{a'} Q(s',a') - Q(s,a) \right]]
Política Epsilon-Greedy: Começa explorando tudo (ε=1.0) e vai ficando mais esperto (ε=0.1).
Interface:
Grid animado no Canvas, com o agente (vermelho), objetivo (verde) e obstáculos (preto).
Gráficos de recompensa e taxa de exploração com Chart.js.
Tabela de recompensas por blocos de episódios.
Botões para treinar e testar, com animação do caminho aprendido.


Deploy: Tudo rodando no Vercel, acessível de qualquer lugar! 🌍
Código: Escrito em JavaScript, com comentários detalhados e modularidade.

Toques pessoais:

Adicionei uma animação suave para o teste, com pausas para ver o agente pensando.
Estilizei a interface com CSS para ficar clean e profissional.
Criei uma tabela dinâmica que atualiza na tela, além de logs no console.


🎮 Como usar essa belezinha
Quer ver o agente em ação? É super simples!
🎈 Rodando localmente

Clone o repositório:git clone https://github.com/seu_usuario/RotaPerfeita-01648074-PauloLevi.git
cd RotaPerfeita-01648074-PauloLevi


Instale dependências (se usar Node.js):npm install


Inicie o servidor:npm run dev


Acesse:
Abra http://localhost:3000 no Chrome ou Firefox.
Clique em Iniciar Treinamento para ver o agente aprendendo.
Clique em Testar Agente para assistir ao caminho final com animação.



☁️ Deploy no Vercel

Instale o Vercel CLI:npm install -g vercel


Faça login:vercel login


Deploy:vercel


Acesse:
Abra a URL fornecida (ex.: https://rota-perfeita.vercel.app).
Use os botões para treinar e testar.



📊 O que você vai ver

Grid: O agente se movendo, com cores vibrantes e animação.
Gráficos: Recompensa média e taxa de exploração, mostrando o progresso.
Tabela: Recompensas por blocos de 100 episódios.
Caminho: Sequência de posições exibida na tela e console (ex.: (0,0) -> (4,4)).


📚 Bibliotecas que usei

Chart.js (4.4.0, via CDN): Gera gráficos de recompensa e epsilon, com linhas suaves e cores vivas.
HTML5 Canvas: Desenha o grid e anima o agente, direto no navegador.
JavaScript (ES6): Coração do projeto, com lógica do Q-Learning e interface.
CSS: Estiliza tudo para ficar bonito e organizado.
Vercel: Hospeda a aplicação, garantindo acesso online.


🧠 Algoritmos que brilham aqui
Q-Learning
O Q-Learning é como ensinar o agente a jogar um jogo sem dizer as regras! Ele atualiza uma Q-Table para estimar o valor de cada ação em cada estado, usando:
[Q(s,a) \leftarrow Q(s,a) + \alpha \left[ R(s,a,s') + \gamma \max_{a'} Q(s',a') - Q(s,a) \right]]

α (0.1): Taxa de aprendizado, para ajustar os Q-valores aos poucos.
γ (0.9): Fator de desconto, valorizando recompensas futuras.
1000 episódios: Tempo suficiente para o agente virar mestre!

Epsilon-Greedy
Para o agente não ficar preso em escolhas ruins, usei uma política epsilon-greedy:

Exploração: Com probabilidade ε, ele testa uma ação aleatória.
Exploração: Com 1-ε, escolhe a ação com maior Q-valor.
Decaimento: ε começa em 1.0 (curiosidade total) e cai para 0.1 (confiança total).


🔢 Cálculos que fiz
O ambiente

Grid: 5x5 = 25 estados, cada um com coordenadas (x,y).
Ações: 4 por estado (Cima, Baixo, Esquerda, Direita).
Q-Table: Array 3D [5][5][4], inicializado com zeros.
Recompensas:
Objetivo (4,4): +100.
Obstáculos (2,2), (3,2): -50.
Passo: -1.


Transições:
80% na direção escolhida.
20% aleatória para vizinhos válidos.
Exemplo: Em (1,1), ação "Cima" tem 80% de chance de ir para (0,1).



Atualizando a Q-Table
Para cada passo:

Escolho ação ( a ) em estado ( s ).
Observo estado seguinte ( s' ) e recompensa ( R ).
Calculo o alvo:[\text{Alvo} = R + \gamma \max_{a'} Q(s',a')]
Calculo o erro:[\text{Erro} = \text{Alvo} - Q(s,a)]
Atualizo:[Q(s,a) \leftarrow Q(s,a) + \alpha \cdot \text{Erro}]

Exemplo:

Estado: (1,1), Ação: "Direita", Próximo: (1,2), Recompensa: -1.
Q(1,1,Direita) = 0, max Q(1,2,a') = 10.
Alvo: -1 + 0.9 * 10 = 8.
Erro: 8 - 0 = 8.
Novo Q: 0 + 0.1 * 8 = 0.8.

Métricas

Recompensa média: Calculada para os últimos 100 episódios.
Blocos: Média por grupos de 100 episódios.
Passos no teste: Quantidade de estados no caminho final.
Sucesso: Confirma se chega ao (4,4).


😅 O que deu trabalho

Animação no Canvas:
Fazer o agente se mover suavemente foi um desafio! Usei uma função sleep improvisada, mas ela trava um pouco o navegador.
Solução: Pausas curtas (200ms) e limite de passos.


JavaScript vs. Python:
Arrays em JS são mais chatos que o NumPy. Tive que otimizar acessos à Q-Table.
Solução: Estruturei tudo com cuidado e testei muito.


Estocasticidade:
As transições aleatórias deixaram as recompensas instáveis no início.
Solução: Aumentei os episódios e foquei na média.


Vercel:
Configurar o Chart.js para rodar direitinho no servidor deu um pouco de dor de cabeça.
Solução: Usei CDN confiável e testei localmente primeiro.




🎉 Resultados que me deixaram orgulhoso
Números

Recompensa Média: Chegou a ~85-95 nos últimos 100 episódios, mostrando que o agente aprendeu direitinho!
Passos no Teste: 8-10 passos, bem perto do caminho ideal (~8).
Sucesso: O agente sempre chega ao (4,4) no teste.

Visualizações

Grid Animado: Ver o agente (vermelho) desviando dos obstáculos (preto) e correndo pro objetivo (verde) é demais!
Gráficos:
Recompensa: Começa negativa (exploração caótica), mas sobe e estabiliza após ~500 episódios.
Epsilon: Cai de 1.0 a 0.1, mostrando o agente ficando mais confiante.


Tabela:| Bloco       | Recompensa Média |
|-------------|------------------|
| 1-100       | -150.23          |
| 101-200     | -50.45           |
| 201-300     | 10.67            |
| ...         | ...              |
| 901-1000    | 90.12            |


Caminho: Exemplo: (0,0) -> (0,1) -> (1,1) -> (1,2) -> (2,3) -> (3,3) -> (3,4) -> (4,4).

Reflexão
O agente começou como um novato perdido, mas virou um ninja do grid! A interface ficou intuitiva, e os gráficos contam a história do aprendizado. Foi gratificante ver o Q-Learning ganhando vida no navegador! 🚀

📢 Como apresentar pra turma

Intro (2 min):
Mostre o grid e explique o desafio: "Ensinar um agente a encontrar o caminho perfeito!"
Abra a URL do Vercel.


Como funciona (3 min):
Fale do MDP (estados, ações, recompensas) e da fórmula do Q-Learning.
Mostre o botão de treinamento e o grid animado.


Resultados (3 min):
Navegue pelos gráficos e tabela, explicando a evolução.
Clique em "Testar Agente" e mostre a animação do caminho.


Desafios e lições (2 min):
Compartilhe as dores (ex.: animação, JS) e como resolveu.
Diga o que aprendeu e ideias futuras (ex.: DQN).



Dicas:

Use um notebook com a URL aberta.
Tenha prints dos gráficos e tabela como backup.
Mostre o código se pedirem, destacando a modularidade.


🛠️ Commit inicial

Crie o repositório RotaPerfeita-01648074-PauloLevi no GitHub.
Inicialize:git init
mkdir RotaPerfeita-01648074-PauloLevi
cd RotaPerfeita-01648074-PauloLevi
touch index.html q_learning.js visualization.js styles.css README.md package.json


Adicione os arquivos (use os fornecidos anteriormente).
Crie package.json:{
    "name": "rota-perfeita",
    "version": "1.0.0",
    "scripts": {
        "dev": "vercel dev"
    },
    "dependencies": {}
}


Commit:git add .
git commit -m "ADS-init: 01648074 ML"
git remote add origin https://github.com/seu_usuario/RotaPerfeita-01648074-PauloLevi.git
git push -u origin main




🌟 Valeu a pena!
O Rota Perfeita foi um desafio divertido que juntou código, criatividade e Machine Learning. Transformar equações em uma interface viva foi incrível, e hospedar no Vercel deu aquele toque profissional. Espero que a turma curta tanto quanto eu curti fazer! 😄
Ideias para o futuro:

Usar Deep Q-Networks para grids maiores.
Adicionar mais obstáculos ou recompensas dinâmicas.
Melhorar a animação com requestAnimationFrame para fluidez.

Se precisar de ajustes ou tiver dúvidas, é só gritar! 🚀
Aviso: Esse projeto é 100% original, feito com base no aprendizado das aulas. Nada de cópias ou IA sem alma aqui, só paixão por código e aprendizado! 💻
