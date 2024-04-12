jogadores = int(input())
numeros = []
intervalo = []
pontos = []
p = 0
m = 0
f = True
maior_pontuacao = -1
ganhador = 0
time_1 = (jogadores + 1)//2

entrada_numeros = input().split()
entrada_intervalo = input().split()

for n in entrada_numeros:
    numeros.append(int(n))

for i in entrada_intervalo:
    intervalo.append(int(i))

while p < jogadores:
    if p < time_1:
        pontos.append(numeros[p]*(intervalo[p*2 + 1]-intervalo[p*2]))
    else:
        pontos.append(numeros[p]+(intervalo[p*2 + 1]-intervalo[p*2]))
    p += 1
    
while m < jogadores:
    if pontos[m] > maior_pontuacao:
        maior_pontuacao = pontos[m]
        ganhador = m + 1
    elif pontos[m] == maior_pontuacao:
        print("Rodada de cerveja para todos os jogadores!")
        f = False
    m += 1

if f == True:
    print("O jogador número {} vai receber o melhor bolo da cidade pois venceu com {} ponto(s)!".format(ganhador, maior_pontuacao))