from torres import *

n = int(input("cuantos discos: "))
#n = 5
T_A,T_B,T_C = torres().clavijas(n)

pilares = [T_A, T_B, T_C]
for x,y,z in zip(*pilares):
    print x,y,z

void = [(n * " ") + ("0") + (n * " ")]
juego = True
k = 2
j = 0
i = 0
while juego:
    direccion = str(raw_input("En que direccion desea moverse: "))
    lista_reemplazo = []
    lista_paso = []
    torre_actual = []
    torre_destino = []
    if direccion == "a":
        torre_actual = pilares[i]
        torre_destino = pilares[i - 1]
        lista_paso.append(torre_destino[n + 1])
        torre_destino[n + 1] = torre_actual[n + 1]
        torre_actual[n + 1] = lista_paso[0]
        for x,y,z in zip(*pilares):
            print x,y,z
        i = i - 1
    if direccion == "d":
        torre_actual = pilares[i]
        torre_destino = pilares[i + 1]
        lista_paso.append(torre_destino[n + 1])
        torre_destino[n + 1] = torre_actual[n + 1]
        torre_actual[n + 1] = lista_paso[0]
        for x,y,z in zip(*pilares):
            print x,y,z
        i = i + 1
    if direccion == "q":
        juego = False
    if direccion == "s":
        torre_actual = pilares[i]
        while j < n:
            if torre_actual[j] != void[0]:
                lista_paso.append(torre_actual[j])
                direccion = str(raw_input("En que direccion desea moverse: "))
                if direccion == "a":
                    torre_destino = pilares[i - 1]
                    lista_paso.append(torre_destino[n + 1])
                    torre_destino[n + 1] = torre_actual[n + 1]
                    torre_actual[n + 1] = lista_paso[1]
                    while k < n + 2:
                        torre_inversa = torre_destino.reverse()
                        if torre_inversa[k] == void[0]:
                            lista_reemplazo = torre_inversa[k]
                            torre_destino[k] = lista_paso[0]
                            k = n + 3
                        else:
                            k = k + 1
                    torre_actual[j] = lista_reemplazo[0]
                    for x,y,z in zip(*pilares):
                        print x,y,z
                    i = i - 1
                if direccion == "d":
                    torre_destino = pilares[i + 1]
                    lista_paso.append(torre_destino[n + 1])
                    torre_destino[n + 1] = torre_actual[n + 1]
                    torre_actual[n + 1] = lista_paso[1]
                    while k < n + 2:
                        torre_inversa = torre_destino[::-1]
                        if torre_inversa[k] == void[0]:
                            lista_reemplazo = torre_inversa[k]
                            torre_destino[k] = lista_paso[0]
                            k = n + 3
                        else:
                            k = k + 1
                    torre_actual[j] = lista_reemplazo[0]
                    for x,y,z in zip(*pilares):
                        print x,y,z
                    i = i + 1
