# Zadanie №2

s = input("Введите слово: ")
for i in range(len(s)):
    if i == 2:
        continue
    if s[i] == 'c':
        print(" Найден символ 'c' ")
    print(s[i], end='')

print("\n Длина строки:", len(s) - 1)
