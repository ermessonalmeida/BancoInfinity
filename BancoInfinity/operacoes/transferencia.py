from banco import obterConta
from saque import sacar
from deposito import depositar


def transferir(contaOri: int, contaDes: int, valor: float)-> None:
    contaOrigem = obterConta(contaOri)
    contaDestino= obterConta(contaDes)
    if contaDestino and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaDestino['saldo'] += valor
            contaOrigem['saldo'] -= valor
            print('Transferência Realizado Com Sucesso!')
        else:
            print("Saldo Insuficiente Para Transferência!")    
    else:
        print("Uma das Contas Não Existe!")        


