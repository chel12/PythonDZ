# Zadanie №1

print("Введите число:")
num1 = float(input())
print("Введите пограничное число:")
boundary = float(input())

if num1 < boundary:
    print("1-ое число меньше пограничного")
elif num1 > boundary:
    print(" 1-ое число больше пограничного")
    if num1 > boundary * 3:
        print("1-ое число больше пограничного более, чем в 3 раза")
