from math import sqrt, pow
num1 = float(input("digite um dos lados do triangulo retangulo: "))
num2 = float(input("digite agora o outro lado: "))

hipotenusa = sqrt((pow(num1, 2)) + (pow(num2, 2)))
print("a hipotenusa do triangulo q tem como catetos os numero {} e {} é igual a {}".format(num1, num2, hipotenusa))