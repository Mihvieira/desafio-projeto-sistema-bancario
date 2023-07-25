#criar programa com saque, depósito e extrato
menu = '''

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> '''
saldo = 0
extrato = ""
numero_saques = 0
d = 0
s = 0

while True:
    opcao = input(menu)

    if opcao == '0':
        print('Depósito')
        d = float(input('Digite o valor que deseja depositar: R$ '))
        if d > 0:
            print(f'R$ {d} valor depositado com sucesso')
            saldo = saldo + d
            extrato = extrato + f'Depósito: + R$ {d:.2f}'
                        
        else: 
            print('O valor digitado é inválido. Por favor, selecione novamente a operação')

    elif opcao == '1':
        print ('Saque')
        s = float(input('Quanto deseja sacar? R$ '))
        
        if numero_saques < 3 and s <= 1500 and saldo > 0:
            print(f'Saque permitido. Retire o valor R$ {s}.')
            numero_saques +=1
            saldo = saldo - s
            extrato = extrato + f'Saque: - R$ {s:.2f}'
            s = s + s

        else:
            print('Operação inválida. Você excedeu o limite diário.')

    elif opcao == '2':
        print('Extrato')
        print (f'{extrato}')
        print( f'Seu saldo é de R$ {saldo}')
    
    elif opcao == '3':
        break
    
    else :
        print('Operação inválida. Por favor, selecione novamente a operação desejada.')




