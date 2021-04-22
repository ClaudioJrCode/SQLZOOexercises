nome = input('Digite seu nome completo')
nome = nome.title()
nome = nome.split()

print(f'Ola {nome[0]} {nome[len(nome)-1]}, tudo bem? ')