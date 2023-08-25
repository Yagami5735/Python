ini_state = [[1, 6, 3],
             [2, 7, 8],
             [4, 5, 0]]

final_state = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 0]]


def find(val):
    for i in range(3):
        for j in range(3):
            if final_state[i][j] == val:
                x1 = i
                y1 = j
                break
    return x1, y1

def moves():
    


def Fs(est, moves):
    if moves() == 'up' and est <= 0 and est < 3:
        aux = ini_state.pop(x)
        ini_state[1][2] = aux


print(find(0))
