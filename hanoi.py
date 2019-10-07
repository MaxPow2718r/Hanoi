'''
rules:
    -n numbers of disks
    -3 pegs
    -every disk haves different size
    -can't put a bigger disk over
    -start in A
    -ends in C

functions:
    -towers
    -disks
    -pegs (list)
    -moves
#resuelve
def hanoi(n, A, B, C):
    if n == 1:
        print('Move disk %s from %s to %s' %(n, A, B))
        print(A,B,C)

    else:
        hanoi(n-1,A,C,B)
        print('Move disk %s from %s to %s' %(n, A, B))
        print(A,B,C)
        hanoi(n-1,C,B,A)


numb = int(input("how many discs: "))
number = numb
a = 'A'
b = 'B'
c = 'C'
print(a,b,c)
hanoi(number,a,b,c)



entero numero de discos = entrada de usuario
crear torre A
crear torre B
crear torre C

movimientos = 0
agregar numero de discos a torre A

definir discos:
    crear discos = numero de discos
    disco 1 = tamano menor
    disco n = tamano mayor

definir posicion:

definir movimientos legitimos:


Mientras no esten todos los discos en la torre C:
'''

#n = int(input("numero de discos: "))
n = 3
T_A = []
T_B = []
T_C = []
moves = 0
i=0

while i <= n:
    if i<n:
        disk = 2*i + 1
        spaces = n - (i)
        T_A.append((spaces * " ") + (disk * "#") + (spaces * " "))
        T_B.append(((n) * " ") + ("0") + ((n) * " "))
        T_C.append(((n) * " ") + ("0") + ((n) * " "))
    elif i == n:
        T_A.append((2*i + 1) * "_")
        T_B.append((2*i + 1) * "_")
        T_C.append((2*i + 1) * "_")

    i += 1

Torres = [T_A, T_B, T_C]

for x,y,z in zip(*Torres):
    print x,y,z
#print Torres

mover = 1

if mover == 1:
    lista_paso = []
    lista_paso.append(T_B[n-1])
    T_B[n-1] = T_A[0]
    T_A[0] = algo[0]
    for x,y,z in zip(*Torres):
        print x,y,z
    #print Torres
    mover = 0
    lista_paso = []
