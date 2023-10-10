import copy

#definindo a matrix
ini_state = [[1, 2, 3],   
             [0, 5, 6],
             [4, 7, 8]]

#definindo os movimentos
movimentos = [0, 1, 2, 3] 

state = copy.deepcopy(ini_state)


def final_state(matrix):      
    finalState = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]
    return matrix == finalState

#Função para achar o vazio
def find(matrix):                  
    pos0 = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                pos0.append(i)
                pos0.append(j)
                break
    return pos0

#Função para o momvimento
def move(matrix, posX,  posY, nposX, nposY):
    nMatrix = []
    for i in range(len(matrix)):
        np = []
        for j in range(len(matrix)):
            np.append(matrix[i][j])
        #copia a matrix para "nMatrix"
        nMatrix.append(np) 
    #altera as posições
    aux = nMatrix[posX][posY]
    nMatrix[posX][posY] = nMatrix[nposX][nposY]
    nMatrix[nposX][nposY] = aux

    return nMatrix

def Fs(matrix, dir):
    #define as linhas e as colunas para delimitar os movimentos
    lin = len(matrix)
    col = len(matrix[0])
    #checa se o movimento é válido, se for, ele permite o movimento
    if dir == "acima" and find(matrix)[0] > 0:
        return move(matrix, find(matrix)[0], find(matrix)[1], find(matrix)[0] - 1, find(matrix)[1])
    elif dir == "abaixo" and find(matrix)[0] < lin - 1:
        return move(matrix, find(matrix)[0], find(matrix)[1], find(matrix)[0] + 1, find(matrix)[1])
    elif dir == "esquerda" and find(matrix)[1] > 0:
        return move(matrix, find(matrix)[0], find(matrix)[1], find(matrix)[0], find(matrix)[1] - 1)
    elif dir == "direita" and find(matrix)[1] < col - 1:
        return move(matrix, find(matrix)[0], find(matrix)[1], find(matrix)[0], find(matrix)[1] + 1)
    else:
        return None


def bfs(matrix):
  count = 0
  #define a pilha
  pilha = [(matrix, [])]#Tupla:(estado do tabuleiro, lista de movimentos)
  visitados = [matrix]#copia a matrix em visitados

  while pilha:
    #guarda o movimento atual e os movimentos realizados
    atual, movimentos_realizados = pilha.pop()

    #quando o 8-puzzle for resolvido, ele retorna os movimentos realizados para resolvê-lo
    if final_state(atual):
      return movimentos_realizados
    
    #dá início ao looping da pilha
    for dir in ["acima", "abaixo", "esquerda", "direita"]:
      novo_atual = Fs(atual, dir)

      #adiciona os elementos no final da pilha
      if novo_atual and novo_atual not in visitados:
        visitados.append(novo_atual)
        pilha.append((novo_atual, movimentos_realizados + [dir]))
    
    count+=1
    print(count)
  return None

tabuleiro_final = bfs(ini_state)

#se ele achar uma solução ele printa a solução
if tabuleiro_final:
  print("Solução encontrada!")
  tabuleiro_atual = state
  for dir in tabuleiro_final:

    #Atualiza o tabuleiro atual com o movimento
    tabuleiro_atual = Fs(tabuleiro_atual, dir)
    print(f"Movimento: {dir}")

    for linha in tabuleiro_atual:
      print(linha)
    print()
  print("8-Puzzle resolvido!")
else:
  print("Não foi possível solucionar.")
