from banco import*
from operacoes.deposito import depositar
from operacoes.consulta import consultarSaldo
from operacoes.saque import sacar 
from operacoes.transferencia import transferir

def menu():
    while True:
        print('-----Sistema bancario------------')
        print('1 - Adicionar Conta')
        print('2 - Editar  Conta')
        print('3 - Consultar Conta')
        print('4 - Apagar Conta')
        print('5 - Listar Conta')
        print('6 - Atualizar Nome')
        print('7 - Atualizar Saldo')
        print('8 - Realizar saque')
        print('9 - Realizar deposito')
        print('10 - Consultar saldo')
        print('11- Transferencia ')
        print('12- Sair')

        opcao = input('Selecione uma Opção')

