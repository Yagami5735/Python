ini_state = [[1, 5, 3],
             [2, 0, 7],
             [4, 8, 6]]

movimentos = ['UP', 'DOWN', 'RIGHT', 'LEFT']
flag = True

def final_state(): 
    finalState = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]


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



def aval(movimento):
    find()
    coordX = find().pop()
    coordY = find().pop()
    if movimento == movimentos[0]:
        if coordX != 0: #limitação pra ir para cima
            return 'UP'
        
    if movimento == movimentos[1]:
        if coordX != 2:
            return 'DOWN'
    
    if movimento == movimentos[2]:
        for i in range(len(ini_state)):
            for j in range(len(ini_state)):
                if coordY != 2:
                    return 'RIGHT'
    
    if movimento == movimentos[3]:
        for i in range(len(ini_state)):
            for j in range(len(ini_state)):
                if coordY != 0:
                    return 'LEFT'



while True:
    find()
    coordX = find().pop()
    coordY = find().pop()
    if(flag == True):

        movimento = input("Digite o movimento: ").upper().strip()

        if(aval(movimento) == 'UP'):
            move(ini_state, coordX, coordY, coordX+1, coordY)
            print('=' * 30)
            print(ini_state)
            print('=' * 30)

        if(aval(movimento) == 'DOWN'):
            move(ini_state, coordX, coordY, coordX-1, coordY)
            print('=' * 30)
            print(ini_state)
            print('=' * 30)

        if(aval(movimento) == 'RIGHT'):
            move(ini_state, coordX, coordY, coordX, coordY+1)
            print('=' * 30)
            print(ini_state)
            print('=' * 30)

        if(aval(movimento) == 'LEFT'):
            move(ini_state, coordX, coordY, coordX, coordY-1)
            print('=' * 30)
            print(ini_state)
            print('=' * 30)




