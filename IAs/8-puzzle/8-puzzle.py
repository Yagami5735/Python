import copy
from collections import deque
from time import sleep
ini_state = [[1, 2, 3],
             [4, 0, 5],
             [7, 8, 6]]


movimentos = [0, 1, 2, 3]

state = copy.deepcopy(ini_state)


def final_state():
    finalState = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]
    if state == finalState:
        return False
    else:
        return True


def find(matrix):
    pos0 = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                pos0.append(i)
                pos0.append(j)
                break
    return pos0


def move(matrix, posX,  posY, nposX, nposY):
    nMatrix = []
    for i in range(len(matrix)):
        np = []
        for j in range(len(matrix)):
            np.append(matrix[i][j])

        nMatrix.append(np)

    aux = nMatrix[posX][posY]
    nMatrix[posX][posY] = nMatrix[nposX][nposY]
    nMatrix[nposX][nposY] = aux

    return nMatrix


'''obs: eu sei que está invertido, o código é refênte ao movimento do zero, porém o que se movimenta realmente, 
são as peças adjacentes, portanto escrevi invertido'''


def aval(movimento):
    if movimento == movimentos[0]:
        if find(state)[0] != 2:  # limitação pra ir para cima
            return 'DOWN'

    if movimento == movimentos[1]:  # limitação para ir para baixo
        if find(state)[0] != 0:
            return 'UP'

    if movimento == movimentos[2]:  # limtação para ir à direita
        if find(state)[1] != 0:
            return 'LEFT'

    if movimento == movimentos[3]:  # limitação para ir à esquerda
        if find(state)[1] != 2:
            return 'RIGHT'


move_state = [0, 1, 2, 3]
counter = 0
c = 0
n = 1
aux2 = 0
exp = 4
inc = 4

maux = copy.deepcopy(state)
laux = copy.deepcopy(move_state)
while final_state():

    print('Movimentos: '+str(counter))
    print(move_state)
    for i in range(n):
        if (aval(move_state[0]) == 'UP'):
            print('cima')
            state = move(state, find(state)[0], find(state)[
                1], find(state)[0]-1, find(state)[1])

        if (aval(move_state[0]) == 'DOWN'):
            print('baixo')
            state = move(state, find(state)[0], find(state)[
                1], find(state)[0]+1, find(state)[1])

        if (aval(move_state[0]) == 'RIGHT'):
            print('direita')
            state = move(state, find(state)[0], find(state)[
                1], find(state)[0], find(state)[1]+1)

        if (aval(move_state[0]) == 'LEFT'):
            print('esquerda')
            state = move(state, find(state)[0], find(state)[
                1], find(state)[0], find(state)[1]-1)

        aux = move_state.pop(0)
        for i in range(inc):
            move_state.append(aux)
            move_state.append(laux[i])
        for i in range(aux2):
            laux.pop(0)

        laux = copy.deepcopy(move_state)

    c += 1
    if (c == exp):
        n += 1
        aux2 += 1
        exp = exp * 4
        inc = inc * 4

    state = copy.deepcopy(maux)

    sleep(1)
    print(state[0])
    print(state[1])
    print(state[2])
    print('=' * 30)
    counter += 1
print("Parabénss Você Completou o Puzzle!")
