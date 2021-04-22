tarifa1 = 0.5
tarifa2 = 0.45

while 1:
    km = int(input('Digite a quantidade de quilometros da viagem:'))
    if km > 200:
        preco = tarifa2*km
    else:
        preco = tarifa1*km
    print(f'O Valor da viagem sera de R${preco:.2f}')
