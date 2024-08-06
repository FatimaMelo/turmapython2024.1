class Funcionario:
    def __init__(self, matricula, nome, telefone, email, cpf, rg, cargo):
        self.matricula = matricula
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.rg = rg
        self.cargo = cargo

class Medico(Funcionario):
    def __init__(self, matricula, nome, telefone, email, cpf, rg, crm):
        super().__init__(matricula, nome, telefone, email, cpf, rg, 'Médico')
        self.crm = crm

    def horarios(self, mensagem):
        print(f'{self.nome} horários: {mensagem} / cargo: {self.cargo}')


class Enfermeiro(Funcionario):
    def __init__(self, matricula, nome, telefone, email, cpf, rg, coren):
        super().__init__(matricula, nome, telefone, email, cpf, rg, 'Enfermeiro')
        self.coren = coren


empresa = []

while True:
    tipo = input('Digite qual seu Cargo M = Médico(a), E = Enfermeiro(a) ou S para sair: ')

    if tipo == 'S':
        break

    matricula = input('Digite a matrícula: ')
    nome = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    cpf = input('Digite o CPF: ')
    rg = input('Digite o RG: ')

    if tipo == 'M':
        crm = input('Digite o CRM: ')
        funcionario = Medico(matricula, nome, telefone, email, cpf, rg, crm)
    elif tipo == 'E':
        coren = input('Digite o COREN: ')
        funcionario = Enfermeiro(matricula, nome, telefone, email, cpf, rg, coren)
    else:
        print('Tipo inválido. Por favor, digite M para Médico(a), E para Enfermeiro(a) ou S para sair.')

    empresa.append(funcionario)

print('Lista de Funcionários:')
for funcionario in empresa:
    print(funcionario.nome, '-', funcionario.cargo)
