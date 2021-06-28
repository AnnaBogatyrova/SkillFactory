import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''

    def wrapper():
        count_ls = []
        # np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим! (закоментировано по скольку интересуют данные в динамике)
        random_array = np.random.randint(1, 101, size=(1000))

        for number in random_array:
            count_ls.append(game_core(number))

        score = int(np.mean(count_ls))
        print(f"Этот алгоритм угадывает число в среднем за {score} попыток")
        print(f"Минимальное число попыток -  {min(count_ls)} ")
        print(f"Максимальное число попыток - {max(count_ls)} ")

    return wrapper


@score_game
def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0

    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


@score_game
def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count


@score_game
def game_core_v3(number):
    '''Берем середину от извесного минимума и максимума и сравниваем с числом.
    В зависимости от того число олше или меньше предсказания коректируем шаг'''
    count = 0
    min_step = 1
    max_step = 100
    predict = 0

    while number != predict:
        if max_step - min_step <= 1:
            predict = min_step
            count += 1
            if number != predict:
                predict = max_step
                count += 1
                continue
        predict = min_step + (max_step - min_step) // 2
        count += 1
        if number > predict:
            min_step = predict
        elif number < predict:
            max_step = predict
    return count


print("""Проведен експеремент по результативности алгоритмов угадівания случайного числа от 1 до 100.
Для єтого 3 алгоритма были протестированы каждый по 1000 раз.
Посмотрим на результати:\n""")

print("""1. Алгоритм по котором случайно сгенерированые числа от 1 до 100 
сравниваються с загаданным числом\n""")
game_core_v1()
print("\n")

print("""2. Алгоритм при котором случайно сгенерированое число сравниваються 
с загаданным числом и коректируется на 1 в зависимости от того оно больше или 
меньше загаданого числа\n""")
game_core_v2()
print("\n")

print("""3. (Мой алгоритм) Алгоритм по котором береться среднее значение между извесным шагом 
загаданого числаю Шаг числа коректируется в зависимости от того предсказаное 
значение больше или меньше загаданого числа\n""")
game_core_v3()
