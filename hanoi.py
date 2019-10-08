import curses
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN
from torres import *

n = 5
T_A,T_B,T_C = torres().clavijas(n)

pilares = [T_A, T_B, T_C]

mover = 1

if mover == 1:
    lista_paso = []
    lista_paso.append(T_B[n-1])
    T_B[n-1] = T_A[0]
    T_A[0] = lista_paso[0]
    for x,y,z in zip(*pilares):
        print x,y,z
    mover = 0
    lista_paso = []
