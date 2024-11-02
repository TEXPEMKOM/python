# Користувач вводить рядок.
# завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# починатися з цифри, містити великі літери, пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
# Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))
# Наприклад:
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

import string
import keyword

def is_valid_variable_name(name):
    # Провкрка зарегистрированньіх слов
    if name in keyword.kwlist:
        return False
    # Проверка на наличие хотябьі одного символа "_"
    if name.count('_') > 1:
        return False
    # Проверка на начало с цифрьі
    if name[0].isdigit():
        return False
    # Проверка на запрещенньіе слова
    for char in name:
        if char in string.punctuation and char != '_':
            return False
        if char.isupper():
            return False
        if char.isspace():
            return False
    return True
variable_name = input("Введите имя переменной: ")
result = is_valid_variable_name(variable_name)

print("Возможньіе именна переменной:", result)



# # Пример имен переменньіх и результат:
# # Вьівод значений используемьіх в валидации
# examples = {
#     "valid_name": "valid_name",
#     "invalidName": "invalidName",
#     "1invalid": "1invalid",
#     "import": "import",
#     "var_name_with_more_than_one_underscore": "var_name_with_more_than_one_underscore"
# }
#
# print("Пример имен переменньіх и результат")
# for ex_name, ex_value in examples.items():
#     ex_result = is_valid_variable_name(ex_value)
# print(f"{ex_name}: {ex_value} => {ex_result}")