class Aloy:
    def __init__(self, vida, flechas):
        '''
        Cria a classe Aloy, que é a personagem principal.
        Ela recebe a sua vida como um número inteiro e suas
        flechas como um dicionário, sendo a chave do dicionário
        o tipo de flecha. "vida_total" e flechas_inicial" feitas
        para não serem alteradas e servirem de comparação durante
        a aventura.
        '''
        self.vida = vida
        self.flechas = flechas
        self.vida_total = int(vida)
        self.flechas_inicial = flechas.copy()

    def recupera_vida(self):
        '''
        Função para curar a vida de Aloy no final de cada combate,
        recebendo metade da vida total do inicio do jogo sem
        ultrapassar o limite de vida inicial.
        '''
        self.vida += self.vida_total // 2
        if self.vida > self.vida_total:
            self.vida = int(self.vida_total)

    def recupera_flecha(self):
        '''
        Função para que Aloy recupere todas as suas flechas no
        final de cada combate.
        '''
        self.flechas = self.flechas_inicial.copy()

    def perde_vida(self, dano):
        '''
        Caso Aloy não consiga com três flechadas derrotar
        todas as máquinas daquele combate, ela irá tomar
        dano das máquinas que ainda estão vivas.
        '''
        self.vida -= dano

    def n_flechas(self):
        '''
        Função para contar o número de flechas que Aloy
        possui durante cada combate
        '''
        return sum(self.flechas.values())


class Maquina:
    def __init__(self, vida, ataque, partes):
        '''
        Cria a classe Maquina que são os inimigos de
        Aloy. Eles possuem sua vida, que é um inteiro;
        seu ataque, que é um inteiro; e um dicionário
        de suas partes, sendo a chave o nome do componente
        e os parâmetros referentes a fraqueza de cada
        componente,
        '''
        self.vida = vida
        self.ataque = ataque
        self.partes = partes

    def dano_forte(self, componente, f_x, f_y):
        '''
        Função para o dano forte, que acontece quando a
        flecha atirada é condizente com a fraqueza do componente
        da máquina.
        '''
        dano = (self.partes[componente][1] - (abs(self.partes[componente][2] - f_x) + abs(self.partes[componente][3] - f_y)))
        if dano > 0:
            self.vida -= dano

    def dano_fraco(self, componente, f_x, f_y):
        '''
        Função para dano fraco, quando a flecha não
        condiz com a fraqueza do componente.
        '''
        dano = (self.partes[componente][1] - (abs(self.partes[componente][2] - f_x) + abs(self.partes[componente][3] - f_y))) // 2
        if dano > 0:
            self.vida -= dano

    def foi_derrotada(self):
        '''
        Função para saber se uma máquina já foi derrotada.
        '''
        return self.vida <= 0


def vida_aloy():
    '''
    Recebe os pontos de vida máximos de Aloy
    '''
    return int(input())


def flechas_aloy():
    '''
    Recebe os tipos de tipo_flecha de Aloy e a quantidade de cada uma e passa para um dicionário
    '''
    lista_flechas = input().split()
    dicionario_flechas = {}

    for i in range(0, len(lista_flechas), 2):
        dicionario_flechas[lista_flechas[i]] = int(lista_flechas[i+1])

    return dicionario_flechas


def verifica_critico(c_x, c_y, f_x, f_y):
    '''
    Verifica se tivemos um dano crítico.
    '''
    return c_x == f_x and c_y == f_y


def situacao_critico(critico, n_maquinas_combate_inicio):
    '''
    Imprime os danos críticos em cada máquina, passando
    a coordenada do dano e quantas vezes o ponto foi
    acertado.
    '''
    print("Críticos acertados:")
    for i in range(n_maquinas_combate_inicio):
        coordenadas = list(critico[i].keys())
        quantidade_ataques = list(critico[i].values())
        titulo = 0
        for j in range(len(coordenadas)):
            if quantidade_ataques[j] != 0:
                titulo += 1
                if titulo == 1:
                    print("Máquina {}:".format(i))
                print("- {}: {}x".format(coordenadas[j], quantidade_ataques[j]))


def situacao_inicial_combate(n_combate, vida_inicio_combate):
    '''
    Imprime o numero do combate e a vida de Aloy no inicio do combate
    '''
    print("Combate {}, vida = {}".format(n_combate, vida_inicio_combate))


def situacao_maquinas_derrotadas(alvo):
    '''
    Imprime quais máquinas foram derrotadas ao final do combate
    '''
    print("Máquina {} derrotada".format(alvo))


def situacao_vida(aloy):
    '''
    Imprime a vida de Aloy após o combate
    '''
    if aloy.vida <= 0:
        print("Vida após o combate = 0")
    else:
        print("Vida após o combate = {}".format(aloy.vida))


def situacao_flechas(aloy):
    '''
    Imprime o tipo de flecha e a quantidade utilizada em cada combate
    '''
    print("Flechas utilizadas:")
    lista = list(aloy.flechas.keys())
    for tipo in lista:
        if aloy.flechas[tipo] != aloy.flechas_inicial[tipo]:
            print("- {}: {}/{}".format(tipo, aloy.flechas_inicial[tipo] - aloy.flechas[tipo], aloy.flechas_inicial[tipo]))


