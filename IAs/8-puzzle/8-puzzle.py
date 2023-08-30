ini_state = [[1, 6, 3],
             [2, 7, 8],
             [4, 5, 0]]

def final_state(): 
    finalState = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]


def find():
    for i in range(len(ini_state)):
        for j in range(len(ini_state)):
            if ini_state[i][j] == 0:
                break
    return i, j

def moves(matrix, posX,  posY, nposX, nposY):
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

print(find())

def res(ini, final):
    while(ini!=final):
        if(find() == ):
