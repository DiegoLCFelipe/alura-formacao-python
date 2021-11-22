# ------------------------------- Dicionário (Mapa, etc) --------------------------------- #
aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

print(aparicoes["Guilherme"])

# Outra forma de criar um dicionario

aparicoes = dict(
    Guilherme=1,
    cachorro=2,
    nome=2,
    vindo=1
)
# Adicionar elemento ao dicionario

aparicoes["Carlos"] = 2
print(aparicoes)

# Remover elemento ao dicionario
del aparicoes["Carlos"]
print(aparicoes)

# Verificar se o elemento pertence ao dicionario
print("Carlos" in aparicoes)

# Quando itermos sobre um dicionario, ele retorna as chaves
for elemento in aparicoes:
    print(elemento)

# É possível iterar apartir ddas chaves
for elemento in aparicoes.keys():
    print(elemento)

# Dos valores
for elemento in aparicoes.values():
    print(elemento)

# Ou de uma combinação entre eles
for elemento in aparicoes.items():
    print(elemento)

# Como o método items() retorna uma tupla, podemos descompactar
for chave, valor in aparicoes.items():
    print(chave, "=", valor)

# Também é possível concatenas palavras as chaves
contatena = ["palavra {}".format(chave) for chave in aparicoes.keys()]
print(contatena)