class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas')

    def mostra_tarefas(self):
        print('Fez muita coisa ...')


class Caelum(Funcionario):
    def mostra_tarefas(self):
        print('fez muita coisa, Caelumer')

    def busca_curso_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando curso deste mês')


class Alura(Funcionario):
    def mostra_tarefas(self):
        print('Fez muita coisa, Alurance!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas no fórum')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno (Alura, Caelum, Hipster):
    pass

jose = Junior('José')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_curso_do_mes()

luan.mostra_tarefas()

print(luan)