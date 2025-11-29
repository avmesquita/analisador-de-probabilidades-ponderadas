import random

# --- VARIÁVEIS DE CONFIGURAÇÃO ---
PESO_BASE_VITORIA = 1.5       # Peso base que uma vitória adiciona
PESO_CONFRONTO_DIRETO = 2.0   # Peso extra para o resultado de um jogo entre os dois rivais
PESO_EMPATE_FIXO = 3.0        # Peso fixo dado ao Empate em uma final (reflete alta chance de tensão)
RESULTADOS_POSSIVEIS = ["Flamengo", "Palmeiras", "Empate"]

# --- DADOS DE ENTRADA (50 JOGOS HISTÓRICOS HIPOTÉTICOS) ---
# W = Vitória, D = Empate, L = Derrota, FP = Confronto Direto
historico_flamengo = [
    "W", "W", "D", "W", "L", "W", "W", "W", "D", "W", 
    "W", "L", "W", "D", "W", "W", "W", "D", "L", "W", 
    "W", "W", "D", "W", "L", "W", "W", "W", "D", "W", 
    "L", "W", "W", "D", "W", "W", "L", "W", "D", "W",
    "W", "W", "D", "W", "L", "W", "W", "W", "FP(W)", "W" # Flamengo venceu o confronto direto
]

historico_palmeiras = [
    "W", "D", "L", "W", "W", "D", "W", "L", "D", "W", 
    "W", "D", "L", "W", "W", "D", "W", "L", "D", "W", 
    "D", "W", "L", "W", "W", "D", "W", "L", "D", "W", 
    "W", "W", "D", "L", "W", "D", "W", "W", "D", "L",
    "W", "W", "D", "L", "W", "D", "W", "FP(L)", "D", "W" # Palmeiras perdeu o confronto direto
]


def calcular_pesos(h_time_a, h_time_b, nome_a="Flamengo", nome_b="Palmeiras"):
    """
    Processa os arrays de histórico e atribui pontos de peso para as equipes.
    Retorna os pesos [peso_a, peso_b, peso_empate].
    """
    pontos_a = 0
    pontos_b = 0
    
    # Processa o histórico do Time A (ajustando o ponto B no Confronto Direto)
    for resultado in h_time_a:
        if resultado == "W":
            pontos_a += PESO_BASE_VITORIA
        elif resultado == "L":
            pontos_a -= (PESO_BASE_VITORIA * 0.5) 
        elif resultado == "D":
            pontos_a += (PESO_BASE_VITORIA * 0.5) 
        
        # Ajuste por CONFRONTO DIRETO
        if resultado.startswith("FP"):
            if resultado == "FP(W)":
                pontos_a += PESO_CONFRONTO_DIRETO
                pontos_b -= PESO_CONFRONTO_DIRETO
            elif resultado == "FP(L)":
                pontos_a -= PESO_CONFRONTO_DIRETO
                pontos_b += PESO_CONFRONTO_DIRETO
                
    # Processa o histórico do Time B
    for resultado in h_time_b:
        if resultado == "W":
            pontos_b += PESO_BASE_VITORIA
        elif resultado == "L":
            pontos_b -= (PESO_BASE_VITORIA * 0.5)
        elif resultado == "D":
            pontos_b += (PESO_BASE_VITORIA * 0.5)

    # Garante que os pesos mínimos sejam 1.0, mesmo com muitas derrotas
    peso_a_final = max(1.0, pontos_a)
    peso_b_final = max(1.0, pontos_b)
    
    return [peso_a_final, peso_b_final, PESO_EMPATE_FIXO]


def calcular_probabilidades(pesos):
    """
    Calcula o percentual de probabilidade de cada resultado com base nos pesos.
    """
    peso_total = sum(pesos)
    prob_flamengo = (pesos[0] / peso_total) * 100
    prob_palmeiras = (pesos[1] / peso_total) * 100
    prob_empate = (pesos[2] / peso_total) * 100
    
    return [prob_flamengo, prob_palmeiras, prob_empate]


def analisar_e_sortear():
    """
    Função principal que executa o cálculo, a análise e o sorteio.
    """
    print("--- 1. Cálculo dos Pesos (Baseado em 50 jogos) ---")
    pesos_finais = calcular_pesos(historico_flamengo, historico_palmeiras)
    
    print(f"Peso do Flamengo: {pesos_finais[0]:.2f}")
    print(f"Peso do Palmeiras: {pesos_finais[1]:.2f}")
    print(f"Peso do Empate:   {pesos_finais[2]:.2f}")
    
    print("\n--- 2. Cálculo das Probabilidades ---")
    probabilidades = calcular_probabilidades(pesos_finais)
    
    print(f"Prob. Flamengo: {probabilidades[0]:.2f}%")
    print(f"Prob. Palmeiras: {probabilidades[1]:.2f}%")
    print(f"Prob. Empate:    {probabilidades[2]:.2f}%")
    
    print(f"Soma Total: {(probabilidades[0] + probabilidades[1] + probabilidades[2]):.2f}%")
    
    # Sorteio
    palpite_final = random.choices(RESULTADOS_POSSIVEIS, weights=pesos_finais, k=1)[0]
    
    print("\n--- 3. Palpite Aleatório Ponderado ---")
    print(f"O resultado sorteado aleatoriamente é: **{palpite_final}**")


if __name__ == "__main__":
    analisar_e_sortear()