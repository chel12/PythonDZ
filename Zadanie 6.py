#Zadanie №6

import math
import random

print(
    "Выберете одну из операций ('+', '-', '*', '/', '**', 'mod', 'rand', 'fact', 'acos'):"
)
operation = input()

if operation == '+':
    print("Введите первое число:")
    num1 = float(input())
    print("Введите второе число:")
    num2 = float(input())
    print("Сумма равна:", num1 + num2)

elif operation == '-':
    print("Введите первое число:")
    num1 = float(input())
    print("Введите второе число:")
    num2 = float(input())
    print("Result:", num1 - num2)

elif operation == '*':
    print("Введите первое число:")
    num1 = float(input())
    print("Введите второе число:")
    num2 = float(input())
    print("Result:", num1 * num2)

elif operation == '/':
    print("Введите первое число:")
    num1 = float(input())
    print("Введите второе число:")
    num2 = float(input())
    if num2 != 0:

        print("Сумма равна:", num1 / num2)
    else:
        print("Делить на '0' нельзя ")

elif operation == '**':
    print("Введите число для возведения в степень:")
    num1 = float(input())
    print("Введите степень:")
    num2 = float(input())
    print("Итоговый результат:", num1**num2)

elif operation == 'mod':
    print("Введите число:")
    num1 = float(input())
    print("Введите модуль:")
    num2 = float(input())
    print("Итоговый результат:", num1 % num2)

elif operation == 'rand':
    print("Введите диапазон случайного числа:")
    print("Введите минимальное число:")
    num1 = int(input())
    print("Введите максимальное число:")
    num2 = int(input())
    print("Случайное число из заданного диапазона: [", num1, ",", num2, "]:",
          random.randint(num1, num2))

elif operation == 'fact':
    print("Введите число для вычисления факториала:")
    num1 = int(input())
    print("Итоговый результат:", math.factorial(num1))

elif operation == 'acos':
    print("Введите число для вычисления арккосинуса (от -1 до 1):")
    num1 = float(input())
    if -1 <= num1 <= 1:
        print("Итоговый результат:", math.acos(num1))

    else:
        print("Число должно быть от -1 до 1!")
