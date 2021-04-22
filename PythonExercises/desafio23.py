limite = 4
numero = input('Digite um numero de 0 a 9999 (os numeros depois do quarto digito serao ignorados): ')
numero = numero[:limite]
numero = numero.zfill(limite)

inteiro = int(numero)

print(f'{numero[len(numero) - 1]} unidades')
print(f'{numero[len(numero) - 2]} dezendas')
print(f'{numero[len(numero) - 3]} centenas')
print(f'{numero[len(numero) - 4]} milhares')

milhar = int(inteiro / 1000)
inteiro = inteiro % 1000
centena = int(inteiro / 100)
inteiro = inteiro % 100
dezena = int(inteiro / 10)
inteiro = inteiro % 10


print(f'{inteiro} unidades')
print(f'{dezena} dezenas')
print(f'{centena} centenas')
print(f'{milhar} milhares')


