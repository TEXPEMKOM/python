# 6.3. Добуток чисел
# Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа, поки воно не стане менше або дорівнювати 9.
# Користувач вводить число з клавіатури.
# Приклади:
# 999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1
def multiply_digits_until_single_digit(number):                     # Определяем функцию, которая принимает целое число в качестве аргумента.
    while number > 9:                                               # Выполняем цикл, пока число больше 9.
        product = 1                                                 # Инициализируем переменную product для хранения результата умножения цифр.
        while number > 0:                                           # Выполняем внутренний цикл, пока число больше 0.
            digit = number % 10                                     # Получаем последнюю цифру числа.
            product *= digit                                        # Умножаем product на последнюю цифру.
            number //= 10                                           # Удаляем последнюю цифру из числа.
        number = product                                            # Присваиваем числу значение product для следующей итерации внешнего цикла.
    return number                                                   # Возвращаем окончательное число, которое меньше или равно 9.

# Дано:
print(multiply_digits_until_single_digit(999))   # 2
print(multiply_digits_until_single_digit(1000))  # 0
print(multiply_digits_until_single_digit(423))   # 8
print(multiply_digits_until_single_digit(33))    # 9
print(multiply_digits_until_single_digit(25))    # 0
print(multiply_digits_until_single_digit(1))     # 1