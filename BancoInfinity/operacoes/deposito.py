from banco import obterConta

def depositar(conta: int, valor:float)-> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['saldo'] += valor
        print("Depositado Realizado com suceeso ")
    else:
        print("Cliente Não Localizado")
        
