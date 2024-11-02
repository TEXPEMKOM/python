# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.

import random



def gen_random_list():
    """
    # gen_num_list = num_elements = random.randint(3, 10) генерирует случайное количество єллементов списка в диапазоне от 3 до 10.
    # gen_element_list генерирует список случайньіх єллементов в диапазоне от 1 до 100 в колличестве = gen_num_list
    """
    gen_num_list = random.randint(3, 10)
    gen_element_list = [random.randint(1, 100) for _ in range(gen_num_list)]
    return gen_element_list

# создаем новьій список с необходимьіми єллементами(первьім, третим и второй с конца)
def extract_specific_elements(lst):
    if len(lst) < 3:
        raise ValueError("B C/7uCKE DOJI)|(HO 6bITb HE MEHbLLIE 3-x EJIEMEHTOB")

    return [lst[0], lst[2], lst[-2]]

start_list = gen_random_list()
new_list = extract_specific_elements(start_list)

print("C/7uCOK -  In: ", start_list)
print("C/7uCOK - Out: ", new_list)