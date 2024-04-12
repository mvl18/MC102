class Link:
    def __init__(self, nome, vida, dano, linha, coluna):
        '''
        Cria a classe Link. Que recebe nome como 'P' quando está
        vivo e 'X' quando morre. Vida e dano passado no input.
        Linha e coluna para sabermos sua posição no mapa. E o
        'chegou_ultima_linha' pois antes disso ele anda só para
        baixo no mapa.
        '''
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.linha = linha
        self.coluna = coluna
        self.chegou_ultima_linha = False

    def movimento(self, mapa):
        '''
        Movimenta link, sendo que no início ele desce para a última
        linha do mapa e após isso anda da direita para a esquerda
        em linhas pares e da esquerda para direita em linhas ímpares.
        '''
        mapa.matriz[self.linha][self.coluna].remove('P')
        if self.chegou_ultima_linha:
            if self.linha % 2 == 0:
                if self.coluna != 0:
                    self.coluna -= 1
                else:
                    self.linha -= 1

            else:
                if self.coluna + 1 != mapa.coluna:
                    self.coluna += 1
                else:
                    self.linha -= 1

        else:
            self.linha += 1
            if self.linha + 1 == mapa.linha:
                self.chegou_ultima_linha = True

    def muda_vida(self, alteracao):
        '''
        Muda a vida de link quando ele pega um objeto do tipo 'v'
        '''
        self.vida += alteracao

    def muda_dano(self, alteracao):
        '''
        Muda o dano de link quando ele pega um objeto do tipo 'd'
        '''
        self.dano += alteracao

    def sofre_dano(self, dano):
        '''
        Diminui a vida de link dependendo do ataque do monstro
        '''
        self.vida -= dano

    def esta_vivo(self):
        '''
        Analisa se link ainda está vivo, caso tenha vida > 0
        '''
        return self.vida > 0


class Monstro:
    def __init__(self, nome, vida, ataque, tipo, linha, coluna):
        '''
        Cria a classe Monstro. Nome do monstro é um inteiro que
        define qual monstro está no mapa. Vida e ataque passado
        no input. Tipo passa o tipo de movimento do monstro e o
        caractere que será impresso no mapa. Linha e coluna para
        sabermos sua posição no mapa.
        '''
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna

    def movimento(self, mapa):
        '''
        Se o tipo do monstro for 'U' o movimento do monstro é
        para cima no mapa. Se 'D' movimento para baixo. Se 'L'
        movimento para a esquerda. Se 'R' movimento para a direita.
        '''
        # retira o monstro antes de movimentá-lo, para não ficar repetido
        mapa.matriz[self.linha][self.coluna].remove(self.nome)

        if self.tipo == 'U' and self.linha != 0:
            self.linha -= 1
        elif self.tipo == 'D' and self.linha + 1 != mapa.linha:
            self.linha += 1
        elif self.tipo == 'L' and self.coluna != 0:
            self.coluna -= 1
        elif self.tipo == 'R' and self.coluna + 1 != mapa.coluna:
            self.coluna += 1
        else:
            return

    def sofre_dano(self, dano):
        '''
        Diminui vida do monstro dependendo do ataque de link
        '''
        self.vida -= dano

    def foi_derrotado(self):
        '''
        Analisa se o mostro ainda etá vivo
        '''
        return self.vida <= 0


class Objeto:
    def __init__(self, nome, tipo, linha, coluna, status):
        '''
        Cria a classe Objeto. Nome do objeto é um inteiro que
        define qual objeto está no mapa. Tipo passa o tipo 'v'
        ou 'd', caractere que será impresso no mapa. Linha e 
        coluna para sabermos sua posição no mapa. Status é um
        inteiro para sabermos o tanto que influenciará link.
        'foi_coletado' para saber se o item já foi coletado.
        '''
        self.nome = nome
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna
        self.status = status
        self.foi_coletado = False


