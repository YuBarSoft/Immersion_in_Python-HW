# Задача 2. Поиск и сохранение вариаций расположения небьющихся ферзей в файл.

quantity = int(input('Введите требуемое количество вариантов расположения 8 ферзей на шахматной доске (от 1 до 92 включительно): '))


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

    for i in range(row):
        if abs(row - i) == abs(col - board[i]):
            return False

    return True


def solve_n_queens(board, row, n, count, solutions):
    if row == n:
        count[0] += 1
        solution = [(i, board[i]) for i in range(n)]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(board, row + 1, n, count, solutions)
            board[row] = -1


def find_n_queens_solutions(n, count, solutions):
    board = [-1] * n
    solve_n_queens(board, 0, n, count, solutions)


count = [0]
solutions = []
find_n_queens_solutions(8, count, solutions)

# Сохранение вариаций расположения ферзей в файл
with open(f'variables-{quantity}.txt', "w+") as file:
    for solution in solutions[:quantity]:
        file.write(str(solution) + "\n")
print(f'Сохранено {quantity} вариации расположения ферзей в файл variables-{quantity}.txt.')
