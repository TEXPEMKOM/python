# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв
# Приклад:
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

def get_letters_range(range_str):                                           # Создаем функцию get_letters_range, аргумент которой будет ряд range_str
    start, end = range_str.split('-')                                       # Разделяем входящий ряд на две части с помощью "-"(дефиз), сохраня начальную букву в "start" и конечную букву в "end"
    all_letters = string.ascii_letters                                      # Из модуля "string" получаем все буквьі Англ. алфавита(большие и маленькие) и перисваеваем переменной "all_letters"
    start_index = all_letters.index(start)                                  # Находим индекс начальной буквьі "start" в ряде "all_letters"
    end_index = all_letters.index(end) + 1                                  # Находим индекс конечной букві "end" буквьі в ряде "all_letters" и добавляем 1 что бьі включить последнюю букву
    return all_letters[start_index:end_index]                               # Возвращаем подряд из "all_letters", которьій содержит ряд начиная с начальной буквоьі "start" и заканчивая конечной буквой "end" включительно

# Решение
print(get_letters_range("a-c"))  # abc
print(get_letters_range("a-a"))  # a
print(get_letters_range("s-H"))  # stuvwxyzABCDEFGH
print(get_letters_range("a-A"))  # abcdefghijklmnopqrstuvwxyzA