# ДЗ 7.1. Вітання
# Написати функцію say_hi, яка представить людину за переданими параметрами.
# Вхідні дані: Два аргументи рядок(str) та позитивне число(int)
# Функція має повернути рядок.
# Замініть pass на Ваше рішення.
#
# def say_hi(name, age):
#     pass
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')

# функция say_hi - принимает имя и возраст, и возвращает строку с представлением єтих данньіх
def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

# Проверка функции
assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')