class Mapa:
    def __init__(self, linha, coluna, saida_linha, saida_coluna):
        '''
        Cria a classe Mapa. Com linha e coluna para sabermos suas
        dimensões. Saida_linha e saida_coluna para sabermos a
        posição da saída. Matriz para sabermos a posição de cada
        objeto no mapa. 
        '''
        self.linha = linha
        self.coluna = coluna
        self.saida_linha = saida_linha
        self.saida_coluna = saida_coluna
        self.matriz = []

        # cria a matriz em que as entradas são listas vazias
        for i in range(self.linha):
            fila = []
            for j in range(self.coluna):
                fila.append([])
            self.matriz.append(fila)

        # insere a saída na matriz
        self.matriz[self.saida_linha][self.saida_coluna].append("*")

    def arrumar(self, link, monstros):
        '''
        Coloca link e os monstros nas posições corretas dentro da matriz
        '''
        self.matriz[link.linha][link.coluna].append(link.nome)
        for i in range(len(monstros)):
            self.matriz[monstros[i].linha][monstros[i].coluna].append(monstros[i].nome)

    def imprimir(self, link, monstros, objetos):
        '''
        Função para imprimir o mapa com link, os monstros e os objetos em
        suas posições atuais. Sendo que link tem prioridade sobre os monstros
        e os monstros prioridade sobre os itens. Sendo que o monstro que
        entrou por último no input tem prioridade para aparecer na casa.
        '''
        for i in range(self.linha):
            x = " "
            for j in range(self.coluna):
                impresso = False
                if j == self.coluna - 1:
                    x = ""

                if len(self.matriz[i][j]) != 0: 
                    # link tem prioridade máxima
                    if link.nome in self.matriz[i][j]:
                        print(link.nome, end=x)
                        impresso = True

                    elif '*' in self.matriz[i][j]:
                        print('*', end=x)
                        impresso = True

                    if not impresso:
                        for m in range(len(monstros)):
                            # para imprimir o tipo do último monstro seguindo a ordem de entrada, sabendo que ele ainda está vivo 
                            if len(monstros) - (m + 1) in self.matriz[i][j] and monstros[len(monstros) - (m + 1)].tipo != '.':
                                print(monstros[len(monstros) - (m + 1)].tipo, end=x)
                                impresso = True
                                break

                    if not impresso:
                        for o in range(len(objetos)):
                            if len(monstros) + len(objetos) - (o + 1) in self.matriz[i][j]:
                                print(objetos[len(objetos) - (o + 1)].tipo, end=x)
                                impresso = True
                                break
                    
                    # feito para imprimir um ponto caso a casa tenha apenas monstros mortos 
                    if not impresso:
                        print(".", end=x)
                        impresso = True

                # caso a posição do mapa esteja vazia, imprimimos um ponto
                else:
                    print(".", end=x)
            print()

    def interacao(self, link, monstros, objetos):
        '''
        Função feita para que link interaja com os objetos e
        com os monstros, alterando sua vida e seu dano dependendo
        dos parâmetros.
        '''
        # a interação de link sempre ocorre primeiro com os objetos
        for o in range(len(objetos)):
            #verifica se o objeto ainda não foi coletado
            if not objetos[o].foi_coletado:
                if len(monstros) + o in self.matriz[link.linha][link.coluna]:
                    if objetos[o].tipo == 'v':
                        link.muda_vida(objetos[o].status)
                    else:
                        link.muda_dano(objetos[o].status)

                    # imprimi o que ocorreu no jogo e transforma o objeto em um ponto no mapa, para indicar que já foi coletado
                    print("[{}]Personagem adquiriu o objeto {} com status de {}".format(objetos[o].tipo, objetos[o].nome, objetos[o].status))
                    objetos[o].tipo = '.'
                    objetos[o].foi_coletado = True

        for m in range(len(monstros)):
            if link.esta_vivo():
                if m in self.matriz[link.linha][link.coluna]:
                    vida_monstro = monstros[m].vida
                    vida_link = link.vida

                    # o dano mínimo que link dá é de 1
                    if link.dano > 1:
                        monstros[m].sofre_dano(link.dano)
                        ataque_link = link.dano  # "ataque_link" pega o dano real de link no monstro para passar na impressão, caso o monstro continue vivo
                    else:
                        monstros[m].sofre_dano(1)
                        ataque_link = 1

                    # sendo que link sempre ataca primeiro, se o monstro for derrotado imprimimos isso e o transformamos em um ponto
                    if monstros[m].foi_derrotado():
                        print("O Personagem deu {} de dano ao monstro na posicao ({}, {})".format(vida_monstro, link.linha, link.coluna))
                        monstros[m].tipo = '.'
                    
                    # se continua vivo o monstro ataca link, indicando a vida atual de link. Caso link seja derrotado, ele vira um X no mapa
                    else:
                        print("O Personagem deu {} de dano ao monstro na posicao ({}, {})".format(ataque_link, link.linha, link.coluna))
                        link.sofre_dano(monstros[m].ataque)
                        if link.esta_vivo():
                            print("O Monstro deu {} de dano ao Personagem. Vida restante = {}".format(monstros[m].ataque, link.vida))
                        else:
                            print("O Monstro deu {} de dano ao Personagem. Vida restante = 0".format(vida_link))
                            link.nome = 'X'
                            self.matriz[link.linha][link.coluna].remove('P')
                            self.matriz[link.linha][link.coluna].append(link.nome)


