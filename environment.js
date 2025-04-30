// Classe que define o ambiente do robô coletor
class Environment {
    constructor() {
        // Configurações do grid
        this.gridSize = 10;
        this.robotPos = [0, 0];
        this.resources = [[9, 9], [5, 5]];
        this.obstacles = [[3, 3], [4, 4]];
        this.actions = [0, 1, 2, 3]; // 0: cima, 1: baixo, 2: esquerda, 3: direita
        this.maxSteps = 50;
        this.currentStep = 0;
        logDebug('🌍 Ambiente inicializado com grid 10x10, robô em (0,0)');
    }

    // Reinicia o ambiente para um novo episódio
    reset() {
        logDebug('🔄 Reiniciando ambiente para novo episódio');
        this.robotPos = [0, 0];
        this.currentStep = 0;
        const state = this.getState();
        logDebug(`🗺️ Estado inicial: ${state}`);
        return state;
    }

    // Calcula o estado atual com base na posição do robô
    getState() {
        const state = this.robotPos[0] * this.gridSize + this.robotPos[1];
        logDebug(`📍 Calculando estado: (${this.robotPos[0]}, ${this.robotPos[1]}) -> ${state}`);
        return state;
    }

    // Verifica se o estado é terminal
    isTerminal() {
        const pos = this.robotPos;
        const collected = this.resources.some(res => res[0] === pos[0] && res[1] === pos[1]);
        const maxStepsReached = this.currentStep >= this.maxSteps;
        const isTerminal = collected || maxStepsReached;
        logDebug(`🔚 Verificando estado terminal: Coletou recurso? ${collected}, Passos máximos atingidos? ${maxStepsReached}, Terminal: ${isTerminal}`);
        return isTerminal;
    }

    // Executa uma ação e retorna [novo_estado, recompensa, terminal]
    step(action) {
        logDebug(`🚶 Executando ação: ${this.actionToString(action)}`);
        let reward = -1; // Penalidade por movimento
        let newPos = [...this.robotPos];
        this.currentStep++;

        // Aplica a ação
        if (action === 0) {
            newPos[0]--;
            logDebug('⬆️ Movendo para cima');
        } else if (action === 1) {
            newPos[0]++;
            logDebug('⬇️ Movendo para baixo');
        } else if (action === 2) {
            newPos[1]--;
            logDebug('⬅️ Movendo para esquerda');
        } else if (action === 3) {
            newPos[1]++;
            logDebug('➡️ Movendo para direita');
        }

        // Verifica limites do grid
        if (newPos[0] < 0 || newPos[0] >= this.gridSize || newPos[1] < 0 || newPos[1] >= this.gridSize) {
            reward = -5;
            newPos = [...this.robotPos];
            logDebug('🚫 Tentativa de sair do grid, penalidade: -5');
        } else {
            // Verifica obstáculos
            const hitObstacle = this.obstacles.some(obs => obs[0] === newPos[0] && obs[1] === newPos[1]);
            if (hitObstacle) {
                reward = -10;
                newPos = [...this.robotPos];
                logDebug('🧱 Bateu em obstáculo, penalidade: -10');
            } else {
                // Verifica recursos
                const collected = this.resources.some(res => res[0] === newPos[0] && res[1] === newPos[1]);
                if (collected) {
                    reward = 100;
                    logDebug('💰 Recurso coletado, recompensa: +100');
                }
                this.robotPos = newPos;
                logDebug(`📍 Nova posição do robô: (${newPos[0]}, ${newPos[1]})`);
            }
        }

        const state = this.getState();
        const terminal = this.isTerminal();
        logDebug(`🎯 Resultado da ação: Novo estado: ${state}, Recompensa: ${reward}, Terminal: ${terminal}`);
        return [state, reward, terminal];
    }

    // Converte ação numérica para string
    actionToString(action) {
        const actionNames = ['cima', 'baixo', 'esquerda', 'direita'];
        return actionNames[action] || 'desconhecida';
    }
}