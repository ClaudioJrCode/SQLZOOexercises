qtde = 10
numero = 0
resultado = 0
contador = 1

while (numero <= 0):
    numero = int(input("quer saber a tabuada de qual numero?: "))

print(f"tabuada do numero {numero}")
for contador in range(qtde):
    resultado = numero * (contador+1)
    print (f"{contador + 1} X {numero} = {resultado}")







