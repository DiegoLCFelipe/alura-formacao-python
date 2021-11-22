# ------------------ Definição de Conjunto ---------------------- #

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

# O método cpy () faz uma cópia rasa de uma lista
assistiram = usuarios_data_science.copy()

# O método extend aciociona elmentos no final da lista
assistiram.extend(usuarios_machine_learning)

# O metodo set transforma uma lista em um conjunto.
# O conjunto é utilizado quando não queremos elementos repetidos e quando a ordem dos elementos não importa,
# já que não existe posição
assistiram = set(assistiram)
print(f'Criação de um conjunto a partir do conjunto {assistiram} \n'
      f'a partir das listas {usuarios_data_science} e {usuarios_machine_learning} \n')

# ------------------ Oprações com Conjuntos  ---------------------- #
# --------------------------- União ------------------------------- #
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

# Para união deve-se utilizar o operador | (ou)
assistiram = usuarios_data_science | usuarios_machine_learning
print(f'Conjuntos: \t {usuarios_data_science} \n  \t \t \t {usuarios_machine_learning} \n')
print(f'União: \t {assistiram} \n')

# ----------------------- Interseção ----------------------------- #
# Para interseção deve-se utiliza o operador & (e)
inter = usuarios_data_science & usuarios_machine_learning
print(f'Interseção:\t{inter} \n')

# ------------------------- Subtração ----------------------------- #
# Para subtração deve-se utiliza o operador - (menos)
sub = usuarios_data_science - usuarios_machine_learning
print(f'Está em conjunto mas não no outro:\t{sub} \n')

# ------------------------- ou exclusivo ----------------------------- #
# Para subtração deve-se utiliza o operador ^
excl = usuarios_data_science ^ usuarios_machine_learning
print(f'Exlui o que estão em ambos os conjuntos:\t{excl} \n')