def entradas():
    vida_link, dano_link = input().split()
    linha_mapa, coluna_mapa = input().split()
    link_x, link_y = input().split(sep=",")
    saida_x, saida_y = input().split(sep=",")

    # recebemos os monstros, sabendo sua vida, ataque, tipo(U,D,L,R) e posição
    n_monstros = int(input())
    monstros = {}
    for i in range(n_monstros):
        vida, ataque, tipo, posicao = input().split()
        monstro_x, monstro_y = posicao.split(sep=",")
        monstros[i] = Monstro(i, int(vida), int(ataque), tipo, int(monstro_x), int(monstro_y))

    # recebemos os objetos, sabendo seu nome, tipo(v ou d), posição e seu status
    n_objetos = int(input())
    objetos = {}
    for i in range(n_objetos):
        nome, tipo, posicao, status = input().split()
        objeto_x, objeto_y = posicao.split(sep=",")
        objetos[i] = Objeto(nome, tipo, int(objeto_x), int(objeto_y), int(status))

    # Instanciamos link para receber a vida inicial e seu dano
    link = Link('P', int(vida_link), int(dano_link), int(link_x), int(link_y))
    # Instanciamos mapa para receber linha e coluna
    mapa = Mapa(int(linha_mapa), int(coluna_mapa), int(saida_x), int(saida_y))

    return link, mapa, objetos, monstros


def main():
    # chama a função "entradas" para armazenar os inputs 
    link, mapa, objetos, monstros = entradas()

    # armazena números no mapa que serão identificados, posteriormente, como sendo os objetos do jogo
    # para não confundir os identificadores dos objetos com o dos monstros, esses serão números acrescidos de "len(monstros)" 
    for j in range(len(objetos)):
        mapa.matriz[objetos[j].linha][objetos[j].coluna].append(len(monstros) + j)

    # colocamos link e os monstros no mapa, em suas posições iniciais
    mapa.arrumar(link, monstros)

    # imprimimos o mapa pela primeira vez com as posições iniciais de cada elemento do jogo
    mapa.imprimir(link, monstros, objetos)
    print()

    # começamos um loop de jogadas, em que só irá parar quando o jogo terminar. Casos em que link for derrotado, ou de link chegar na saída
    while (link.linha != mapa.saida_linha or link.coluna != mapa.saida_coluna):
        # movimentamos link e cada um dos monstros
        link.movimento(mapa)
        for i in range(len(monstros)):
            monstros[i].movimento(mapa)

        # colocamos no mapa as novas posições de link e dos monstros
        mapa.arrumar(link, monstros)

        # se a casa em que link está tiver algo além dele devemos investigar
        if len(mapa.matriz[link.linha][link.coluna]) != 1:

            # se link encontrar a saída ele sai imediatamente, mesmo que tenha monstros naquela casa
            if '*' in mapa.matriz[link.linha][link.coluna]:
                mapa.imprimir(link, monstros, objetos)
                print()
                print("Chegou ao fim!")
                exit()

            # se ainda não é a saída, link interage com os monstros ou com os objetos
            mapa.interacao(link, monstros, objetos)

        mapa.imprimir(link, monstros, objetos)
        print()

        # caso em que link foi derrotado, e o jogo acaba
        if not link.esta_vivo():
            exit()


if __name__ == "__main__":
    main()
