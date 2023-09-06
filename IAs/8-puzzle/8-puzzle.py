import copy

ini_state = [[8, 6, 1],
             [7, 5, 2],
             [4, 3, 0]]

movimentos = ['UP', 'DOWN', 'RIGHT', 'LEFT']


def final_state(): 
    finalState = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]
    if ini_state == finalState:
        return False
    else:
        return True


def find():
    pos0 = []
    for i in range(len(ini_state)):
        for j in range(len(ini_state)):
            if ini_state[i][j] == 0:
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
        if find()[0] != 2: #limitação pra ir para cima
            return 'DOWN'
        else:
            return False
        
    if movimento == movimentos[1]: #limitação para ir para baixo
        if find()[0] != 0:
            return 'UP'
        else:
            return False
    
    if movimento == movimentos[2]: #limtação para ir à direita
        if find()[1] != 0:
            return 'LEFT'
        else:
             return False
    
    if movimento == movimentos[3]: #limitação para ir à esquerda
        if find()[1] != 2:
            return 'RIGHT'
        else:
            return False



while final_state():
    print('=' * 30)
    print(ini_state[0])
    print(ini_state[1])
    print(ini_state[2])
    print('=' * 30)
    print('=' * 30)

    movimento = input("Digite o movimento: ").upper().strip()
    
    print('=' * 30)
    if(aval(movimento) == 'UP'):
        ini_state = move(ini_state, find()[0], find()[1], find()[0]-1, find()[1])

    if(aval(movimento) == 'DOWN'):
        ini_state = move(ini_state, find()[0], find()[1], find()[0]+1, find()[1])

    if(aval(movimento) == 'RIGHT'):
        ini_state = move(ini_state, find()[0], find()[1], find()[0], find()[1]+1)

    if(aval(movimento) == 'LEFT'):
        ini_state = move(ini_state, find()[0], find()[1], find()[0], find()[1]-1)

print("Parabénss Você Completou o Puzzle!")


