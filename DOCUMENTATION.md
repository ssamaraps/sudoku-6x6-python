# Manual do Sudoku 6x6 – Python

## Visão Geral

Este projeto implementa um Sudoku 6x6 em Python. Ele cria um tabuleiro vazio, preenche automaticamente com uma solução válida, remove alguns números para criar o desafio e permite que o usuário jogue preenchendo os espaços vazios pelo console.

O Sudoku segue as regras tradicionais adaptadas para a grade 6x6:

1. Cada linha deve conter os números de 1 a 6 sem repetição.
2. Cada coluna deve conter os números de 1 a 6 sem repetição.
3. Cada bloco 2x3 (2 linhas x 3 colunas) deve conter os números de 1 a 6 sem repetição.

---

## Estrutura do Código

### 1. Importações

O projeto utiliza apenas a biblioteca `random`:

```python
import random
```

Funções usadas:

* `random.shuffle(lista)` → embaralha os elementos da lista.
* `random.randint(a, b)` → gera número aleatório entre `a` e `b` (inclusive).

---

### 2. Tabuleiro Inicial

```python
matriz = [
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0]]
```

* Cria uma matriz 6x6 zerada, que será o tabuleiro de Sudoku.
* Cada célula com valor `0` representa um espaço vazio.

---

### 3. Função: `validar_jogada`

```python
def validar_jogada(matriz):
```

**O que faz:** Solicita ao usuário linha, coluna e número e valida a jogada antes de inserir.

**Validações realizadas:**

1. Linha e coluna devem ser números inteiros entre 0 e 5.
2. A célula escolhida deve estar vazia.
3. O número deve estar entre 1 e 6.
4. O número não pode repetir na linha, coluna ou bloco 2x3 correspondente.

**Saída:** Atualiza a matriz com a jogada válida e retorna `True`.

---

### 4. Função: `valido`

```python
def valido(matriz, linha, coluna, numero):
```

**O que faz:** Verifica se é permitido colocar um número em uma posição específica, sem violar as regras do Sudoku.

**Checagens:**

* Número não pode repetir na linha.
* Número não pode repetir na coluna.
* Número não pode repetir no bloco 2x3 correspondente.

**Retorno:**

* `True` → jogada válida
* `False` → jogada inválida

---

### 5. Função: `preencher_matriz`

```python
def preencher_matriz(matriz):
```

**O que faz:** Preenche automaticamente toda a matriz com números válidos, criando uma solução completa.

**Como funciona:**

* Percorre cada célula vazia.
* Cria a lista `[1,2,3,4,5,6]` e **embaralha com `shuffle`** para aleatoriedade.
* Tenta colocar cada número usando a função `valido`.
* Usa **recursão e backtracking**: se um caminho não funciona, desfaz a última jogada e tenta outro número.

**Objetivo:** Gerar diferentes soluções válidas de Sudoku a cada execução.

---

### 6. Função: `gerar_espacos`

```python
def gerar_espacos(matriz):
```

**O que faz:** Remove aleatoriamente 10 números da matriz preenchida, criando espaços vazios para o jogador completar.

**Como funciona:**

* Sorteia linha e coluna aleatoriamente.
* Se a célula não estiver vazia, zera o valor.
* Repete até remover 10 números.

---

### 7. Função: `imprimir_sudoku`

```python
def imprimir_sudoku(matriz):
```

**O que faz:** Exibe o Sudoku no console com separadores para visualização dos blocos.

**Detalhes:**

* Linhas separadas por `*` a cada 2 linhas (bloco vertical).
* Colunas separadas por `*` a cada 3 colunas (bloco horizontal).

---

### 8. Função: `verificar_vitoria`

```python
def verificar_vitoria(matriz):
```

**O que faz:** Verifica se o Sudoku foi completamente preenchido.

**Saída:**

* `False` → ainda existem células vazias
* `True` → todas as células preenchidas, imprime mensagem de vitória

---

## 9. Fluxo Principal

```python
preencher_matriz(matriz)
gerar_espacos(matriz)

while True:
    imprimir_sudoku(matriz)
    validar_jogada(matriz)
    if verificar_vitoria(matriz):
        break
```

**Passos:**

1. Preenche automaticamente a matriz (`preencher_matriz`).
2. Remove 10 números aleatoriamente (`gerar_espacos`).
3. Loop de jogo:

   * Exibe o tabuleiro.
   * Solicita jogada do usuário.
   * Verifica vitória.

---

## 10. Dicas de Uso

* Sempre insira números entre 1 e 6.
* Observe os blocos 2x3 para não repetir números.
* O tabuleiro é visualizado no console, acompanhe os separadores `*`.
* Cada execução gera um Sudoku diferente graças ao `shuffle`.
