nome = input("Digite seu nome: ")
print('seu nome é em minusculas: {}'.format(nome.lower()))
print('seu nome em maisculas: {}' .format(nome.upper()))
print('a quantidade de letras do seu nome sem espaço é de {} letras'.format(len(nome) - nome.count(' ')))
dividir = nome.split()
print(f'seu primeiro nome tem {len(dividir[0])} letras')
