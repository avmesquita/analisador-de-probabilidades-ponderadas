# ⚽ Analisador de Probabilidades Ponderadas (Libertadores)

Este é um script Python que gera uma previsão aleatória para um jogo de futebol (final da Libertadores, por exemplo) utilizando um modelo de **probabilidade ponderada**.

Em vez de usar pura aleatoriedade, o algoritmo atribui pesos (pontos) a cada equipe com base no seu desempenho histórico recente, incluindo um bônus/penalidade por confrontos diretos recentes.

## Como Funciona

1.  **Histórico de 50 Jogos:** Os dados de entrada são arrays (listas) de 50 jogos recentes de cada equipe (W: Vitória, D: Empate, L: Derrota).
2.  **Peso Dinâmico:** Uma função calcula os pontos de peso para cada time.
3.  **Confronto Direto (FP):** Adiciona peso extra a quem venceu o rival recentemente.
4.  **Probabilidade:** Calcula a porcentagem de chance de cada resultado (Vitória do Time A, Vitória do Time B, Empate).
5.  **Sorteio:** Realiza um sorteio aleatório usando as probabilidades calculadas.

## ⚙️ Configuração do Ambiente

Para rodar este script, é altamente recomendado criar um **ambiente virtual** na pasta do projeto:

### 1. Criar o Ambiente Virtual

No terminal, dentro da pasta do projeto, execute:

```bash
python -m venv .
```

### 2. Ativar o Ambiente Virtual

```bash Windows (CMD)
.\Scripts\activate.bat
```

```bash Linux/macOS
source bin/activate
```

### 3. Como usar?

1. Edite os Dados: Abra o arquivo Python (analisador_libertadores.py) e atualize os arrays historico_flamengo e historico_palmeiras com os resultados reais mais recentes.

2. Execute o Script: Com o ambiente virtual ativado, rode o arquivo:

```bash
python analisador_libertadores.py
```

### 4. Resultado

O script imprimirá os pesos calculados, as taxas de probabilidade e o palpite aleatório final.

```bash
--- 1. Cálculo dos Pesos (Baseado em 50 jogos) ---
Peso do Flamengo: 34.50
Peso do Palmeiras: 28.00
Peso do Empate:   3.00

--- 2. Cálculo das Probabilidades ---
Prob. Flamengo: 52.67%
Prob. Palmeiras: 42.75%
Prob. Empate:    4.58%
Soma Total: 100.00%

--- 3. Palpite Aleatório Ponderado ---
O resultado sorteado aleatoriamente é: **Flamengo**
```

