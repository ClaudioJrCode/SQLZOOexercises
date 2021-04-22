nome = input('Digite seu nome completo: ')
nome = nome.upper()
flag = nome.find("SILVA")+1

if flag:
    print('Tem SILVA no nome')
else:
    print('Nao tem SIlva no nome')