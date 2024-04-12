def escaneando_ambiente(robot, n_linhas, casas, matriz):
    '''
    Esta função escaneia todo o ambiente da matriz, guiando o
    robô. Ela analisa se existe sujeira em volta do robô dependendo
    se está em uma linha par ou ímpar. Tendo sujeira por perto é
    chamada a função "limpando" seguida da função "voltando" ou
    ainda sendo chamada recursivamente, caso o robô tenha apenas
    limpado uma sujeira que já estava no seu caminho corrente.
    Caso não tenha sujeira, continua chamando a função "andando".
    '''

    # Esse primeiro if serve para que o robô não pergunte por casos fora da matriz, podendo seguir "andando"
    if ((robot["linha"] == n_linhas - 1) or (robot["coluna"] == len(matriz[0]) - 1 and robot["linha"] % 2 == 0) or
            (robot["coluna"] == 0 and robot["linha"] % 2 == 1)):
        casas = andando(casas, n_linhas, matriz, robot)

    else:
        # Precisamos desse if pois se o robô está em uma linha par ele deve procurar sujeira nas casas à direita e embaixo
        if robot["linha"] % 2 == 0:
            if matriz[robot["linha"]][robot["coluna"] + 1] == 'o':
                casas = andando(casas, n_linhas, matriz, robot)
            elif matriz[robot["linha"] + 1][robot["coluna"]] == 'o':
                anterior = (robot["linha"], robot["coluna"])  # Salva a posição do robô quando achou sujeira pela primeira vez
                limpando(matriz, n_linhas, robot)

                if (robot["linha"] == anterior[0] and robot["coluna"] == anterior[1] + 1):
                    casas += 2
                    escaneando_ambiente(robot, n_linhas, casas, matriz)
                else:
                    voltando(matriz, n_linhas, robot, anterior)
            else:
                casas = andando(casas, n_linhas, matriz, robot)

        # Nas linhas ímpares, o robô deve procurar sujeira nas casas à sua esquerda e embaixo
        else:
            if matriz[robot["linha"]][robot["coluna"] - 1] == 'o':
                casas = andando(casas, n_linhas, matriz, robot)
            elif matriz[robot["linha"] + 1][robot["coluna"]] == 'o':
                anterior = (robot["linha"], robot["coluna"])
                limpando(matriz, n_linhas, robot)

                if (robot["linha"] == anterior[0] and robot["coluna"] == anterior[1] - 1):
                    casas += 2
                    escaneando_ambiente(robot, n_linhas, casas, matriz)
                else:
                    voltando(matriz, n_linhas, robot, anterior)
            else:
                casas = andando(casas, n_linhas, matriz, robot)

    return casas


def andando(casas, n_linhas, matriz, robot):
    '''
    Função que é chamada pela função "escaneando_ambiente", apenas para
    agrupar a função "caminho_corrente" e "imprimir_caminho".
    '''

    casas = caminho_corrente(robot, matriz, n_linhas, casas)
    imprimir_momento(matriz, n_linhas)

    return casas


def imprimir_momento(matriz, n_linhas):
    '''
    Função para imprimir a situação da matriz, sempre que o robô muda
    de posição, para assim, acompanharmos todo o percurso.
    '''

    print()
    for i in range(n_linhas):
        print(' '.join(matriz[i]))


def caminho_corrente(robot, matriz, n_linhas, casas):
    '''
    Função que guia o robô pela matriz, ela é chamada quando não existe
    sujeira por perto e o robô pode seguir seu caminho pela matriz até
    encontrar nova sujeira pelas imediações. Esta é a função que incrementa
    a variável casas, para saber a hora que o robô tem que parar.
    '''

    matriz[robot["linha"]][robot["coluna"]] = "."
    # Em linhas pares o robô deve andar para a direita, devendo nos atentar para quando o robô muda de linha.
    if n_linhas % 2 == 0:
        if robot["linha"] % 2 == 0 and robot["linha"] != n_linhas - 1:
            if robot["coluna"] == len(matriz[0]) - 1:
                robot["linha"] += 1
            else:
                robot["coluna"] += 1

        elif robot["linha"] == n_linhas - 1:
            if casas >= n_linhas * len(matriz[0]):
                robot["coluna"] += 1
            else:
                robot["coluna"] -= 1

        else:
            if robot["coluna"] == 0:
                robot["linha"] += 1
            else:
                robot["coluna"] -= 1
    else:
        if robot["linha"] % 2 == 0:
            if robot["coluna"] == len(matriz[0]) - 1:
                robot["linha"] += 1
            else:
                robot["coluna"] += 1
        else:
            if robot["coluna"] == 0:
                robot["linha"] += 1
            else:
                robot["coluna"] -= 1

    matriz[robot["linha"]][robot["coluna"]] = "r"

    casas += 1

    return casas


