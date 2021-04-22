import math
import time

def calcula(x, ang):
    if x == 1:
        frase = 'O Seno'
        result = math.sin(ang)
    elif x == 2:
        frase = 'O cosseno'
        result = math.cos(ang)
    elif x == 3:
        frase = 'A tangente'
        result = math.tan(ang)
    return frase, result

while 1:
    print("\t SENO, COSSENO E TANGENTE: \n")
    a = input("Para SENO digite:        ----> '1'\n"
              "Para COSSENO digite      ----> '2'\n"
              "Para TANGENTE digite     ----> '3'\n\n"
              "Para SAIR digite qualquer tecla\n")
    if '0' < a < '4':
        b = int(a)
        angulo = float(input('Digite o Angulo: '))
        sujeito, resultado = calcula(b, angulo) #sujeito e resultado recebem frase e result(return)da funçao calcula
        print(f'{sujeito} do angulo de {angulo}º é de {resultado}')
        time.sleep(3)
    else:
        exit()




