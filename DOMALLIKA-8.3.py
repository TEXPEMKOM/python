# 8.3. Унікальне число
# Вам необхідно написати функцію find_unique_value, яка приймає список із чисел,
# знаходить серед них унікальне число та повертати його.
# Унікальне число - це число, яке зустрічається в списку один раз.
# Випадок, коли в одному списку буде кілька унікальних чисел, перевіряти не потрібно.
#
# Приклад:
#
# def find_unique_value(some_list):
#     pass
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")

def find_unique_value(some_list):
    # Создаем словарь для подсчета количества каждого числа
    count_dict = {}
    for num in some_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Ищем число, которое встречается один раз
    for num, count in count_dict.items():
        if count == 1:
            return num

# Тесты
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'

print("ОК")


# v2
import re

def is_palindrome(text):
    """
    Функция для проверки, является ли строка палиндромом.
    :param text: Входная строка.
    :return: Булево значение True, если строка является палиндромом, иначе False.
    """
    # Приводим строку к нижнему регистру и удаляем все неалфавитные символы
    cleaned_text = re.sub(r'[^a-z0-9]', '', text.lower())

    # Проверяем, является ли очищенная строка палиндромом
    return cleaned_text == cleaned_text[::-1]

# Тесты
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
