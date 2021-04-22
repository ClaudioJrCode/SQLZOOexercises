while 1:
    num1 = int(input('Digite um numero:(1/3)'))
    num2 = int(input('Digite um numero:(2/3)'))
    num3 = int(input('Digite um numero:(3/3)'))
    maior, menor = 0,0
    if num2 < num1 > num3:
        maior = num1
        if num2 > num3:
            menor = num3
        else:
            menor = num2
    if num1 < num2 > num3:
        maior = num2
        if num1 > num3:
            menor = num3
        else:
            menor = num1
    if num2 < num3 > num1:
        maior = num3
        if num2 > num1:
            menor = num1
        else:
            menor = num2

    print(f'maior: {maior}')
    print(f'menor: {menor}')





