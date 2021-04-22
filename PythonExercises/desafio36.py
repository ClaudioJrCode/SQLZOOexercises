num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
fat = 1
listafatorial = []
cont = 2

maximo = num1 if num1 > num2 else num2

while cont < maximo+1:

    if num1 % cont != 0 and num2 % cont != 0:
        cont = cont+1
    elif num1 % cont == 0 or num2 % cont == 0:
        fat = cont * fat
        listafatorial.append(cont)
        if num1 % cont == 0:
            num1 = num1 // cont
        else:
            num2 = num2 // cont

print(fat)
print(listafatorial)






