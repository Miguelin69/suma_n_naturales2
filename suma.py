N = int(input("Digite el valor de N: "))

i = 1
suma = 0

while (i<=N):
    suma = suma + i
    i = i +1 
    print("i = " , str(i))
    print("suma = " , str(suma))

print("La suma es " , str(suma))