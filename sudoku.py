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

    #Cria um loop infinito que irá rodar para que se o jogador erre le possa tentar de novo
    while True:
        linha_escolhida = int(input('Escolha uma linha de 0 a 5: '))
        coluna_escolhida = int(input('Escolha uma coluna de 0 a 5: '))
        #Coloca a linha e coluna escolhida em uma variável
        if matriz[linha_escolhida][coluna_escolhida] != 0:
            print('A célula já está preenchida, escolha outra.')
            continue 
        #verifica se a célula está preenchida, se estiver o CONTINUE vplta para o início do loop e ignora o resto do código
        numero_jogada = int(input('Escreva um número de 1 a 6 para preencher: '))
        #se estiver vazio pede um num e armazena
        while True:
            #loop que verifica o numero digitado
            if numero_jogada in matriz[linha_escolhida]:
                #verifica se o valor está dentro (IN) da linha
                print('O número já está presente na linha') 
                numero_jogada = int(input('Escreva um número de 1 a 6 para preencher: '))
                continue
                #volta para o início da validação
                
            coluna = [linha[coluna_escolhida] for linha in matriz]
            # percorre as linhas na matriz e permaanece na coluna escolhida e reserva a coluna em uma variável
            if numero_jogada in coluna:
                print('O número já está presente na coluna')
                numero_jogada = int(input('Escreva um número de 1 a 6 para preencher: '))
                continue
            #verifica se o num está na coluna

            if 6 < numero_jogada or numero_jogada < 1:
                print('O número que você digitou não está entre 1 e 6')
                numero_jogada = int(input('Escreva um número de 1 a 6 para preencher: '))
                continue

            if not encontra_bloco(linha_escolhida, coluna_escolhida, matriz, numero_jogada):
                print('O número já está presente no bloco 2x3.')
                numero_jogada = int(input('Escreva um número de 1 a 6 para preencher: '))
                continue
                #Se for False o número já está no bloco

            matriz[linha_escolhida][coluna_escolhida] = numero_jogada
            print('Jogada válida!')
            break
        #Se tiver tudo certo adiciona na posição escolhida o num escolhido

        break  

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
    print('*****************')
    print('     SUDOKU      ')
    print('*****************')
    for i in range(len(matriz)):
        if i != 0 and i % 2 == 0:
            print('*' * 13)

        for j in range(len(matriz[i])):
            if j != 0 and j % 3 == 0:
                print('*', end=' ')
                #não quebra linha, imprime o espaço
            print(matriz[i][j], end=' ')
        
        print()  
        #quebra linha no final de cada linha

def verificar_vitoria(matriz):
    for linha in matriz:
        if 0 in linha:
            return False
    print('Vocêe venceu, parabéns')
    return True



preencher_matriz(matriz)
gerar_espacos(matriz)

while True:
    imprimir_sudoku(matriz)
    validar_jogada(matriz)
    if verificar_vitoria(matriz):
        break
