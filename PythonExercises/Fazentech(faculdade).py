def ordenhar_gado(lista, cod_gado):
    primeiro = 0
    ultimo = len(lista) - 1
    found = False

    while primeiro <= ultimo and not found:

        meiodalista = (primeiro + ultimo) // 2
        if lista[meiodalista] == cod_gado:
            found = True
            posicao = meiodalista+1
            lista.remove(lista[meiodalista])
        else:
            if cod_gado < lista[meiodalista]:
                ultimo = meiodalista - 1
            else:
                primeiro = meiodalista + 1
    if found:
        print(f'Gado encontrado na posição {posicao} e ordenhado com sucesso')
    else:
        print('Gado ja foi ordenhado ou nao existe')

lista = [1001,1002,1003,1005,1006,1007]
while 1:
    a = False
    posicaofila = 0
    print('Os numeros abaixo são dos animais que não foram ordenhadas ainda')
    print(lista)
    print('Digite:')
    print('1 - para ordenhar(tira o animal da lista)')
    print('2 - inserir um gado para ordenha')
    print('3 - para sair: ')
    escolha = int(input())
    if escolha == 1:
        if len(lista) == 0:
            print('Todos os gados ordenhados')
        else:
            codigo = int(input("Digite o código do animal: "))
            ordenhar_gado(lista, codigo)
    elif escolha == 2:
        codigo = int(input("Digite o codigo do animal para coloca-lo na fila:"))
        lista.append(codigo)
        print("Gado Adicionado com sucesso")
    elif escolha == 3:
        break
    else:
        print('Opçao invalida')


  #  print(buscar_gado(lista, 1001))
   # print(buscar_gado(lista, 1006))
