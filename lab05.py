# Função que inverte a ordem dos elementos do genoma entre os índices i e j (inclusivos)
def reverter(i, j):
    global genoma

    if i > len(genoma) - 1:
        return None          # Se i está fora dos limites do genoma, retorna sem fazer nada
    elif j > len(genoma) - 1:
        j = len(genoma) - 1  # Se j está fora dos limites do genoma, define j como o último índice

    # Inverte os elementos do genoma entre os índices i e j
    while i < j:
        operador = genoma[i]
        genoma[i] = genoma[j]
        genoma[j] = operador
        i += 1
        j -= 1

# Função que transpõe a ordem dos elementos do genoma entre os índices i e j (inclusivos) e os insere na posição k
def transpor(i, j, k):
    global genoma

    if i > len(genoma) - 1:
        return None           # Se i está fora dos limites do genoma, retorna sem fazer nada
    elif j > len(genoma) - 1:
        return None           # Se j está fora dos limites do genoma, retorna sem fazer nada
    elif k > len(genoma) - 1:
        k = len(genoma) - 1   # Se k está fora dos limites do genoma, define k como o último índice

    # Transpõe os elementos do genoma entre os índices i e j e os insere na posição k
    genoma = genoma[:i] + genoma[(j+1):(k+1)] + genoma[i:(j+1)] + genoma[(k+1):]

# Função que insere o genoma g na posição i dentro do genoma original
def combinar(g, i):
    global genoma
    inserir = list(g)
    genoma = genoma[:i] + inserir + genoma[i:]

# Função que adiciona o genoma g no final do genoma original
def concatenar(g):
    global genoma
    genoma.extend(g)

# Função que remove os elementos do genoma entre os índices i e j (inclusivos)
def remover(i, j):
    global genoma

    if i > len(genoma) - 1:
        return None    
    elif j > len(genoma) - 1:
        j = len(genoma) - 1
    
    genoma = genoma[:i] + genoma[(j+1):]

# Função que transpõe a ordem dos elementos do genoma entre os índices i e j (inclusivos) e inverte a ordem dos elementos entre os índices i e k (inclusivos)
def transpor_e_reverter(i, j, k):
    transpor(i, j, k)
    reverter(i, k)

# Função que conta o número de ocorrências do genoma g no genoma original, desconsiderando sub-ocorrências
def buscar(g):
    # O genoma original é transformado em uma palavra com (.join) para depois ser comparado com o genoma g com (.count)    
    buscador = ''.join(genoma).count(g)
    
    return buscador

# Função que conta o número de ocorrências do genoma g no genoma original em ambos sentidos
def buscar_bidirecional(g):
    buscador_1 = buscar(g)
    reverter(0, len(genoma))
    buscador_2 = buscar(g)
    reverter(0, len(genoma))

    print(buscador_1 + buscador_2)

# Função para mostrar o genoma na tela
def mostrar():
    for i in range(len(genoma)):
        print(genoma[i], end ='')
    
    print()

# Função para encerrar o programa
def sair():
    exit()

# Inicializa a variável operador com 0 e lê o genoma do usuário
operador = 0
genoma = list(input())

# Loop infinito para receber comandos do usuário e executá-los
while True:
    comando = input().split()   
     
    if comando[0] == 'reverter':
        reverter(int(comando[1]), int(comando[2]))

    elif comando[0] == 'transpor':
        transpor(int(comando[1]), int(comando[2]), int(comando[3]))

    elif comando[0] == 'combinar':
        combinar(comando[1], int(comando[2]))    

    elif comando[0] == 'concatenar':
        concatenar(comando[1])  

    elif comando[0] == 'remover':
        remover(int(comando[1]), int(comando[2])) 

    elif comando[0] == 'transpor_e_reverter':
        transpor_e_reverter(int(comando[1]), int(comando[2]), int(comando[3])) 

    elif comando[0] == 'buscar':
        print(buscar(comando[1]))

    elif comando[0] == 'buscar_bidirecional':
        buscar_bidirecional(comando[1])

    elif comando[0] == 'mostrar':
        mostrar()
    
    elif comando[0] == 'sair':
        sair()