# ДЗ 7.3. Пошук підрядка
# Функція second_index приймає як параметри 2 рядки. Вам необхідно знайти індекс другого входження шуканого рядка у рядку для пошуку.
# Розберемо перший приклад, де необхідно знайти друге входження "s" в слові "sims".
# Якби нам треба було знайти її перше входження, то тут все просто:
# за допомогою функції index або find ми можемо дізнатися, що "s" - це перший символ у слові "sims", а значить індекс першого входження дорівнює 0.
# Але нам Необхідно визначити другу "s", а вона четверта за рахунком. Значить індекс другого входження (і у відповідь питання) дорівнює 3.
# Рядок, який потрібно знайти, може складатися з кількох символів.
# Input: Два рядки (String).
# Output: Int or None
#
# Приклади:
#
# def second_index(text, some_str):
#     pass
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')

def second_index(text, some_str):
    """
    Функция для нахождения индекса второго вхождения искомой строки в строке для поиска.
    :param text: Строка, в которой ищем.
    :param some_str: Строка, которую ищем.
    :return: Индекс второго вхождения или None, если такого нет.
    """
    # Находим первое вхождение искомой строки
    first_occurrence = text.find(some_str)

    # Если первое вхождение не найдено, возвращаем None
    if first_occurrence == -1:
        return None

    # Находим второе вхождение, начиная поиск после первого вхождения
    second_occurrence = text.find(some_str, first_occurrence + len(some_str))

    # Если второе вхождение найдено, возвращаем его индекс, иначе возвращаем None
    if second_occurrence != -1:
        return second_occurrence
    else:
        return None

# Тесты
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
