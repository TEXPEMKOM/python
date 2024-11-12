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
