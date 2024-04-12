def soma_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Retorna a soma elemento a elemento dos dois vetores de entrada.
    Após terem sido igualados em tamanho pela função "iguala_tamanho".

    Argumentos:
        vetor1 (list[int]): lista de inteiros representando o primeiro vetor.
        vetor2 (list[int]): lista de inteiros representando o segundo vetor.

    Retorno:
        list[int]: lista resultante da soma dos elementos.
    """

    iguala_tamanho(vetor1, vetor2, 0)

    return [x + y for x, y in zip(vetor1, vetor2)]


def subtrai_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Retorna a diferença elemento a elemento dos dois vetores de entrada.

    Argumentos:
        vetor1 (list[int]): lista de inteiros representando o primeiro vetor.
        vetor2 (list[int]): lista de inteiros representando o segundo vetor.

    Retorno:
        list[int]: lista resultante da diferença dos elementos.
    """

    iguala_tamanho(vetor1, vetor2, 0)

    return [x - y for x, y in zip(vetor1, vetor2)]


def multiplica_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Retorna o produto elemento a elemento dos dois vetores de entrada.

    Argumentos:
        vetor1 (list[int]): lista de inteiros representando o primeiro vetor.
        vetor2 (list[int]): lista de inteiros representando o segundo vetor.

    Retorno:
        list[int]: lista resultante do produto dos elementos.
    """

    iguala_tamanho(vetor1, vetor2, 1)

    return [x * y for x, y in zip(vetor1, vetor2)]


def divide_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Retorna a divisão inteira dos elementos do primeiro vetor pelos
    elementos correspondentes do segundo vetor.

    Argumentos:
        vetor1 (list[int]): lista de inteiros representando o primeiro vetor.
        vetor2 (list[int]): lista de inteiros representando o segundo vetor.

    Retorno:
        list[int]: lista resultante da divisão dos elementos.
    """

    iguala_tamanho(vetor1, vetor2, 2)

    return [x // y for x, y in zip(vetor1, vetor2)]


def multiplicacao_escalar(vetor: list[int], escalar: int) -> list[int]:
    """Retorna o produto de um vetor elemento a elemento por um escalar.

    Argumentos:
        vetor (list[int]): lista de inteiros representando o vetor.
        escalar (int): inteiro representando o escalar.

    Retorno:
        list[int]: lista resultante do produto do vetor pelo escalar.
    """

    return [x * escalar for x in vetor]


def n_duplicacao(vetor: list[int], n: int) -> list[int]:
    """Duplica um vetor n vezes.

    Argumentos:
        vetor (list[int]): lista de inteiros representando o vetor.
        n (int): inteiro representando o número de duplicações.

    Retorno:
        list[int]: lista resultante com o vetor duplicado n vezes.
    """

    return vetor * n


def soma_elementos(vetor: list[int]) -> int:
    """Retorna a soma de todos os elementos do vetor.

    Argumentos:
        vetor (list[int]): lista de inteiros representando o vetor.

    Retorno:
        int: soma de todos os elementos do vetor.
    """

    soma = 0

    for elemento in vetor:
        soma += elemento

    return soma


def produto_interno(vetor1: list[int], vetor2: list[int]) -> int:
    """Retorna o produto interno entre dois vetores.

    Argumentos:
        vetor1 (list[int]): lista de inteiros representando o primeiro vetor.
        vetor2 (list[int]): lista de inteiros representando o segundo vetor.

    Retorno:
        int: produto interno entre os dois vetores.
    """

    iguala_tamanho(vetor1, vetor2, 1)

    return soma_elementos(multiplica_vetores(vetor1, vetor2))


def multiplica_todos(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Retorna uma lista resultante da multiplicação de cada elemento do
    primeiro vetor pelos elementos correspondentes do segundo vetor.

    Argumentos:
        vetor1 (list[int]): lista de inteiros representando o primeiro vetor.
        vetor2 (list[int]): lista de inteiros representando o segundo vetor.

    Retorno:
        list[int]: lista resultante da multiplicação de cada elemento do
        primeiro vetor pelos elementos correspondentes do segundo vetor.
    """

    if len(vetor1) == 0:
        return []
    elif len(vetor2) == 0:
        return [0] * len(vetor1)

    iguala_tamanho(vetor1, vetor2, 0)

    vetor_momentaneo = []

    for i in range(len(vetor1)):
        soma = 0
        for j in range(len(vetor2)):
            soma += vetor2[j] * vetor1[i]
        vetor_momentaneo.append(soma)

    if vetor_momentaneo[len(vetor_momentaneo)-1] == 0:
        vetor_momentaneo = vetor_momentaneo[:len(vetor_momentaneo)-1]

    return vetor_momentaneo


def correlacao_cruzada(vetor: list[int], mascara: list[int]) -> list[int]:
    """Retorna uma lista resultante da operação de correlação cruzada entre
    um vetor e uma máscara.

    Argumentos:
        vetor (list[int]): lista de inteiros representando o vetor.
        mascara (list[int]): lista de inteiros representando a máscara.

    Retorno:
        list[int]: lista resultante da operação de correlação cruzada
        entre o vetor e a máscara.
    """

    vetor_momentaneo = []

    for i in range(len(vetor) - len(mascara) + 1):
        soma = produto_interno(vetor[i:len(mascara)+i], mascara)
        vetor_momentaneo.append(soma)

    return vetor_momentaneo


def iguala_tamanho(vetor1: list[int], vetor2: list[int], p: int) -> None:
    """Iguala o tamanho dos dois vetores de entrada.

    Se os vetores possuem tamanhos diferentes, esta função adiciona elementos
    com 0 ou 1 ao vetor mais curto, para que ambos tenham o mesmo tamanho.

    Argumentos:
        vetor1 (list[int]): lista de inteiros representando o primeiro vetor.
        vetor2 (list[int]): lista de inteiros representando o segundo vetor.
        p (int): inteiro representando a operação que está sendo realizada.
            Se p = 0, a função está sendo chamada para igualar os vetores
            antes de uma soma ou subtração, adicionando 0.
            Se p = 1, a função está sendo chamada para igualar os vetores
            antes de uma multiplicação ou produto interno, adicionando 1.
            Se p = 2, a função está sendo chamada para igualar os vetores
            antes de uma divisão, 0 ao vetor do dividendo e 1 ao vetor do
            divisor, caso estes sejam os menores.

    Retorno:
        None
    """

    if p == 1 or p == 0:
        if len(vetor1) < len(vetor2):
            for i in range(len(vetor2) - len(vetor1)):
                vetor1.append(p)
        elif len(vetor1) > len(vetor2):
            for i in range(len(vetor1) - len(vetor2)):
                vetor2.append(p)
        else:
            return None

    elif p == 2:
        if len(vetor1) < len(vetor2):
            for i in range(len(vetor2) - len(vetor1)):
                vetor1.append(0)
        elif len(vetor1) > len(vetor2):
            for i in range(len(vetor1) - len(vetor2)):
                vetor2.append(1)
        else:
            return None


def main() -> None:
    """Função principal do programa.

    Solicita que o usuário informe duas listas de números inteiros
    e uma operação a ser realizada.
    Em seguida, chama a função correspondente à operação informada
    e exibe o resultado.

    Argumentos:
        None

    Retorno:
        None
    """

    vetor_corrente = list(map(int, input().split(sep=',')))

    while True:
        comando = input()

        if comando == 'soma_vetores':
            vetor_operacao = list(map(int, input().split(sep=',')))
            vetor_corrente = soma_vetores(vetor_corrente, vetor_operacao)
            print(vetor_corrente)

        elif comando == 'subtrai_vetores':
            vetor_operacao = list(map(int, input().split(sep=',')))
            vetor_corrente = subtrai_vetores(vetor_corrente, vetor_operacao)
            print(vetor_corrente)

        elif comando == 'multiplica_vetores':
            vetor_operacao = list(map(int, input().split(sep=',')))
            vetor_corrente = multiplica_vetores(vetor_corrente, vetor_operacao)
            print(vetor_corrente)

        elif comando == 'divide_vetores':
            vetor_operacao = list(map(int, input().split(sep=',')))
            vetor_corrente = divide_vetores(vetor_corrente, vetor_operacao)
            print(vetor_corrente)

        elif comando == 'multiplicacao_escalar':
            escalar = int(input())
            vetor_corrente = multiplicacao_escalar(vetor_corrente, escalar)
            print(vetor_corrente)

        elif comando == 'n_duplicacao':
            n = int(input())
            vetor_corrente = n_duplicacao(vetor_corrente, n)
            print(vetor_corrente)

        elif comando == 'soma_elementos':
            vetor_corrente = [soma_elementos(vetor_corrente)]
            print(vetor_corrente)

        elif comando == 'produto_interno':
            vetor_operacao = list(map(int, input().split(sep=',')))
            vetor_corrente = [produto_interno(vetor_corrente, vetor_operacao)]
            print(vetor_corrente)

        elif comando == 'multiplica_todos':
            vetor_operacao = list(map(int, input().split(sep=',')))
            vetor_corrente = multiplica_todos(vetor_corrente, vetor_operacao)
            print(vetor_corrente)

        elif comando == 'correlacao_cruzada':
            vetor_operacao = list(map(int, input().split(sep=',')))
            vetor_corrente = correlacao_cruzada(vetor_corrente, vetor_operacao)
            print(vetor_corrente)

        elif comando == 'fim':
            exit()


if __name__ == "__main__":
    main()