def repeticao(aloy, maquinas_combate, f_x, f_y, teve_critico, maquinas_derrotadas, critico, alvo, componente, tipo_flecha):
    '''
    Função feita para evitar repetição na main(). Tem o objetivo
    de chamar a função para ver se a flechada de Aloy teve dano
    crítico e caso tiver isso será salvo no dicionário "crítico".
    Esta função também chama a função para verificar se a máquina
    foi derrotada com a flechada, e caso positivo salva na variável
    "maquinas_derrotadas".
    Além de subtrair a flecha de Aloy do tipo utilizado.
    '''
    if verifica_critico(maquinas_combate[alvo].partes[componente][2], maquinas_combate[alvo].partes[componente][3], f_x, f_y):
        teve_critico += 1  # confirma se esse combate teve ataque crítico para futura impressão
        tupla = (f_x, f_y)
        critico[alvo][tupla] += 1
    if maquinas_combate[int(alvo)].foi_derrotada():  # verifica se a máquina já foi derrotada e adiciona seu numero na lista "maquinas derrotadas"
        maquinas_derrotadas += 1
        situacao_maquinas_derrotadas(alvo)
    aloy.flechas[tipo_flecha] -= 1

    return teve_critico, maquinas_derrotadas


def main():
    # Instanciamos aloy para receber a vida inicial e a quantidade de flechas com seu tipo
    aloy = Aloy(vida_aloy(), flechas_aloy())  

    n_maquinas_total = int(input())  # quantidade de máquinas que devem ser derrotadas para que Aloy volte para a tribo
    n_combate = -1  # variável para calcular quantos combates será preciso para que Aloy termine a batalha

    while n_maquinas_total > 0:  # loop para iniciar um novo combate com um novo número de máquinas
        n_combate += 1
        n_maquinas_combate = int(input())  # quantidade de máquinas que vão lutar com Aloy naquele combate
        maquinas_combate = {}  # dicionário que armazena as informações de cada máquina

        critico = {}  # dicionário para receber os danos críticos sendo a chave o nome da máquina

        for i in range(n_maquinas_combate):
            vida, ataque, n_partes = list(map(int, input().split()))

            critico[i] = {}  # cria um dicionário dentro de outro, para receber as coordenadas e a quantidade de veze que foi acertada
            partes = {}  # dicionário que armazena cada nome de componente da máquina como chave e seus respectivos atributos
            for _ in range(n_partes):
                componente, fraqueza, dano_maximo, c_x, c_y = input().split(sep =", ")
                partes[componente] = [fraqueza, int(dano_maximo), int(c_x), int(c_y)]
                critico[i][(int(c_x), int(c_y))] = 0

            maquinas_combate[i] = Maquina(vida, ataque, partes)

        vida_inicio_combate = aloy.vida
        situacao_inicial_combate(n_combate, vida_inicio_combate)
        n_maquinas_combate_inicio = n_maquinas_combate

        teve_critico = 0

        while n_maquinas_combate != 0:  # verifica se Aloy já derrotou todas as maquinas daquele combate

            maquinas_derrotadas = 0

            # Enquanto todos as maquinas não forem derrotadas, recebe as três flechadas seguidas se Aloy enquanto for preciso
            for flechadas in range(3):
                if aloy.n_flechas() > 0:
                    alvo, componente, tipo_flecha, f_x, f_y = input().split(sep =", ")
                    if tipo_flecha == maquinas_combate[int(alvo)].partes[componente][0] or maquinas_combate[int(alvo)].partes[componente][0] == "todas":
                        maquinas_combate[int(alvo)].dano_forte(componente, int(f_x), int(f_y)) # da o dano na máquina
                        teve_critico, maquinas_derrotadas = repeticao(aloy, maquinas_combate, int(f_x), int(f_y), teve_critico, maquinas_derrotadas, critico, int(alvo), componente, tipo_flecha)

                    else:
                        maquinas_combate[int(alvo)].dano_fraco(componente, int(f_x), int(f_y))
                        teve_critico, maquinas_derrotadas = repeticao(aloy, maquinas_combate, int(f_x), int(f_y), teve_critico, maquinas_derrotadas, critico, int(alvo), componente, tipo_flecha)

                    # caso todas as máquinas forem derrotadas, imprimo a situação, aloy recupera vida e as flechas e parte para encontrar mais maquinas
                    if maquinas_derrotadas == n_maquinas_combate:
                        n_maquinas_total -= n_maquinas_combate_inicio
                        n_maquinas_combate -= maquinas_derrotadas
                        situacao_vida(aloy)
                        situacao_flechas(aloy)
                        if teve_critico != 0:
                            situacao_critico(critico, n_maquinas_combate_inicio)
                        aloy.recupera_vida()
                        aloy.recupera_flecha()

                        break

                    # caso já tenha atirado as três flechas e ainda não derrotou todos, perde vida e continua lutando com as maquinas do combate
                    elif maquinas_derrotadas != n_maquinas_combate and flechadas == 2:
                        n_maquinas_combate -= maquinas_derrotadas
                        dano = 0
                        for i in range(n_maquinas_combate_inicio):
                            if not maquinas_combate[i].foi_derrotada():  # verifica se a máquina realmente ainda está viva para poder atacar Aloy
                                dano += maquinas_combate[i].ataque

                        aloy.perde_vida(dano)

                        if aloy.vida <= 0:
                            situacao_vida(aloy)
                            print("Aloy foi derrotada em combate e não retornará a tribo.")
                            return

                else:
                    situacao_vida(aloy)
                    print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")
                    return

    print("Aloy provou seu valor e voltou para sua tribo.")  # ocorre quando saímos do loop "while n_maquinas_total > 0", o que indica que todas as maquinas foram derrotadas
    return


if __name__ == "__main__":
    main()
