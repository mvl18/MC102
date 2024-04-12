def descriptografia(linha: list[str], senha: int) -> list[None]:
    """Função que realiza a descriptografia de uma linha criptografada.

    Argumentos:
        linha (list[str]): Lista de caracteres da linha criptografada.
        senha (int): Valor numérico usado para descriptografar a linha.

    Retorno:
        list[None]: Lista de caracteres da linha descriptografada.
    """
    lista_intermediaria = []
    lista_intermediaria_2 = []
    lista_pronta = []

    for i in range(len(linha)):
        decimal = ord(linha[i]) + senha
        if decimal >= 127:
            while decimal >= 127:
                decimal = decimal - 95
        elif decimal < 32:
            while decimal < 32:
                decimal = decimal + 95
        lista_intermediaria.append(decimal)

    for j in range(len(linha)):
        lista_intermediaria_2.append(chr(lista_intermediaria[j]))

    lista_pronta = ''.join(lista_intermediaria_2)

    return lista_pronta


def chave(linha: list[str], sinal: str, operador_1: str, operador_2: str) -> int:
    """Função que calcula a senha a partir da linha criptografada e dos operadores.

    Argumentos:
        linha (list[str]): Lista de caracteres da linha criptografada.
        sinal (str): Sinal matemático para calcular a senha.
        operador_1 (str): Tipo de caractere usado como operando 1.
        operador_2 (str): Tipo de caractere usado como operando 2.

    Retorno:
        int: Valor da senha calculada.
    """
    vogal = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    numero = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    consoante = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'w', 'y', 'z'
                 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'W', 'Y', 'Z')
    andador = 0
    chave_1 = 0
    chave_2 = 0

    if operador_1 == 'vogal':
        operador_1 = vogal
    if operador_1 == 'numero':
        operador_1 = numero
    if operador_1 == 'consoante':
        operador_1 = consoante

    if operador_2 == 'vogal':
        operador_2 = vogal
    if operador_2 == 'numero':
        operador_2 = numero
    if operador_2 == 'consoante':
        operador_2 = consoante

    for i in range(len(linha)):
        if linha[i] in operador_1:
            chave_1 = i
            andador = i
            break

    while andador < len(linha):
        if linha[andador] in operador_2:
            chave_2 = andador
            break
        else:
            andador += 1

    if sinal == '+':
        resultado = chave_1 + chave_2
    elif sinal == '-':
        resultado = chave_1 - chave_2
    elif sinal == '*':
        resultado = chave_1 * chave_2
    elif sinal == '/':
        resultado = chave_1 / chave_2
    else:
        resultado = None

    return (resultado)


def main() -> None:
    """Função principal responsável por realizar a interação com o usuário,
    ler os valores de entrada e chamar as funções `chave` e `descriptografia`
    para calcular a senha e descriptografar a linha criptografada, respectivamente.

    Argumentos:
        Nenhum.

    Retorno:
        None.
    """
    operador = input()
    operador_1 = input()
    operador_2 = input()
    n_linhas = int(input())
    linha_criptografada = list(input())
    tamanhos = [0, len(linha_criptografada)]

    for i in range(n_linhas-1):
        linha_auxiliar = list(input())
        linha_criptografada += linha_auxiliar
        tamanhos.append(len(linha_criptografada))

    senha = chave(linha_criptografada, operador, operador_1, operador_2)
    print(senha)

    for j in range(n_linhas):
        linha_descriptografada = descriptografia(linha_criptografada[tamanhos[j]:tamanhos[j+1]], senha)
        print(linha_descriptografada)


if __name__ == "__main__":
    main()
