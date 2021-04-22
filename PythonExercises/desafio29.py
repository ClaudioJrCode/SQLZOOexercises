while 1:
    velocidade = int(input('Digite sua velocidade no veículo:'))
    velmaxima = 80
    multa = 7.00

    if velocidade <= velmaxima:
        print("voce esta dentro do limite de velcidade")
    else:
        print(f'Voce esta acima do limite e tera de pagar uma multa de R${((velocidade - velmaxima)*multa):.2f}')
