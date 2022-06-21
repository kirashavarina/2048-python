import random
import copy

def print_arr(arr):
    print('-' * 10)
    for row in arr:
        print(*row)
    print('-' * 10)

# функция для присваивания индекса
def get_number_from_index(i, j):
    return i*4+j+1

def get_index_from_number(num):
    num -= 1
    x, y = num // 4, num % 4
    return x, y

def insert_2_or_4(arr, x, y):
    if random.random() <= 0.75:
        arr[x][y] = 2
    else:
        arr[x][y] = 4
    return arr

def get_empty_list(arr):
    empty = []
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty

def is_empty(arr):
    for row in arr:
        if 0 in row:
          return True
    return False

def move_left(arr):
    # сохранить первоначальное значение массива
    origin = copy.deepcopy(arr)
    delta = 0
    for row in arr:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            # добавляем в конец - то есть справа
            row.append(0)
    for i in range(4):
        for j in range(3):
            if arr[i][j] == arr[i][j+1] and arr[i][j] != 0:
                arr[i][j] *= 2
                delta += arr[i][j]
                arr[i].pop(j+1)
                arr[i].append(0)
    return arr, delta, not origin == arr

def move_right(arr):
    origin = copy.deepcopy(arr)
    delta = 0
    for row in arr:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            # добавляем в начало - то есть слева
            row.insert(0, 0)
    for i in range(4):
        for j in range(3, 0, -1):
            if arr[i][j] == arr[i][j-1] and arr[i][j] != 0:
                arr[i][j] *= 2
                delta += arr[i][j]
                arr[i].pop(j-1)
                arr[i].insert(0, 0)
    return arr, delta, not origin == arr

def move_up(arr):
    origin = copy.deepcopy(arr)
    delta = 0
    for j in range(4):
        column = []
        # при помощи этого цикла из колонки 8004 сделали список 84
        for i in range(4):
            if arr[i][j] != 0:
                column.append(arr[i][j])
        while len(column) != 4:
            # добавляем нули в конец
            column.append(0)
        for i in range(3):
            if column[i] == column[i+1] and column[i] != 0:
                column[i] *= 2
                delta += arr[i][j]
                column.pop(i+1)
                column.append(0)
        # преобразуем массив обратно
        for i in range(4):
            arr[i][j] = column[i]
    return arr, delta, not origin == arr

def move_down(arr):
    origin = copy.deepcopy(arr)
    delta = 0
    for j in range(4):
        column = []
        # при помощи этого цикла из колонки 8004 сделали список 84
        for i in range(4):
            if arr[i][j] != 0:
                column.append(arr[i][j])
        while len(column) != 4:
            # добавляем нули в начало
            column.insert(0, 0)
        for i in range(3, 0, -1):
            if column[i] == column[i-1] and column[i] != 0:
                column[i] *= 2
                delta += arr[i][j]
                column.pop(i-1)
                column.insert(0, 0)
        # преобразуем массив обратно
        for i in range(4):
            arr[i][j] = column[i]
    return arr, delta, not origin == arr

def can_move(arr):
    # три потому что обращаемся к соседям рядом
    for i in range(3):
        for j in range(3):
            if arr[i][j]==arr[i][j+1] or arr[i][j] == arr[i+1][j]:
                return True
    return arr[3][3] == arr[2][2] or arr[3][3] == arr[3][2]
