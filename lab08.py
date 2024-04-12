# Recebe os Inputs
n_filmes = int(input())
filmes_participantes = []
for _ in range(n_filmes):
    filmes_participantes.append(input())

n_avaliadores = int(input())
votos = {}
filmes_avaliados = []

for _ in range(n_avaliadores):
    avaliador, categoria, filme, nota = input().split(", ")
    nota = float(nota)
    filmes_avaliados.append(filme)

    if categoria in votos:
        if filme in votos[categoria]:
            votos[categoria][filme]["nota_total"] += nota
            votos[categoria][filme]["quantidade_votos"] += 1
        else:
            votos[categoria][filme] = {"nota_total": nota, "quantidade_votos": 1}
    else:
        votos[categoria] = {filme: {"nota_total": nota, "quantidade_votos": 1}}

# Calcular a média dos filmes em cada categoria
for categoria in votos:
    for filme in votos[categoria]:
        nota_total = votos[categoria][filme]["nota_total"]
        quantidade_votos = votos[categoria][filme]["quantidade_votos"]
        votos[categoria][filme]["média"] = nota_total / quantidade_votos

# Encontrar o filme com a maior média em cada categoria
resultados = []

for categoria in votos:
    i = 0

    for filme in votos[categoria]:
        if votos[categoria][filme]["média"] > i:
            i = votos[categoria][filme]["média"]
            ganhador = filme
            pontuacao = i
        elif votos[categoria][filme]["média"] == i:
            if votos[categoria][filme]["quantidade_votos"] > votos[categoria][ganhador]["quantidade_votos"]:
                ganhador = filme

    resultados.extend((categoria, ganhador, pontuacao))


# Encontrar vencedor da categoria "Pior filme do ano"
freq_max = 0
desempate_max = 0

for elemento in filmes_participantes:
    freq = 0
    desempate = 0

    for i in range(1, len(resultados), 3):
        if elemento == resultados[i]:
            freq += 1
            desempate += resultados[i+1]

    if freq > freq_max:
        pior_filme = elemento
        freq_max = freq
        desempate_max = desempate
    elif freq == freq_max and desempate > desempate_max:
        pior_filme = elemento
        desempate_max = desempate

# Encontrar vencedores da categoria "Não merecia estar aqui"
nao_merecia = []

for elemento in filmes_participantes:
    if elemento not in filmes_avaliados:
        nao_merecia.append(elemento)
if len(nao_merecia) == 0:
    nao_merecia.append("sem ganhadores")

# Resultado
print("#### abacaxi de ouro ####")
print()
print("categorias simples")
print("categoria: filme que causou mais bocejos")
print("- " + resultados[resultados.index("filme que causou mais bocejos") + 1])
print("categoria: filme que foi mais pausado")
print("- " + resultados[resultados.index("filme que foi mais pausado") + 1])
print("categoria: filme que mais revirou olhos")
print("- " + resultados[resultados.index("filme que mais revirou olhos") + 1])
print("categoria: filme que não gerou discussão nas redes sociais")
print("- " + resultados[resultados.index("filme que não gerou discussão nas redes sociais") + 1])
print("categoria: enredo mais sem noção")
print("- " + resultados[resultados.index("enredo mais sem noção") + 1])
print()
print("categorias especiais")
print("prêmio pior filme do ano")
print("- " + pior_filme)
print("prêmio não merecia estar aqui")
print("- " + ', '.join(nao_merecia))
