import copy
import pprint

input_minesweeper = [
        ['0', '1', '0', '0'], 
        ['0', '0', '1', '0'], 
        ['0', '1', '0', '1'], 
        ['1', '1', '0', '0']
    ]

# Declarar una matriz vacía dinamica
output_minesweeper = copy.deepcopy(input_minesweeper)

# Para cada elemento en el campo (una matriz 2D)
for i in range(len(input_minesweeper)):
    for j in range(len(input_minesweeper[0])):
        # Si el elemento actual no es '1'
        if input_minesweeper[i][j] != '1':
            # Inicializa un contador a 0
            count_mines = 0
            # Para cada vecino del elemento actual (incluyendo diagonales)
            for x in (-1, 0, 1):
                for y in (-1, 0, 1):
                    # Si el vecino está dentro de los límites del campo y es '1'
                    if (0 <= i+x < len(input_minesweeper) and 0 <= j+y < len(input_minesweeper[0]) and input_minesweeper[i+x][j+y] == '1'): 
                        # Incrementa el contador
                        count_mines += 1
            # Asigna el contador al elemento correspondiente en la matriz de salida
            output_minesweeper[i][j] = str(count_mines)
        else:
            # Si el elemento actual es '1', asigna '9' en la matriz de salida
            output_minesweeper[i][j] = str('9')

pprint.pprint(output_minesweeper)

