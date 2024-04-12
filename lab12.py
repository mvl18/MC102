class Monte:
    def __init__(self, cartas):
        '''
        Cria a classe Jogador
        '''
        self.cartas = cartas

    def transformacao_letra_numero(self):
        '''
        Função feita para transformar as letras dos nomes das cartas
        em números para posterior comparação de força entre elas.
        '''
        # primeiramente vamos transformar as strings do nome das cartas em lista modificável
        lista = []
        for m in range(len(self.cartas)):
            lista.append(list(self.cartas[m]))

        # vamos trocar as letras dos naipes por números, seguindo a força
        inversao_naipes = {'O': '2', 'E': '3', 'C': '4', 'P': '5'}
        for i in range(len(lista)):
            for j in inversao_naipes:
                if j == lista[i][-1]:
                    lista[i][-1] = inversao_naipes[j]
                    break

        # agora trocamos o nome das cartas por números
        inversao_nomes = {'A': '1', 'J': '11', 'Q': '12', 'K': '13'}
        for i in range(len(lista)):
            for j in inversao_nomes:
                if j == lista[i][0]:
                    lista[i][0] = inversao_nomes[j]
                    break

        # transformamos as strings em números inteiros e salvamos na lista de cada objeto
        for i in range(len(lista)):
            if len(lista[i]) == 3:
                # para quando a carta tinha valor 10, 11 ou 12, o que acabou separando dezenas de unidades
                self.cartas[i] = int(lista[i][0] + lista[i][1] + lista[i][2])
            else:    
                # vale ressaltar que o naipe da carta ficará como o algarismo das unidades
                self.cartas[i] = int(lista[i][0])*10 + int(lista[i][1])

    def transformacao_numero_letra(self):
        '''
        Função feita para transformar os números nos nomes das cartas originalmente para imprimir
        '''
        lista = []
        for i in range(len(self.cartas)):
            lista.append(self.cartas[i] // 10)
            lista.append(self.cartas[i] % 10)

        lista = list(map(str, lista))

        inversao_nomes = {'1': 'A', '11': 'J', '12': 'Q', '13': 'K'}
        for i in range(0, len(lista), 2):
            for j in inversao_nomes:
                if j == lista[i]:
                    lista[i] = inversao_nomes[j]
                    break

        inversao_naipes = {'2': 'O', '3': 'E', '4': 'C', '5': 'P'}
        for i in range(1, len(lista), 2):
            for j in inversao_naipes:
                if j == lista[i]:
                    lista[i] = inversao_naipes[j]
                    break

        cartas = []
        for i in range(0, len(lista), 2):
            cartas.append(lista[i] + lista[i+1])

        return cartas

    def cartas_atuais(self):
        '''
        Função para imprimir as cartas de cada jogador já em ordem decrescente
        '''
        cartas = self.transformacao_numero_letra()
        for i in range(len(cartas)):
            if i != len(cartas) - 1:
                print(cartas[i], end=' ')
            else:
                print(cartas[i])


def busca_binaria(cartas, valor):
    '''
    Função criada para saber se o jogador tem uma carta para jogar
    '''
    inicio = 0 # indice mínimo para a busca na lista de cartas
    fim = len(cartas) - 1 # indice máximo para a busca na lista de cartas
    while inicio <= fim:
        meio = (inicio + fim)//2
        if cartas[meio] // 10 == valor:
            return cartas[meio]
        elif cartas[meio] // 10 < valor:
            fim = meio - 1
        else:
            inicio = meio + 1
    return 0


def jogada(i, jogadores, pilha, n):
    '''
    Função para imprimir a quantidade de cartas jogadas pelo jogador
    seguida pelo valor da carta. Essas cartas descartadas são
    adicionadas na pilha.
    '''
    descarte = []  # lista com todas as cartas que serão descartadas pelo jogador
    n_inicial = n
    blefe = False
    adicionar = 0
    adicionar += busca_binaria(jogadores[i].cartas, n)  # recebe a carta com o valor mínimo permitido
    while adicionar == 0 and n <= 13:  # caso ele tenha que jogar uma carta de maior valor do que o anterior
        n += 1
        adicionar += busca_binaria(jogadores[i].cartas, n)
    if adicionar != 0:  # quando encontra o valor da carta que irá descartar, procura se tem outras do mesmo valor
        descarte.append(adicionar)
        jogadores[i].cartas.remove(adicionar)
        while adicionar != 0:
            adicionar = 0
            adicionar += busca_binaria(jogadores[i].cartas, n)
            if adicionar != 0:
                descarte.append(adicionar)
                jogadores[i].cartas.remove(adicionar)

    else:  # caso ele não tenha nenhuma carta favorável, irá blefar!
        blefe = True
        n = 1
        adicionar += busca_binaria(jogadores[i].cartas, n)
        while adicionar == 0 and n <= n_inicial:
            n += 1
            adicionar += busca_binaria(jogadores[i].cartas, n)
        if adicionar != 0:
            descarte.append(adicionar)
            jogadores[i].cartas.remove(adicionar)
            while adicionar != 0:
                adicionar = 0
                adicionar += busca_binaria(jogadores[i].cartas, n)
                if adicionar != 0:
                    descarte.append(adicionar)
                    jogadores[i].cartas.remove(adicionar)

    if blefe:
        x = n_inicial
    else:
        x = n

    m = x
    if m == 1 or m > 10:
        if m == 1:
            m = 'A'
        elif m == 11:
            m = 'J'
        elif m == 12:
            m = 'Q'
        elif m == 13:
            m = 'K'

    print('[Jogador {}] {} carta(s) {}'.format(i + 1, len(descarte), m))

    descarte = ordenamento(descarte)  # ordena o descarte na ordem decrescente
    descarte = descarte[::-1]  # muda da ordem decrescente para ordem crescente para descartar
    for i in range(len(descarte)):
        pilha.cartas.append(descarte[i])
    print('Pilha:', end=' ')
    pilha.cartas_atuais()

    return x, blefe


def ordenamento(lista):
    '''
    Função para ordenar as cartas, que já estão transformadas em números inteiros
    seguindo a ordem de força
    '''
    for i in range(len(lista)):
        indice_maior_valor = i
        for j in range(i + 1, len(lista)):
            if lista[j] > lista[i]:
                indice_maior_valor = j
                lista[i], lista[indice_maior_valor] = lista[indice_maior_valor], lista[i]

    return lista


def situacao_jogo(jogadores):
    '''
    Imprime a situação do jogo no início do jogo, após o duvido e no final
    '''
    for i in range(len(jogadores)):
        print('Jogador {}'.format(i+1))
        if len(jogadores[i].cartas) == 0:
            print('Mão:')
        else:
            print('Mão:', end=' ')
            jogadores[i].cartas = ordenamento(jogadores[i].cartas)
            jogadores[i].cartas_atuais()
    print('Pilha:')


def entradas():
    '''
    Recebe as entradas do jogo. A quantidade de jogadores, as cartas de cada jogador
    e em qual jogada será feito o "duvido"
    '''
    n_jogadores = int(input())

    jogadores = {}
    for i in range(n_jogadores):
        lista = input().split(sep=", ")
        jogadores[i] = Monte(lista)

    duvido = int(input())

    return jogadores, duvido


def desafio(i, blefe, jogadores, pilha):
    '''
    Função criada para quando, no jogo, for pedido o 'duvido'
    '''
    #para sabermos se quem duvidou foi o primeiro jogador
    if i + 1 == len(jogadores):
        print('Jogador 1 duvidou.')
        # se o jogador anterior realmente blefou, ele pega toda a pilha de cartas
        if blefe:
            for j in range(len(pilha.cartas)):
                jogadores[i].cartas.append(pilha.cartas[j])
            pilha.cartas = []
        # caso contrário quem pega a pilha é o jogador que disse "duvido"
        else:
            for j in range(len(pilha.cartas)):
                jogadores[0].cartas.append(pilha.cartas[j])
            pilha.cartas = []

    else:
        print('Jogador {} duvidou.'.format(i+2))
        if blefe:
            for j in range(len(pilha.cartas)):
                jogadores[i].cartas.append(pilha.cartas[j])
            pilha.cartas = []
        else:
            for j in range(len(pilha.cartas)):
                jogadores[i+1].cartas.append(pilha.cartas[j])
            pilha.cartas = []


def main():
    # chama a função "entradas" para armazenar os inputs
    jogadores, duvido = entradas()
    pilha = Monte([])

    # transformamos as cartas em números para melhor ordenamento de força
    for i in range(len(jogadores)):
        jogadores[i].transformacao_letra_numero()

    # chamado no início do jogo
    situacao_jogo(jogadores)

    # inicio das jogadas
    n = 1  # n = 1 pois no início o Ás é a menor carta que pode ser jogada
    rodada = 0

    while True:
        for i in range(len(jogadores)):
            rodada += 1
            n, blefe = jogada(i, jogadores, pilha, n)
            if rodada == duvido:
                desafio(i, blefe, jogadores, pilha)
                situacao_jogo(jogadores)
                n = 1  # começamos a sequencia de força novamente
                rodada = 0
            if len(jogadores[i].cartas) == 0:
                print('Jogador {} é o vencedor!'.format(i+1))
                exit()


if __name__ == "__main__":
    main()
    