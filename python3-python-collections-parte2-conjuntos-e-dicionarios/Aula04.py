# Contagem de ocorrências de palavras
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho meu cachorro e gosto muito de cachorros"
print(f'Texto original: {meu_texto} \n')

meu_texto = meu_texto.lower()
print(f'Texto em caixa baixa: {meu_texto} \n')

## Método 1: Utilizando o método get()
aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0 )
    aparicoes[palavra] = ate_agora + 1

print(f'{aparicoes} \n')

## Metodo 2: Utilizando um dicionário padrão
### Obs: int() retorna 0
from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1

print(f'{aparicoes} \n')

### Simplificando código
for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(f'{aparicoes} \n')

# Mais aplicações do default dict
class Conta:
    def __init__(self):
        print("Criando uma conta \n")

contas = defaultdict(Conta)
contas[15]

# Utilizando um conatdor
from collections import Counter

aparicoes = Counter(meu_texto.split())
print(aparicoes)
