while 1:
    flag = False
    a = int(input('Digite o lado 1:'))
    b = int(input('Digite o lado 1:'))
    c = int(input('Digite o lado 1:'))

    if (b - c) < a < (b + c):
        print("1")
        if (c - a) < b < (c + a):
            print("2")
            if (b - a) < c < (b + a):
                print("3")
                flag = True

    if flag:
        print('Os valores digitados formam um triangulo')
    else:
        print('Os valores digitados nao formam um triangulo')








