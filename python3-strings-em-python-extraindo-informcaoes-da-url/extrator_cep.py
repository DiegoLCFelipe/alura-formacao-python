endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re # Regular expressions -- RegEX

# Cep : 5 digitos + hifen (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0-1}[0-9]{3}")
busca = padrao.search(endereco) # Match : Busca o padrão na string

if busca:
    cep = busca.group()  # retorna a string caso ela seja encontrada
    print(cep)


identificacao = "Rafaela Brasil, CPF: 718.457.190-85"
padrao = re.compile('[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}')

busca = padrao.search(identificacao)
if busca:
    cpf = busca.group()
    print(cpf)
