import sys
sys.setrecursionlimit(16385)  # importado para aumentar o limite de recursões


def balde(matriz, cor_nova, cor_antiga, limiar, semente, linha, coluna):
    '''
    Função feita para preencher as regiões conexas a uma região "semente" com
    uma cor específica "cor_nova". O parâmetro "cor_antiga" identifica a
    cor do pixel semente, para ser feita a análise se o pixel deve ser
    pintado pelo balde ou não, dentro do limite definido pelo "limiar"
    e calculado pelo "parâmetro".
    '''
    # caso esteja procurando fora da matriz
    if linha < 0 or linha >= len(matriz) or coluna < 0 or coluna >= len(matriz[0]):
        return matriz
    # caso em que o pixel analisado e igual a cor_nova, o que deve parar a expansão
    elif matriz[linha][coluna] == cor_nova:
        return matriz
    # caso em que o pixel já foi alterado, parando a expansão naquela direção
    elif type(matriz[linha][coluna]) == str:
        return matriz

    # calcula se o pixel deve ser alterado ou não
    parametro = abs(matriz[linha][coluna] - cor_antiga)

    # caso para alterar o pixel da semente, alteramos sempre para uma string
    # para identificar que aquele pixel já foi alterado, para evitar repetições.
    if linha == semente[1] and coluna == semente[0]:
        matriz[linha][coluna] = str(cor_nova)
    # para os pixels que devem ser pintados com a cor nova
    elif parametro <= limiar:
        matriz[linha][coluna] = str(cor_nova)
    # caso em que o pixel não deve ser pintado, encerrando a expansão para ele
    elif parametro > limiar:
        return matriz

    # recursão de cada pixel expandindo em todas as direções
    matriz = balde(matriz, cor_nova, cor_antiga, limiar, semente, linha - 1, coluna)  # cima
    matriz = balde(matriz, cor_nova, cor_antiga, limiar, semente, linha + 1, coluna)  # baixo
    matriz = balde(matriz, cor_nova, cor_antiga, limiar, semente, linha, coluna - 1)  # esquerda
    matriz = balde(matriz, cor_nova, cor_antiga, limiar, semente, linha, coluna + 1)  # direita
    matriz = balde(matriz, cor_nova, cor_antiga, limiar, semente, linha - 1, coluna - 1)  # noroeste
    matriz = balde(matriz, cor_nova, cor_antiga, limiar, semente, linha + 1, coluna + 1)  # sudeste
    matriz = balde(matriz, cor_nova, cor_antiga, limiar, semente, linha - 1, coluna + 1)  # nordeste
    matriz = balde(matriz, cor_nova, cor_antiga, limiar, semente, linha + 1, coluna - 1)  # sudoeste

    return matriz


def negativo(matriz, cor_antiga, pixel_max, limiar, semente, linha, coluna):
    '''
    Função para inverter as cores das regiões conexas a uma região semente
    (intensidade pixel_max - cor pixel atual). As descrições linha a linha
    desta função são iguais a da função balde. Omitimos aqui para evitar
    repetição.
    '''
    if linha < 0 or linha >= len(matriz) or coluna < 0 or coluna >= len(matriz[0]):
        return matriz

    elif type(matriz[linha][coluna]) == str:
        return matriz

    parametro = abs(matriz[linha][coluna] - cor_antiga)

    if linha == semente[1] and coluna == semente[0]:
        matriz[linha][coluna] = str(pixel_max - matriz[linha][coluna])

    elif parametro <= limiar:
        matriz[linha][coluna] = str(pixel_max - matriz[linha][coluna])

    elif parametro > limiar:
        return matriz

    matriz = negativo(matriz, cor_antiga, pixel_max, limiar, semente, linha - 1, coluna)  # cima
    matriz = negativo(matriz, cor_antiga, pixel_max, limiar, semente, linha + 1, coluna)  # baixo
    matriz = negativo(matriz, cor_antiga, pixel_max, limiar, semente, linha, coluna - 1)  # esquerda
    matriz = negativo(matriz, cor_antiga, pixel_max, limiar, semente, linha, coluna + 1)  # direita
    matriz = negativo(matriz, cor_antiga, pixel_max, limiar, semente, linha - 1, coluna - 1)  # noroeste
    matriz = negativo(matriz, cor_antiga, pixel_max, limiar, semente, linha + 1, coluna + 1)  # sudeste
    matriz = negativo(matriz, cor_antiga, pixel_max, limiar, semente, linha - 1, coluna + 1)  # nordeste
    matriz = negativo(matriz, cor_antiga, pixel_max, limiar, semente, linha + 1, coluna - 1)  # sudoeste

    return matriz


