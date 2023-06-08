#Zadanie 7

import math
import random


class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Ошибка при деление на '0' "


class Power:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def exponentiation(self):
        return self.num1**self.num2


class Modulo:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def remainder(self):
        return self.num1 % self.num2


class RandomGenerator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def generate(self):
        return random.randint(self.num1, self.num2)


class Factorial:

    def __init__(self, num):
        self.num = num

    def calculate(self):
        return math.factorial(self.num)


class InverseCosine:

    def __init__(self, num):
        self.num = num

    def calculate(self):
        if -1 <= self.num <= 1:
            return math.acos(self.num)
        else:
            return "Выберетеот -1 до 1!"
