
import random
import time

from storage import logses


def queen_beat (position: list[list[int]]) -> bool:
    n = 8
    x = []
    y = []

    for i in range(n):
        x.append(position[i][0])
        y.append(position[i][1])
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    if correct:
        return True
    else:
        return False

def success_position (count_success):
    start = time.time()
    position = []
    n = 8
    count = 1
    count_iter = 0
    while count <= count_success:
        count_iter += 1
        i = 0
        while i < n:
            x = random.randint(1, 8)
            y = random.randint(1, 8)
            if [x, y] not in position:
                position.append([x, y])
                i += 1

        if queen_beat(position):
            end = time.time()
            data = f' Попытка номер: {count_iter}, затраченное время: {end - start}'
            logses.log(position, data)

            count += 1
        print(position)
        position.clear()