def limpando(matriz, n_linhas, robot, primeiro=0):
    '''
    Função que realiza a limpeza e constante procura de sujeira na matriz, após a primeira sujeira
    ter sido identificada pela função "escaneando_ambiente".
    '''

    while True:
        primeiro += 1 
        ''' "primeiro" Serve para sabermos a primeira vez que o robô está limpando 
        uma sujeira, pois neste caso não é necessário seguir a mesma direção'''
         
        # procurando para a esquerda
        if robot["coluna"] != 0 and matriz[robot["linha"]][robot["coluna"] - 1] == "o":
            while matriz[robot["linha"]][robot["coluna"] - 1] == "o":
                matriz[robot["linha"]][robot["coluna"]] = "."
                robot["coluna"] -= 1
                matriz[robot["linha"]][robot["coluna"]] = "r"
                imprimir_momento(matriz, n_linhas)
                if robot["coluna"] == 0 or primeiro == 1:
                    break

        # procurando para cima
        elif robot["linha"] != 0 and matriz[robot["linha"] - 1][robot["coluna"]] == "o":
            while matriz[robot["linha"] - 1][robot["coluna"]] == "o":
                matriz[robot["linha"]][robot["coluna"]] = "."
                robot["linha"] -= 1
                matriz[robot["linha"]][robot["coluna"]] = "r"
                imprimir_momento(matriz, n_linhas)
                if robot["linha"] == 0 or primeiro == 1:
                    break

        # procurando para a direita
        elif robot["coluna"] != len(matriz[0]) - 1 and matriz[robot["linha"]][robot["coluna"] + 1] == "o":
            while matriz[robot["linha"]][robot["coluna"] + 1] == "o":
                matriz[robot["linha"]][robot["coluna"]] = "."
                robot["coluna"] += 1
                matriz[robot["linha"]][robot["coluna"]] = "r"
                imprimir_momento(matriz, n_linhas)
                if robot["coluna"] == len(matriz[0]) - 1 or primeiro == 1:
                    break

        # procurando para baixo
        elif robot["linha"] != n_linhas - 1 and matriz[robot["linha"] + 1][robot["coluna"]] == "o":
            while matriz[robot["linha"] + 1][robot["coluna"]] == "o":
                matriz[robot["linha"]][robot["coluna"]] = "."
                robot["linha"] += 1
                matriz[robot["linha"]][robot["coluna"]] = "r"
                imprimir_momento(matriz, n_linhas)
                if robot["linha"] == n_linhas - 1 or primeiro == 1:
                    break
        else:
            break


def voltando(matriz, n_linhas, robot, anterior):
    '''
    Função feita para que o robô retorne a posição da matriz
    de quando encontrou uma sujeira pela primeira vez. Note
    que enquanto ele está voltando, pode também encontrar outras
    sujeiras e continuar limpando, retornando a posição original
    chamada de "anterior" após terminar.
    '''

    while anterior[1] != robot["coluna"]:
        if anterior[1]-robot["coluna"] < 0:
            # andando para esquerda
            matriz[robot["linha"]][robot["coluna"]] = "."
            robot["coluna"] -= 1

        else:
            # andando para direita
            matriz[robot["linha"]][robot["coluna"]] = "."
            robot["coluna"] += 1

        matriz[robot["linha"]][robot["coluna"]] = "r"
        imprimir_momento(matriz, n_linhas)
        limpando(matriz, n_linhas, robot)

    while anterior[0] != robot["linha"]:
        # andando para cima
        matriz[robot["linha"]][robot["coluna"]] = "."
        robot["linha"] -= 1
        matriz[robot["linha"]][robot["coluna"]] = "r"
        imprimir_momento(matriz, n_linhas)
        limpando(matriz, n_linhas, robot)


def main():
    n_linhas = int(input())  # número de linhas da matriz
    matriz = []
    robot = {"linha": 0, "coluna": 0}  # posição do robô
    casas = 1  # serve para saber quantas vezes o robô mudou de casa enquanto faz a função "caminho_corrente"

    # feito para receber a situação inicial da matriz
    for i in range(n_linhas):
        linha = input().split()
        matriz.append(linha)

    # feito para imprimir a situação inicial da matriz
    for i in range(n_linhas):
        print(' '.join(matriz[i]))

    # distinção para saber se a matriz tem número par ou ímpar de colunas
    if n_linhas % 2 == 0:
        # quando par, o robô além de andar por todas as casas da matriz, deve retornar para a posição final pela última linha
        while casas < n_linhas * len(matriz[0]) + (len(matriz[0])-1):
            casas = escaneando_ambiente(robot, n_linhas, casas, matriz)

    else:
        # quando ímpar, o robô necessita andar apenas por todas as casas da matriz
        while casas < n_linhas * len(matriz[0]):
            casas = escaneando_ambiente(robot, n_linhas, casas, matriz)


if __name__ == "__main__":
    main()
