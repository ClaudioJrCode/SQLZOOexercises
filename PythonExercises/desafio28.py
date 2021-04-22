from random import randint

sorteado = randint(1,6)
digitado = int(input('Digite um numero entre 1 e 5:'))
print(sorteado)
if sorteado > digitado:
    num1 = sorteado
    num2 = digitado
else:
    num1 = digitado
    num2 = sorteado
if sorteado == digitado:
    print("parabens!!!voce acertou!!!")
elif sorteado != digitado:
    print(f'Voce errou por {num1 - num2} números de diferença')

