#--------------------------- Adicionando elementos no conjunto --------------------------- #
usuarios = {1, 5, 76, 34, 52, 13, 17}
print(f'Usuários: {usuarios} \n')
usuarios.add(765)
print(f'Usuárioa adicionando o elemento 765: \n'
      f'{usuarios}\n')

# ------------------------ Criação de conjuntos imutáveis ------------------------------- #
usuarios = frozenset(usuarios)
print(f'Conjunto imutável: \n'
      f'{usuarios}')