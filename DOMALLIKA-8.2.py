# 8.2. Паліандром
# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False
#
# Приклад:
# def is_palindrome(text):
#     pass
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")

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
