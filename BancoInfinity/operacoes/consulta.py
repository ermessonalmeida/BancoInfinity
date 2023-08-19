from banco import obterConta, banco

def consultarSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(F"seu Saldo é {cliente['saldo']}")
    else:
        print('Cliente Não Encontrado!')    

consultarSaldo(1)        