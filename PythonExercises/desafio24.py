cidade = input('Digite o nome da cidade: ')
cidade = cidade.upper()
cidade = cidade.split()


if cidade[0].find('SANTO') == 0 or cidade[0].find('SAO') == 0:
    print('Essa Cidade tem nome de santo')
else:
    print('Essa Cidade não tem nome de santo')