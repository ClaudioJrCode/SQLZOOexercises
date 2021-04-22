while 1:
    salario = float(input('Digite seu Salario: '))
    if salario > 1250:
        salario = salario * 1.1
        print('10')
    else:
        print('15')
        salario = salario * 1.15
    print(f'seu novo salario é de: R${salario:.2f}')





