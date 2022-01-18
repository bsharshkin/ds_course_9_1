"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np




def binary_search(number:int=50) -> int:
    """Бинарный поиск
    Args:
        number (int, optional): Загаданное число. Defaults to 50.

    Returns:
        int: Число попыток
    """
    first = 0
    last = 100
    count = 0
    while first <= last:
        mid = (first+last)//2
        if number == mid:
            break  # выход из цикла если угадали
        else:
            if number<mid:
                count+=1
                last = mid -1
            else:
                count+=1
                first = mid +1
    return count

def score_game(binary_search) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        binary_search ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(binary_search(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_search)
