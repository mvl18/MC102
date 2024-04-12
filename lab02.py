desafio = "Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições:"
motiva = "Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são:"
aprenda =  "Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são:"
erro = "Opção inválida, recomece o questionário."

print("Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.")
first = int(input("Seu SO anterior era Linux?\n(0) Não\n(1) Sim\n"))

if(first == 0):
    second = int(input("Seu SO anterior era um MacOS?\n(0) Não\n(1) Sim\n"))

    if(second == 0):
        print("{} Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro.".format(motiva))
    elif(second == 1):
         print("{} ElementaryOS, ApricityOS.".format(motiva))
    else:print(erro)
        
elif(first == 1):
    second = int(input("É programador/ desenvolvedor ou de áreas semelhantes?\n(0) Não\n(1) Sim\n(2) Sim, realizo testes e invasão de sistemas\n"))
    
    if(second == 0):        
        print("{} Ubuntu Mint, Fedora.".format(aprenda))
    elif(second == 2):
        print("{} Kali Linux, Black Arch.".format(aprenda))
    elif(second == 1):
        third = int(input("Gostaria de algo pronto para uso ao invés de ficar configurando o SO?\n(0) Não\n(1) Sim\n"))
        
        if(third == 0):
            fourth = int(input("Já utilizou Arch Linux?\n(0) Não\n(1) Sim\n"))

            if(fourth == 0):
                print("{} Antergos, Arch Linux.".format(aprenda))
            elif(fourth == 1):
                print("{} Gentoo, CentOS, Slackware.".format(desafio))
            else:print(erro)

        elif(third == 1):
            fourth = int(input("Já utilizou Debian ou Ubuntu?\n(0) Não\n(1) Sim\n"))

            if(fourth == 0):
                print("{} OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu.".format(aprenda))
            elif(fourth == 1):
                print("{} Manjaro, ApricityOS.".format(desafio))
            else:print(erro)
        else:print(erro)

    else:print(erro)
    
else:print(erro)