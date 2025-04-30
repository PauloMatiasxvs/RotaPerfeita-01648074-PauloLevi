// Classe que implementa o algoritmo Q-Learning
class QLearning {
    constructor(env) {
        this.env = env;
        this.qTable = this.initializeQTable();
        this.alpha = 0.1; // Taxa de aprendizado
        this.gamma = 0.9; // Fator de desconto
        this.epsilon = 1.0; // Taxa de exploração inicial
        this.epsilonMin = 0.1; // Taxa mínima
        this.epsilonDecay = 0.995; // Decaimento
        this.episode = 0; // Contador de episódios
        this.totalReward = 0; // Recompensa acumulada
        this.rewards = []; // Histórico de recompensas
        this.maxEpisodes = 1000; // Limite de episódios
        logDebug('🧠 Q-Learning inicializado com α=0.1, γ=0.9, ε=1.0');
    }

    // Inicializa a Q-Table com zeros
    initializeQTable() {
        logDebug('📊 Inicializando Q-Table...');
        const states = this.env.gridSize * this.env.gridSize;
        const actions = this.env.actions.length;
        const qTable = new Array(states);
        for (let i = 0; i < states; i++) {
            qTable[i] = new Array(actions);
            for (let j = 0; j < actions; j++) {
                qTable[i][j] = 0;
            }
        }
        logDebug(`📋 Q-Table criada: ${states} estados, ${actions} ações`);
        return qTable;
    }

    // Escolhe uma ação usando política ε-greedy
    chooseAction(state) {
        logDebug(`🤔 Escolhendo ação para o estado ${state}`);
        const randomValue = Math.random();
        if (randomValue < this.epsilon) {
            const action = this.env.actions[Math.floor(Math.random() * this.env.actions.length)];
            logDebug(`🌪️ Exploração: Ação aleatória ${this.env.actionToString(action)} (ε=${this.epsilon.toFixed(2)})`);
            return action;
        } else {
            const qValues = this.qTable[state];
            let maxQ = qValues[0];
            let bestAction = 0;
            for (let i = 1; i < qValues.length; i++) {
                if (qValues[i] > maxQ) {
                    maxQ = qValues[i];
                    bestAction = i;
                }
            }
            logDebug(`🎯 Exploração: Melhor ação ${this.env.actionToString(bestAction)} com Q=${maxQ.toFixed(2)}`);
            return bestAction;
        }
    }

    // Atualiza a Q-Table com base na recompensa
    updateQTable(state, action, reward, nextState) {
        logDebug(`🔧 Atualizando Q-Table: Estado ${state}, Ação ${this.env.actionToString(action)}`);
        const currentQ = this.qTable[state][action];
        const nextQValues = this.qTable[nextState];
        let maxNextQ = nextQValues[0];
        for (let i = 1; i < nextQValues.length; i++) {
            if (nextQValues[i] > maxNextQ) {
                maxNextQ = nextQValues[i];
            }
        }
        const newQ = currentQ + this.alpha * (reward + this.gamma * maxNextQ - currentQ);
        this.qTable[state][action] = newQ;
        logDebug(`📈 Novo valor Q: ${newQ.toFixed(2)} (Recompensa: ${reward}, Max Q próximo: ${maxNextQ.toFixed(2)})`);
    }

    // Executa um episódio completo de treinamento
    trainEpisode() {
        logDebug(`🏁 Iniciando episódio ${this.episode}`);
        let state = this.env.reset();
        let episodeReward = 0;
        let terminal = false;
        let stepCount = 0;

        while (!terminal) {
            logDebug(`🔄 Passo ${stepCount} do episódio ${this.episode}`);
            const action = this.chooseAction(state);
            const [nextState, reward, isTerminal] = this.env.step(action);
            this.updateQTable(state, action, reward, nextState);
            state = nextState;
            episodeReward += reward;
            terminal = isTerminal;
            stepCount++;
            if (stepCount > this.env.maxSteps) {
                logDebug('⚠️ Limite de passos atingido, forçando término do episódio');
                terminal = true;
            }
        }

        this.totalReward += episodeReward;
        this.rewards.push(episodeReward);
        this.epsilon = Math.max(this.epsilonMin, this.epsilon * this.epsilonDecay);
        this.episode++;
        logDebug(`✅ Episódio ${this.episode} concluído. Recompensa: ${episodeReward}, Novo ε: ${this.epsilon.toFixed(2)}`);
    }

    // Verifica se o treinamento terminou
    isTrainingComplete() {
        const complete = this.episode >= this.maxEpisodes;
        if (complete) {
            logDebug('🏆 Treinamento concluído: Máximo de episódios atingido');
        }
        return complete;
    }
}