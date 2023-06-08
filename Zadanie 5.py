#Zadanie 5
words = input("Введите слова через ',': ").split(",")
word_set = set(words)
print("Количество слов:", len(words))
second_list = input(
    "Введите список слов такого же количества символов: ").split(",")
dictionary = dict(zip(words, second_list))
print(dictionary)