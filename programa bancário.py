#Programa bancário com opções de depósito, saque, extrato e crianção de usuário e conta - versão 2
menu = '''

[0] Depositar
[1] Sacar
[2] Extrato
[3] Abrir Nova Conta
[4] Sair

=> '''

saldo = 0
extrato = f"Saldo Anterior: {saldo}\n"
numero_saques = 0
usuario = dict()
agencia = '0001'
numero_conta = []
conta_corrente = [agencia, usuario, numero_conta]


#Definindo função para criar usuário abrindo uma conta
def criar_usuario():
    global usuario
    global conta_corrente

    cpf = str(input('Digite os números do seu CPF: ')).replace('.', '').strip()

    if cpf.isnumeric() and cpf is not usuario and len(cpf) == 11:
              
        while True:
            import time
                        
            #cadastrando o nome
            nome = str(input('Digite seu nome completo: ')).strip().title()
            #removendo espaços
            nome2 = nome.replace(' ','')
            #verificando se o nome inserido está correto
            if nome2.isalpha() == True:
                nome1 = nome.split()
                nome3 = nome1[0]
                ultimo_nome = nome1[-1]
                time.sleep(0.2)
                print(f'Olá {nome3} {ultimo_nome}!')
                
                #Cadastrando a data de nascimento e verificando se é maior de idade
                from datetime import datetime
                data_nascimento = datetime.strptime(input('Digite a sua data de nascimento (formato dd/mm/AAAA): '), "%d/%m/%Y")
                idade = (datetime.now() - data_nascimento).days//365
                    
                if idade >= 18:
                                            
                        # criando o endereço
                    print('Ótimo, vamos cadastrar o seu endereço')
                    rua = str(input('Digite o nome da Rua: '))
                    num = int(input('Digite o número da sua casa: '))
                    bairro = str(input('Digite o seu bairro: '))
                    cidade = str(input('Digite a sua cidade: '))
                    estado = str(input('Digite o Estado: '))
                    cep = str(input('Digite seu CEP: '))
                    endereço = [rua, num, bairro, cidade, estado, cep]
                    print('Cadastro realizado com sucesso.')

                    #Após cumpridas as condições, inserir dados no cadastro
                    usuario['nome_completo'] = nome
                    usuario['CPF'] = cpf
                    usuario['Data de nascimento'] = data_nascimento
                    usuario['Idade'] = idade
                    usuario['Endereço'] = endereço
                    conta_corrente.append(usuario.copy())
                    criar_conta()
                    return menu
                    

                else:
                    print('Você não possui a idade necessária. Não é possível abrir a conta.')
                    return menu
            else:
                print('O nome digitado não é válido. Digite novamente.')
                criar_usuario()

    elif cpf in usuario:
        print('Certo! Você já possui cadastro!')
        n = str('Deseja abrir nova conta? [S/N] ').upper()
        if n == 'S':
            criar_conta()
        
    else:
        print('O número digitado não é válido. Tente novamente')
        return menu
                    
            
            
#Definindo função para cria conta
def criar_conta():
    import random
    import math
    global usuario
    global conta_corrente

    for usuario['CPF'] in conta_corrente:
        n_conta = math.ceil(100000*random.random())
        
    usuario['numero_conta'] = n_conta
    conta_corrente.append(usuario.copy())
    print('Conta criada com sucesso')
    print(f'O número da sua conta é {n_conta}')
       


#Definindo função depósito
def deposito (): 
    print('Depósito')
    global saldo
    global extrato
    valor = float(input('Informe o valor do depósito: R$ '))
    if valor > 0:
        print('Valor depositado com sucesso')
        saldo += valor
        extrato = extrato + f'Depósito: + R$ {valor:.2f}\n'
    else: 
        print('O valor digitado é inválido. Por favor, selecione novamente a operação')

#Definindo função saque
def saque():
    global saldo
    global extrato
    global numero_saques
    print ('Saque')
    valor = float(input('Informe o valor que deseja sacar: R$ '))
       
    if saldo <= 0:
        print('Saldo insuficiente')
      
    elif numero_saques < 3 and valor <= 1500 and saldo > 0:
            print(f'Saque permitido. Retire o valor.')
            numero_saques +=1
            saldo = saldo - valor
            extrato = extrato + f'Saque: - R$ {valor:.2f}\n'
            valor += valor
    else:
        print('Operação inválida. Você excedeu o limite diário.')

# Definindo função extrato 
def extrato_conta ():
    global saldo
    global extrato
    print('\n=======Extrato======')
    print (f'{extrato}')
    print( f'\nSaldo disponível: R$ {saldo:.2f}')


while True:
    opcao = input(menu)

    if opcao == '0':
        deposito()

    elif opcao == '1':
        saque()

    elif opcao == '2':
        extrato_conta()
    
    elif opcao == '3':
        criar_usuario()
        
    elif opcao == '4':
        break
    else :
        print('Operação inválida. Por favor, selecione novamente a operação desejada.')