def mascara(matriz, cor_antiga, limiar, semente, linha, coluna):
    '''
    Função para retornar uma imagem binária (máscara) contendo 0 nos pixels
    pertencentes a região conexa contendo o pixel semente, e 255 nas demais
    regiões não-conexas. As descrições linha a linha desta função são iguais
    a da função balde. Omitimos aqui para evitar repetição.
    '''
    if linha < 0 or linha >= len(matriz) or coluna < 0 or coluna >= len(matriz[0]):
        return matriz

    elif type(matriz[linha][coluna]) == str:
        return matriz

    parametro = abs(matriz[linha][coluna] - cor_antiga)

    if linha == semente[1] and coluna == semente[0]:
        matriz[linha][coluna] = str(0)

    elif parametro <= limiar:
        matriz[linha][coluna] = str(0)

    elif parametro > limiar:
        return matriz

    matriz = mascara(matriz, cor_antiga, limiar, semente, linha - 1, coluna)  # cima
    matriz = mascara(matriz, cor_antiga, limiar, semente, linha + 1, coluna)  # baixo
    matriz = mascara(matriz, cor_antiga, limiar, semente, linha, coluna - 1)  # esquerda
    matriz = mascara(matriz, cor_antiga, limiar, semente, linha, coluna + 1)  # direita
    matriz = mascara(matriz, cor_antiga, limiar, semente, linha - 1, coluna - 1)  # noroeste
    matriz = mascara(matriz, cor_antiga, limiar, semente, linha + 1, coluna + 1)  # sudeste
    matriz = mascara(matriz, cor_antiga, limiar, semente, linha - 1, coluna + 1)  # nordeste
    matriz = mascara(matriz, cor_antiga, limiar, semente, linha + 1, coluna - 1)  # sudoeste

    return matriz


def salvar(matriz, coluna_linha, pixel_max):
    '''
    Função para salvar a imagem, ou seja, irá imprimir a situação
    final da imagem após as alterações feitas.
    '''
    print('P2')
    print('# Imagem criada pelo lab13')
    print(' '.join(map(str, coluna_linha)))
    print(pixel_max)
    for i in range(coluna_linha[1]):
        print(' '.join(map(str, matriz[i])))


def correcao(matriz):
    '''
    Função criada para voltar os pixels alterados, que agora são
    strings, para números inteiros. Desta forma será possível
    fazer as próximas operações.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if type(matriz[i][j]) == str:
                matriz[i][j] = int(matriz[i][j])

    return matriz


def correcao_mascara(matriz, pixel_max):
    '''
    Função que continua a operação de máscara, transformando os
    pixels não alterados e não conexos a semente para a intensidade
    máxima.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if type(matriz[i][j]) != str:
                matriz[i][j] = pixel_max

    return matriz


def processamento(arquivo):
    '''
    Função para extrair os dados do arquivo de imagem, salvando
    seu tamanho, intensidade máxima do pixel e o valor de cada
    pixel, que será salvo em uma matriz.
    '''
    texto = open(arquivo)
    matriz = []

    for indice, linha in enumerate(texto):
        if indice == 2:
            coluna_linha = tuple(map(int, linha.rsplit()))
        elif indice == 3:
            pixel_max = int(linha.rstrip())
        elif indice > 3:
            matriz.append(list(map(int, linha.rsplit())))

    texto.close()

    return coluna_linha, pixel_max, matriz


def entradas():
    '''
    Função para salvar as entradas do programa
    '''
    arquivo = input()
    n_operacoes = int(input())
    lista_operacoes = []

    for _ in range(n_operacoes):
        lista_operacoes.append(input().split())

    return arquivo, n_operacoes, lista_operacoes


def main():
    arquivo, n_operacoes, lista_operacoes = entradas()
    coluna_linha, pixel_max, matriz = processamento(arquivo)

    # percorre a lista de operações, buscando o nome dela e executando cada
    # função correspondente a operação.
    for i in range(n_operacoes):
        nome_operacao = lista_operacoes[i][0]
        if nome_operacao == 'bucket':
            matriz = balde(matriz, int(lista_operacoes[i][1]), matriz[int(lista_operacoes[i][4])][int(lista_operacoes[i][3])],\
                           int(lista_operacoes[i][2]), tuple([int(lista_operacoes[i][3]), int(lista_operacoes[i][4])]),\
                           int(lista_operacoes[i][4]), int(lista_operacoes[i][3]))
            matriz = correcao(matriz)

        elif nome_operacao == 'negative':
            matriz = negativo(matriz, matriz[int(lista_operacoes[i][3])][int(lista_operacoes[i][2])], pixel_max,\
                              int(lista_operacoes[i][1]), tuple([int(lista_operacoes[i][2]), int(lista_operacoes[i][3])]),\
                              int(lista_operacoes[i][3]), int(lista_operacoes[i][2]))
            matriz = correcao(matriz)

        elif nome_operacao == 'cmask':
            matriz = mascara(matriz, matriz[int(lista_operacoes[i][3])][int(lista_operacoes[i][2])], int(lista_operacoes[i][1]),\
                             tuple([int(lista_operacoes[i][2]), int(lista_operacoes[i][3])]), int(lista_operacoes[i][3]),\
                             int(lista_operacoes[i][2]))
            matriz = correcao_mascara(matriz, pixel_max)
            matriz = correcao(matriz)

        elif nome_operacao == 'save':
            salvar(matriz, coluna_linha, pixel_max)


if __name__ == "__main__":
    main()
