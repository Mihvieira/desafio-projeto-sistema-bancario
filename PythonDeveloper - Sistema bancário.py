#Programa bancário - versão 3 - classes
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereço):
        self.endereço = endereço
        self.contas = []
    
    def realizar_trasação(self, conta, transação):
        transação.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFísica:
    def __init__(self, cpf, nome, data_nascimento, endereço):
        super().__init__(endereço)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        
class Conta:
    def __init__ (self, número, cliente):
        self._saldo = 0
        self._número = número
        self._agência = '0001'
        self._cliente = cliente
        self._histórico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, número):
        return cls(número, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def número(self):
        return self._número
    
    @property
    def agência(self):
        return self._agência
    
    @property
    def histórico(self):
        return self._histórico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('\nOperação falhou! Você não tem saldo suficiente.')
        elif valor > 0:
            self.valor -=valor
            print('\n ### Saque realizado com sucesso! ###')
            return True
        else: 
            print('Operação falhou! O valor informado é inválido.')
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\n Depósito realizado com Sucesso!')
        else:
            print('\n Operação Falhou! O valor depositado é inválido')
            return False
        return True

class ContaCorrente:
    def __init__ (self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques: limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transação for transação in self.histórico.
             transações if transação['tipo'] == Saque.__name__])
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques

        if excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite.')
        
        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido')
        
        else: 
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f'''\
            Agência: \t{self.agência}
            c/c: \t\t{self.número}
            Titular:\t{self.cliente.nome}
        '''

class Historico:
    def __init__ (self):
        self._trasação = []
        
    @property
    def transações(self):
        return self._transações
    def adicionar_transação(self, transação):
        self._trasações.append("{'tipo': transação.__class__.__name__,'valor': transação.valor 'data': datetime.now().strftime('%d-%m-%Y %H:%M%s')}")


class Transação(ABC):
    @property
    @abstractproperty
    def valor (self):
        pass
    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transação):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        sucesso_transação = conta.sacar(self.valor)
        if sucesso_transação:
            conta.histórico.adicionar_transação(self)

class Depósito(Transação):
    def __init__ (self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transação = conta.depositar(self.valor)
        if sucesso_transação:
            conta.histórico.adicionar_transação(self)
    

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('Cliente não possui conta!')
        return

    return cliente.contas[0]

def depositar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return

    valor = float(input('Informe o valor do depósito: '))
    transacao = Depósito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return

    valor = float(input('Informe o valor do saque: '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

    
def exibir_extrato(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print('\n================ EXTRATO ================')
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
    print('==========================================')


def criar_cliente(clientes):
    cpf = input('Informe o CPF (somente número): ')
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('Já existe cliente com esse CPF!')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereço = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    cliente = PessoaFísica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereço=endereço)

    clientes.append(cliente)

    print('Cliente criado com sucesso!')


def criar_conta(numero_conta, clientes, contas):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado, fluxo de criação de conta encerrado!')
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print('Conta criada com sucesso!')


def listar_contas(contas):
    for conta in contas:
        print('=' * 100)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            depositar(clientes)

        elif opcao == 's':
            sacar(clientes)

        elif opcao == 'e':
            exibir_extrato(clientes)

        elif opcao == 'nu':
            criar_cliente(clientes)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Operação inválida, por favor selecione novamente a operação desejada. ')


main()