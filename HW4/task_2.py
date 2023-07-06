# Напишите функцию для транспонирования матрицы.


def transponder_matrix():
    final = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            final[j][i] = matrix[i][j]

    print(*final, sep="\n")


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transponder_matrix()
