matriz= [
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0]]

#cria uma matriz zerada, que será o tabuleiro

import random
#importa biblioteca para usar o random.randint(gera num aleatório) e random.shuffle (embaralha a lista)


#Função que valida se a linha, coluna e numero que o usuário escolheu é válido para a matriz


def validar_jogada(matriz):
    while True:
        try:
            linha = int(input('Escolha uma linha de 1 a 6: ')) - 1
            coluna = int(input('Escolha uma coluna de 1 a 6: ')) - 1
        except ValueError:
            print('⚠️ Digite números inteiros para linha e coluna.')
            continue

        if not (0 <= linha < 6 and 0 <= coluna < 6):
            print('⚠️ Linha ou coluna fora do intervalo (1 a 6). Tente novamente.')
            continue

        if matriz[linha][coluna] != 0:
            print('⚠️ A célula escolhida já está preenchida. Escolha outra.')
            continue

        try:
            numero = int(input('Escolha um número de 1 a 6 para preencher: '))
        except ValueError:
            print('⚠️ Digite um número inteiro entre 1 e 6.')
            continue

        if not (1 <= numero <= 6):
            print('⚠️ O número deve estar entre 1 e 6.')
            continue

        if not valido(matriz, linha, coluna, numero):
            print('❌ Jogada inválida: o número já existe na linha, coluna ou bloco.')
            continue

        # tudo certo -> insere e sai
        matriz[linha][coluna] = numero
        print('✅ Jogada válida!')
        return True  # ou return matriz se preferir retornar a matriz

 

def encontra_bloco(linha_escolhida,coluna_escolhida, matriz, numero_jogada):
    if linha_escolhida < 2:
        linha_inicio = 0
    elif linha_escolhida < 4:
        linha_inicio = 2
    else:
        linha_inicio = 4

    if coluna_escolhida < 3:
        coluna_inicio = 0
    else:
        coluna_inicio = 3
# ve em qual bloco está
    for i in range(linha_inicio, linha_inicio + 2):
        #percorre as duas linhas
        for j in range(coluna_inicio, coluna_inicio + 3):
            #percorre as 3 colunas
            if matriz[i][j] == numero_jogada:
                return False  
            #retorna false se o numero JÁ estiver no bloco
    return True  
    #num não está no bloco

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
                #percorre cada célula da matriz e vê se está vazia
                numeros = [1, 2, 3, 4, 5, 6]
                random.shuffle(numeros) 
                #embaralha a ordem aleatoriamente
                for numero in numeros:
                    #pega cada numero da lista embaralhada
                    if valido(matriz, linha, coluna, numero):
                        #se o num passar na função válido é adicionado na matriz
                        matriz[linha][coluna] = numero
                        #Aqui é feioto backtrcking e chamada recursiva
                        if preencher_matriz(matriz):
                            #chama a própria função dentro da função para tentar preencher a próxima célula 
                            return True
                            # se der certo até o fim retorna True
                        matriz[linha][coluna] = 0 
                        #Se em algum lugar der errado desfaz a última jogada e retorna false
                    #coloca o num na célula mas depois  não existe nenhum num q funcione nas outras células, então desfaz
                return False 
    return True     




def gerar_espacos(matriz):
    contador = 0
    while contador < 10:
        linha_sorteada = random.randint(0,5)
        coluna_sorteada = random.randint(0,5)
        if matriz[linha_sorteada][coluna_sorteada] != 0:
            matriz[linha_sorteada][coluna_sorteada] = 0
            contador += 1



def imprimir_sudoku(matriz):
    print('\n' + '═' * 25)
    print(' ' * 8 + 'SUDOKU 6x6')
    print('═' * 25)
    for i in range(len(matriz)):
        if i != 0 and i % 2 == 0:
            print('─' * 25)

        linha_str = ''
        for j in range(len(matriz[i])):
            if j != 0 and j % 3 == 0:
                linha_str += '│ '
            if matriz[i][j] == 0:
                linha_str += '. '
            else:
                linha_str += f'{matriz[i][j]} '
        print(linha_str)
    print('═' * 25 + '\n')

def verificar_vitoria(matriz):
    for linha in matriz:
        if 0 in linha:
            return False
    print('🎉 Parabéns! Você venceu o Sudoku!')
    return True



preencher_matriz(matriz)
gerar_espacos(matriz)

while True:
    imprimir_sudoku(matriz)
    validar_jogada(matriz)
    if verificar_vitoria(matriz):
        break
