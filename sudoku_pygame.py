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
            linha = int(input('Escolha uma linha de 0 a 5: '))
            coluna = int(input('Escolha uma coluna de 0 a 5: '))
        except ValueError:
            print('Digite números inteiros para linha e coluna.')
            continue

        if not (0 <= linha < 6 and 0 <= coluna < 6):
            print('Linha ou coluna fora do intervalo (0 a 5). Tente novamente.')
            continue

        if matriz[linha][coluna] != 0:
            print('A célula escolhida já está preenchida. Escolha outra.')
            continue

        try:
            numero = int(input('Escreva um número de 1 a 6 para preencher: '))
        except ValueError:
            print('Digite um número inteiro entre 1 e 6.')
            continue

        if not (1 <= numero <= 6):
            print('O número deve estar entre 1 e 6.')
            continue

        if not valido(matriz, linha, coluna, numero):
            print('Jogada inválida: número já existe na linha, coluna ou bloco.')
            continue

        # tudo certo -> insere e sai
        matriz[linha][coluna] = numero
        print('Jogada válida!')
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

import pygame
import random

# =========================================
# Use seu código de lógica do Sudoku aqui
# =========================================
# matriz, valido(), verificar_vitoria(), preencher_matriz(), gerar_espacos()
# Supondo que você já tenha:
# preencher_matriz(matriz)
# gerar_espacos(matriz)

# Para teste rápido, exemplo mínimo:
matriz = [[0]*6 for _ in range(6)]

def valido(matriz, l, c, n):
    if n in matriz[l]: return False
    for i in range(6):
        if matriz[i][c] == n: return False
    linha_inicio = (l//2)*2
    coluna_inicio = (c//3)*3
    for i in range(linha_inicio, linha_inicio+2):
        for j in range(coluna_inicio, coluna_inicio+3):
            if matriz[i][j] == n: return False
    return True

def verificar_vitoria(matriz):
    for linha in matriz:
        if 0 in linha: return False
    return True

def preencher_matriz(matriz):
    for l in range(6):
        for c in range(6):
            if matriz[l][c]==0:
                nums=[1,2,3,4,5,6]
                random.shuffle(nums)
                for n in nums:
                    if valido(matriz,l,c,n):
                        matriz[l][c]=n
                        if preencher_matriz(matriz):
                            return True
                        matriz[l][c]=0
                return False
    return True

def gerar_espacos(matriz):
    cnt=0
    while cnt<10:
        l=random.randint(0,5)
        c=random.randint(0,5)
        if matriz[l][c]!=0:
            matriz[l][c]=0
            cnt+=1

preencher_matriz(matriz)
gerar_espacos(matriz)


import pygame
import random

# =========================
# INICIALIZAÇÃO DO PYGAME
# =========================

pygame.init()  # inicia o Pygame (obrigatório antes de usar qualquer função do Pygame)

LARGURA = 600  # largura da tela do Sudoku
ALTURA = 600   # altura da tela do Sudoku
TAMANHO_CELULA = LARGURA // 6  # cada célula será 1/6 da largura
TELA = pygame.display.set_mode((LARGURA, ALTURA + 50))  # cria a tela, deixando espaço extra embaixo para mensagens
pygame.display.set_caption("Sudoku 6x6")  # título da janela

# =========================
# FONTES (texto na tela)
# =========================

FONTE_NUMERO = pygame.font.SysFont("Arial", 40)  # fonte para os números do Sudoku
FONTE_MSG = pygame.font.SysFont("Arial", 28, bold=True)  # fonte para mensagens
FONTE_VITORIA = pygame.font.SysFont("Arial", 60, bold=True)  # fonte grande para vitória

# =========================
# CORES
# =========================

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)  # cor dos números digitados pelo usuário
AZUL_CLARO = (173, 216, 230)  # cor da célula selecionada
VERDE = (0, 200, 0)  # mensagem de jogada válida / vitória
VERMELHO = (200, 0, 0)  # mensagem de jogada inválida
ROSA_CLARO = (255, 192, 203)  # cor de fundo dos blocos 2x3

jogadas_usuario = []  # lista para guardar as posições onde o usuário digitou números

# =========================
# FUNÇÃO PARA DESENHAR O TABULEIRO
# =========================

def desenhar_tabuleiro(matriz, celula_selecionada=None, mensagem="", cor_msg=PRETO, vitoria=False):
    # se não venceu ainda
    if not vitoria:
        # percorre cada célula da matriz
        for i in range(6):
            for j in range(6):
                # define a cor do bloco 2x3
                cor_fundo = ROSA_CLARO if (i//2 + j//3) % 2 == 0 else BRANCO
                # desenha o fundo da célula
                pygame.draw.rect(TELA, cor_fundo, (j*TAMANHO_CELULA, i*TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))

        # percorre a matriz de novo para desenhar os números
        for i in range(6):
            for j in range(6):
                num = matriz[i][j]
                if num != 0:
                    # se o número foi digitado pelo usuário, pinta de azul
                    cor_num = AZUL if (i, j) in jogadas_usuario else PRETO
                    # cria o texto
                    texto = FONTE_NUMERO.render(str(num), True, cor_num)
                    # coloca o texto na célula (com um pequeno deslocamento para centralizar)
                    TELA.blit(texto, (j*TAMANHO_CELULA + 20, i*TAMANHO_CELULA + 10))

        # desenha as linhas do tabuleiro
        for i in range(7):
            # linhas horizontais, mais grossas a cada 2 linhas
            pygame.draw.line(TELA, PRETO, (0, i*TAMANHO_CELULA), (LARGURA, i*TAMANHO_CELULA), 4 if i in [0,2,4,6] else 2)
        for j in range(7):
            # linhas verticais, mais grossas a cada 3 colunas
            pygame.draw.line(TELA, PRETO, (j*TAMANHO_CELULA, 0), (j*TAMANHO_CELULA, ALTURA), 4 if j in [0,3,6] else 2)

        # se o usuário clicou em uma célula
        if celula_selecionada:
            l, c = celula_selecionada
            # pinta a célula clicada de azul claro
            pygame.draw.rect(TELA, AZUL_CLARO, (c*TAMANHO_CELULA, l*TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))
            # desenha uma borda azul escuro ao redor da célula
            pygame.draw.rect(TELA, AZUL, (c*TAMANHO_CELULA, l*TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA), 3)

        # desenha a área de mensagens em branco
        pygame.draw.rect(TELA, BRANCO, (0, ALTURA, LARGURA, 50))
        if mensagem:
            # escreve a mensagem centralizada
            texto_msg = FONTE_MSG.render(mensagem, True, cor_msg)
            x_msg = (LARGURA - texto_msg.get_width()) // 2
            y_msg = ALTURA + 10
            TELA.blit(texto_msg, (x_msg, y_msg))

    # se venceu
    else:
        TELA.fill(BRANCO)  # fundo branco
        # mensagem grande de vitória
        texto_vitoria = FONTE_VITORIA.render("VOCÊ VENCEU!", True, VERDE)
        x_texto = (LARGURA - texto_vitoria.get_width()) // 2
        y_texto = ALTURA//2 - texto_vitoria.get_height() // 2
        TELA.blit(texto_vitoria, (x_texto, y_texto))

        # efeito simples de confete colorido
        cores_confete = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)]
        for _ in range(50):
            x = random.randint(0, LARGURA)
            y = random.randint(0, ALTURA)
            pygame.draw.circle(TELA, random.choice(cores_confete), (x,y), 5)

    # atualiza a tela
    pygame.display.update()

