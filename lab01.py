# Se Sheila ganha verão Interestelar, caso contrário será Jornada nas Estrelas.
sheila = str(input())
reginaldo = str(input())

if (sheila == reginaldo):
    print("empate")
else:
    if( (sheila == "tesoura" and ((reginaldo == "papel")   or (reginaldo == "lagarto"))) or
        (sheila == "pedra"   and ((reginaldo == "lagarto") or (reginaldo == "tesoura"))) or
        (sheila == "papel"   and ((reginaldo == "pedra")   or (reginaldo == "spock")))   or
        (sheila == "spock"   and ((reginaldo == "tesoura") or (reginaldo == "pedra")))   or
        (sheila == "lagarto" and ((reginaldo == "spock")   or (reginaldo == "papel")))     ):
        print("Interestelar")
    else:
        print("Jornada nas Estrelas")