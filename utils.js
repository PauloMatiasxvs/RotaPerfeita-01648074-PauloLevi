// Funções utilitárias para logs e validações
function logDebug(message) {
    const timestamp = new Date().toLocaleTimeString();
    console.log(`[DEBUG ${timestamp}] ${message}`);
}

// Valida se um elemento DOM existe
function validateElement(element, id) {
    if (!element) {
        logDebug(`❌ Erro: Elemento com ID ${id} não encontrado`);
        return false;
    }
    logDebug(`✅ Elemento com ID ${id} encontrado`);
    return true;
}

// Valida se um array está vazio
function validateArray(array, name) {
    if (!array || array.length === 0) {
        logDebug(`⚠️ Aviso: Array ${name} está vazio`);
        return false;
    }
    logDebug(`✅ Array ${name} contém ${array.length} itens`);
    return true;
}

// Converte coordenadas para string
function coordsToString(coords) {
    return `(${coords[0]}, ${coords[1]})`;
}