# =========================
# LOOP PRINCIPAL DO JOGO
# =========================

celula_selecionada = None  # célula que o usuário clicou
mensagem = ""  # mensagem para mostrar na parte de baixo
cor_msg = PRETO  # cor da mensagem
vitoria = False  # status de vitória

rodando = True
while rodando:
    # desenha todo o tabuleiro e mensagens
    desenhar_tabuleiro(matriz, celula_selecionada, mensagem, cor_msg, vitoria)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # se o usuário clicar no X para fechar
            rodando = False

        if not vitoria:
            # se o usuário clicou com o mouse
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  # pega posição do clique
                if y < ALTURA:  # só se clicou dentro do tabuleiro
                    l = y // TAMANHO_CELULA
                    c = x // TAMANHO_CELULA
                    if matriz[l][c] == 0:  # só permite selecionar células vazias
                        celula_selecionada = (l,c)

            # se o usuário apertou uma tecla
            if evento.type == pygame.KEYDOWN and celula_selecionada:
                if evento.unicode.isdigit():  # se a tecla é número
                    numero = int(evento.unicode)
                    l, c = celula_selecionada
                    if 1 <= numero <= 6:  # número válido
                        if valido(matriz, l, c, numero):  # se a jogada é válida
                            matriz[l][c] = numero  # preenche o Sudoku
                            jogadas_usuario.append((l,c))  # marca como jogada do usuário
                            mensagem = "Jogada válida!"
                            cor_msg = VERDE
                            celula_selecionada = None  # desmarca célula
                            if verificar_vitoria(matriz):  # checa vitória
                                vitoria = True
                        else:  # número repetido
                            mensagem = "Jogada inválida!"
                            cor_msg = VERMELHO
                    else:  # número fora do intervalo 1-6
                        mensagem = "Digite um número de 1 a 6!"
                        cor_msg = VERMELHO
                else:  # tecla não é número
                    mensagem = "Digite um número de 1 a 6!"
                    cor_msg = VERMELHO

pygame.quit()  # fecha o Pygame quando o loop termina
