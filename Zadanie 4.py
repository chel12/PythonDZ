#Zadanie №4

print("Введите название овощей в количестве 3 штук:")
veg1 = input().strip()
veg2 = input().strip()
veg3 = input().strip()

print("Lowercase: {}, {}, {}".format(veg1.lower(), veg2.lower(), veg3.lower()))
print("Uppercase: {}, {}, {}".format(veg1.upper(), veg2.upper(), veg3.upper()))


def capitalize_first(s):
    return s[0].upper() + s[1:]


print("Capitalized: {}, {}, {}".format(capitalize_first(veg1),
                                       capitalize_first(veg2),
                                       capitalize_first(veg3)))

print("Введите количество каждого овоща:")
amount1 = int(input())
amount2 = int(input())
amount3 = int(input())

# Вывод количества каждого овоща
print("Вывод количества овощей - {} ({}, {}), {} ({}, {}), {} ({}, {})".format(
    veg1, amount1, veg1.upper(), veg2, amount2, veg2.upper(), veg3, amount3,
    veg3.upper()))
