while 1:
    ano = int(input('Digite um ano: '))
    flag = True

    if ano % 4 != 0:
        if ano % 400 != 0:
            print('O ano não é bissexto')
    if ano % 4 == 0:
        if ano % 100 != 0:
            print('O ano é bissexto')