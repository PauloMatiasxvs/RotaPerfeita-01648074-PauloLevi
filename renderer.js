// Classe que gerencia a renderização da interface
class Renderer {
    constructor(env, qLearning) {
        this.env = env;
        this.qLearning = qLearning;
        this.gridElement = document.getElementById('gameGrid');
        this.rewardTableBody = document.getElementById('rewardTableBody');
        this.episodeElement = document.getElementById('episode');
        this.totalRewardElement = document.getElementById('totalReward');
        this.epsilonElement = document.getElementById('epsilon');
        logDebug('🎨 Renderizador inicializado');
    }

    // Inicializa a grade de divs
    initializeGrid() {
        logDebug('🛠️ Construindo grade 10x10...');
        if (!this.gridElement) {
            logDebug('❌ Erro: Elemento gameGrid não encontrado');
            return;
        }
        this.gridElement.innerHTML = '';
        for (let i = 0; i < this.env.gridSize; i++) {
            for (let j = 0; j < this.env.gridSize; j++) {
                const cell = document.createElement('div');
                cell.className = 'cell';
                cell.dataset.row = i;
                cell.dataset.col = j;
                this.gridElement.appendChild(cell);
            }
        }
        logDebug('✅ Grade inicializada com 100 células');
        this.renderEnvironment();
    }

    // Renderiza o ambiente atual
    renderEnvironment() {
        logDebug('🖌️ Renderizando ambiente...');
        const cells = this.gridElement.querySelectorAll('.cell');
        if (cells.length === 0) {
            logDebug('❌ Erro: Nenhuma célula encontrada na grade');
            return;
        }

        // Limpa classes anteriores
        cells.forEach(cell => {
            cell.className = 'cell';
        });

        // Renderiza recursos
        this.env.resources.forEach(res => {
            const cell = this.gridElement.querySelector(`[data-row="${res[0]}"][data-col="${res[1]}"]`);
            if (cell) {
                cell.classList.add('resource');
                logDebug(`💰 Recurso renderizado em (${res[0]}, ${res[1]})`);
            }
        });

        // Renderiza obstáculos
        this.env.obstacles.forEach(obs => {
            const cell = this.gridElement.querySelector(`[data-row="${obs[0]}"][data-col="${obs[1]}"]`);
            if (cell) {
                cell.classList.add('obstacle');
                logDebug(`🧱 Obstáculo renderizado em (${obs[0]}, ${obs[1]})`);
            }
        });

        // Renderiza robô
        const robotCell = this.gridElement.querySelector(`[data-row="${this.env.robotPos[0]}"][data-col="${this.env.robotPos[1]}"]`);
        if (robotCell) {
            robotCell.classList.add('robot');
            logDebug(`🤖 Robô renderizado em (${this.env.robotPos[0]}, ${this.env.robotPos[1]})`);
        } else {
            logDebug('❌ Erro: Célula do robô não encontrada');
        }
    }

    // Atualiza a tabela de recompensas
    renderRewardTable() {
        logDebug('📊 Atualizando tabela de recompensas...');
        if (this.qLearning.rewards.length === 0) {
            logDebug('⚠️ Nenhuma recompensa para exibir ainda');
            return;
        }

        const lastEpisode = this.qLearning.rewards.length - 1;
        const reward = this.qLearning.rewards[lastEpisode];
        const row = document.createElement('tr');
        row.innerHTML = `<td>${lastEpisode}</td><td>${reward.toFixed(2)}</td>`;
        this.rewardTableBody.appendChild(row);
        logDebug(`✅ Adicionada linha à tabela: Episódio ${lastEpisode}, Recompensa ${reward.toFixed(2)}`);

        // Limita a tabela a 10 linhas visíveis
        const rows = this.rewardTableBody.querySelectorAll('tr');
        if (rows.length > 10) {
            rows[0].remove();
            logDebug('🗑️ Removida linha mais antiga da tabela');
        }
    }

    // Atualiza as métricas na interface
    updateMetrics() {
        logDebug('📈 Atualizando métricas na interface...');
        if (this.episodeElement) {
            this.episodeElement.textContent = this.qLearning.episode;
            logDebug(`📍 Episódio atualizado: ${this.qLearning.episode}`);
        }
        if (this.totalRewardElement) {
            this.totalRewardElement.textContent = this.qLearning.totalReward.toFixed(2);
            logDebug(`💰 Recompensa total atualizada: ${this.qLearning.totalReward.toFixed(2)}`);
        }
        if (this.epsilonElement) {
            this.epsilonElement.textContent = this.qLearning.epsilon.toFixed(2);
            logDebug(`🔍 Epsilon atualizado: ${this.qLearning.epsilon.toFixed(2)}`);
        }
    }

    // Loop de renderização e treinamento
    renderLoop() {
        const trainingStatus = window.getTrainingStatus();
        logDebug(`🔄 renderLoop chamado: Episódio ${this.qLearning.episode}, Training: ${trainingStatus}`);
        if (!this.qLearning.isTrainingComplete() && trainingStatus) {
            logDebug('🏃 Executando episódio de treinamento...');
            this.qLearning.trainEpisode();
            this.renderEnvironment();
            this.renderRewardTable();
            this.updateMetrics();
            setTimeout(() => {
                logDebug('⏳ Agendando próximo renderLoop...');
                this.renderLoop();
            }, 100); // Atraso para visualização
        } else {
            logDebug('🛑 Treinamento pausado ou concluído');
        }
    }
}