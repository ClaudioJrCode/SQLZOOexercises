print("Fibonacci!")
qtde = 0
num1 = 0
num2 = 1
resultado = 0

while (qtde <= 0):
    qtde = int(input("Digite a quantidades de numeros de fibonacci desejada: "))

print("Os numeros de fibonacci: ")
for i in range(qtde):
    resultado = num1 + num2
    num1 = num2
    num2 = resultado
    print (resultado)








Python 3.3
1	def binarySearch(alist, item):
2	    first = 0
3	    last = len(alist)-1
4	    found = False
5
6	    while first<=last and not found:
7	        midpoint = (first + last)//2
8	        if alist[midpoint] == item:
9	            found = True
10	        else:
11	            if item < alist[midpoint]:
12	                last = midpoint-1
13	            else:
14	                first = midpoint+1
15
16	    return found
17
18	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
19	print(binarySearch(testlist, 3))
20	print(binarySearch(testlist, 13))