# 10.3 Перевірити чи є парним чи ні
# Ваша функція is_even повинна повертати True якщо число парне, і False якщо число непарне.
# Вхідні дані: Ціле число.
# Вихідні дані: Логічний тип.
#
# def is_even(digit):
#     """ Перевірка чи є парним число """
#     pass
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')

def is_even(digit):
    """ Перевірка чи є парним число """
    # Число является четным, если его остаток от деления на 2 равен 0
    return digit % 2 == 0

# Тесты
assert is_even(2) == True, 'Test1'  # 2 является четным числом
assert is_even(5) == False, 'Test2'  # 5 является нечетным числом
assert is_even(0) == True, 'Test3'  # 0 является четным числом

print('OK')

