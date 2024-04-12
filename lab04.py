dias = int(input())

for d in range(dias):
    nome_brigas = []
    brigas = 0
    procedimentos_desejados = []
    atendimento = False
    animais_atendidos = []
    animais_nao_atendidos = []
    indisponivel = []

    num_brigas = int(input())
    
    for i in range(num_brigas):
        dupla_da_briga = input().split()
        nome_brigas.append(dupla_da_briga)
        
    procedimentos_disponiveis = input().split()

    for i in range(len(procedimentos_disponiveis)):
        if i%2 != 0:
            procedimentos_disponiveis[i] = int(procedimentos_disponiveis[i])

    animais_dia = int(input())
    
    for i in range(animais_dia):
        nome_procedimento = input().split()

        for b in range(0, len(procedimentos_disponiveis), 2):
            if procedimentos_disponiveis[b] == nome_procedimento[1]:
                procedimentos_disponiveis[b+1] -= 1
                if procedimentos_disponiveis[b+1] >= 0:
                    animais_atendidos.append(nome_procedimento[0])
                else:
                    animais_nao_atendidos.append(nome_procedimento[0])
                atendimento = True

        if atendimento == False:
            indisponivel.append(nome_procedimento[0])
        
        atendimento = False

        procedimentos_desejados.append(nome_procedimento)

    
    for i in range(len(nome_brigas)):
        for j in range(len(procedimentos_desejados)):
            for k in range(len(procedimentos_desejados)):
                if (nome_brigas[i][0] == procedimentos_desejados[j][0]) and (nome_brigas[i][1] == procedimentos_desejados[k][0]):
                    brigas += 1

    
    print("Dia: {}".format(d+1))
    print("Brigas: {}".format(brigas))
    if len(animais_atendidos) != 0:
        print("Animais atendidos:", end = ' ')
        for i in range(len(animais_atendidos)):
            if i < (len(animais_atendidos) -1):
                print(animais_atendidos[i], end = ', ')
            else:
                print(animais_atendidos[i])
        
    if len(animais_nao_atendidos) != 0:
        print("Animais não atendidos:", end = ' ')
        for i in range(len(animais_nao_atendidos)):
            if i < (len(animais_nao_atendidos) - 1):
                print(animais_nao_atendidos[i], end = ', ')
            else:
                print(animais_nao_atendidos[i])

    if len(indisponivel) != 0:
        for i in range(len(indisponivel)):
            print("Animal {} solicitou procedimento não disponível.".format(indisponivel[i]))
    print()