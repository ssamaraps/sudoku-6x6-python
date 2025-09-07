matriz= [[0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 6, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0]]

import random

def validar_jogada(matriz):
    while True:
        linha_escolida = int(input('Escolha uma linha de 0 a 5: '))
        coluna_escolhida = int(input('Escolha uma coluna de 0 a 5: '))

        if matriz[linha_escolida][coluna_escolhida] != 0:
            print('A célula já está preenchida, escolha outra.')
            continue 

        numero_jogada = int(input('Escreva um número de 1 a 6 para preencher: '))

        while True:
            if numero_jogada in matriz[linha_escolida]:
                print('O número já está presente na linha') 
                numero_jogada = int(input('Escreva um número de 1 a 6 para preencher: '))
                continue
                
            coluna = [linha[coluna_escolhida] for linha in matriz]
            if numero_jogada in coluna:
                print('O número já está presente na coluna')
                numero_jogada = int(input('Escreva um número de 1 a 6 para preencher: '))
                continue

            if 6 < numero_jogada or numero_jogada < 1:
                print('O número que você digitou não está entre 1 e 6')
                numero_jogada = int(input('Escreva um número de 1 a 6 para preencher: '))
                continue

            if not encontra_bloco(linha_escolida, coluna_escolhida, matriz, numero_jogada):
                print('O número já está presente no bloco 2x3.')
                numero_jogada = int(input('Escreva um número de 1 a 6 para preencher: '))
                continue

            matriz[linha_escolida][coluna_escolhida] = numero_jogada
            print('Jogada válida!')
            break

        break  

def encontra_bloco(linha_escolida,coluna_escolhida, matriz, numero_jogada):
    if linha_escolida < 2:
        linha_inicio = 0
    elif linha_escolida < 4:
        linha_inicio = 2
    else:
        linha_inicio = 4

    if coluna_escolhida < 3:
        coluna_inicio = 0
    else:
        coluna_inicio = 3

    for i in range(linha_inicio, linha_inicio + 2):
        for j in range(coluna_inicio, coluna_inicio + 3):
            if matriz[i][j] == numero_jogada:
                return False  
    return True  


def valido(matriz, linha, coluna, numero):

    if numero in matriz[linha]:
        return False


    for i in range(6):
        if matriz[i][coluna] == numero:
            return False

   
    if linha < 2:
        linha_inicio = 0
    elif linha < 4:
        linha_inicio = 2
    else:
        linha_inicio = 4

    if coluna < 3:
        coluna_inicio = 0
    else:
        coluna_inicio = 3

    for i in range(linha_inicio, linha_inicio + 2):
        for j in range(coluna_inicio, coluna_inicio + 3):
            if matriz[i][j] == numero:
                return False

    return True  


def preencher_matriz(matriz):
    for linha in range(6):
        for coluna in range(6):
            if matriz[linha][coluna] == 0:
                numeros = [1, 2, 3, 4, 5, 6]
                random.shuffle(numeros) 
                for numero in numeros:
                    if valido(matriz, linha, coluna, numero):
                        matriz[linha][coluna] = numero
                        if preencher_matriz(matriz):
                            return True
                        matriz[linha][coluna] = 0 
                return False 
    return True     


for linha in matriz:
    print(linha)

def gerar_espacos(matriz):
    contador = 0
    while contador < 10:
        linha_sorteada = random.randint(0,5)
        coluna_sorteada = random.randint(0,5)
        if matriz[linha_sorteada][coluna_sorteada] != 0:
            matriz[linha_sorteada][coluna_sorteada] = 0
            contador += 1



def imprimir_sudoku(matriz):
    for i in range(len(matriz)):
        if i != 0 and i % 2 == 0:
            print('*' * 13)

        for j in range(len(matriz[i])):
            if j != 0 and j % 3 == 0:
                print('*', end=' ')
            
            print(matriz[i][j], end=' ')
        
        print()  

def verificar_vitoria(matriz):
    for linha in matriz:
        if 0 in linha:
            return False
    print('Vocêe venceuuuuuu')
    return True



preencher_matriz(matriz)
gerar_espacos(matriz)

while True:
    imprimir_sudoku(matriz)
    validar_jogada(matriz)
    if verificar_vitoria(matriz):
        break
