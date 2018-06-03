class Pessoa:
    def __init__(self,nome):
        self.nome = nome
class Inscricao:
    def __init__(self):
        self.valor = 0
class Encoinfo:
    def __init__(self):
        self.inscritos = []
        self.atendentes = []
    def emitir_relatorio(self):
        qtA = 0
        qtProfe = 0
        qtProfi = 0
        print('--> Quantidade de atendimentos por atendente <--')
        for i in self.atendentes:
            qtA += i.qt_aluno
            qtProfe += i.qt_professor
            qtProfi += i.qt_profissional
            print(i.nome,'-->',i.qt_aluno+i.qt_professor+i.qt_profissional\
            ,'Atendimentos\n',i.qt_aluno,'Alunos == ',i.qt_professor\
            ,'Professores == ',i.qt_profissional,'Profissionais')
        print('\n--> Valor total arrecadado para cada tipo de inscricao <--'\
        ,'\nAlunos -->',qtA*50.0,'R$','\nProfessores -->',qtProfe*80.0,'R$'\
        ,'\nProfissionais -->',qtProfi*120.0,'R$','\n--> Valor total arrecadado <--\n'\
        ,qtA*50.0+qtProfe*80.0+qtProfi*120.0,'R$')
class Inscrito:
    def __init__(self,pessoa,inscricao):
        self.pessoa = pessoa
        self.inscricao = inscricao
class Aluno(Inscricao):
    def __init__(self,universidade):
        super().__init__()
        self.valor = 50
        self.universidade = universidade
class Professor(Inscricao):
    def __init__(self,universidade):
        super().__init__()
        self.valor = 80
        self.universidade = universidade
class Profissional(Inscricao):
    def __init__(self,empresa):
        super().__init__()
        self.valor = 120
        self.empresa = empresa
class Atendente(Pessoa):
    def __init__(self,nome,encoinfo):
        super().__init__(nome)
        self.encoinfo = encoinfo
        self.qt_aluno = 0
        self.qt_professor = 0
        self.qt_profissional = 0
    def atender(self,pessoa,inscricao):
        if len(self.encoinfo.inscritos) < 50:
            self.encoinfo.inscritos.append(Inscrito(pessoa,inscricao))
            if (type(inscricao).__name__) == 'Aluno':
                self.qt_aluno += 1
            elif (type(inscricao).__name__) == 'Professor':
                self.qt_professor += 1
            else:
                self.qt_profissional += 1
        else:
            return print('Voce efetuou a quantidade maxima de inscricoes!!!\n')


import random

e = Encoinfo()
a = Atendente('Crisley1',e)
b = Atendente('Crisley2',e)
c = Atendente('Crisley3',e)
e.atendentes.append(a)
e.atendentes.append(b)
e.atendentes.append(c)
fila = random.randint(0,301)
for n in range(0,fila):
    aux = random.randint(1,3)
    aux2 = random.randint(1,3)
    universidade = ['ULBRA','CATOLICA','IFTO','UFT','UNITINS']
    empresa = ['SENAI','TELEMONT','MV','MINDS','IEL']
    p = Pessoa('Jose'+str(n))
    if aux == 1:
        if aux2 == 1:
            a.atender(p, Aluno(random.choice(universidade)))
        elif aux2 == 2:
            a.atender(p, Professor(random.choice(universidade)))
        else:
            a.atender(p, Profissional(random.choice(empresa)))
    elif aux == 2:
        if aux2 == 1:
            b.atender(p, Aluno(random.choice(universidade)))
        elif aux2 == 2:
            b.atender(p, Professor(random.choice(universidade)))
        else:
            b.atender(p, Profissional(random.choice(empresa)))
    else:
        if aux2 == 1:
            c.atender(p, Aluno(random.choice(universidade)))
        elif aux2 == 2:
            c.atender(p, Professor(random.choice(universidade)))
        else:
            c.atender(p, Profissional(random.choice(empresa)))
e.emitir_relatorio()

