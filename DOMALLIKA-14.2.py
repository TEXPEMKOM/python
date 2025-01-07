# ДЗ 14.2. Створення власних модулів
#Необхідно зробити дві речі на підставі  ДЗ 14.1.
# 1. До класу Student необхідно додати метод порівняння. Порівнювати можна за тими рядками,
# які повертає метод str Для того, щоб спрацювала коректно ось ця перевірка
# assert gr.find_student('Jobs') == st1
# 2. Рознести класи, які використовували під час виконання завдання про групу студентів за модулями.

from group import Group
from student import Student


def main():
    # Використовуємо - перелік студентів
    st1 = Student("Male", 18, "Tom", "Cruz", 'RB11')
    st2 = Student("Female", 20, "Ann", "Smith", "RB22")
    st3 = Student("Male", 21, "Bob", "White", "RB33")
    st4 = Student("Female", 21, "Emily", "Brown", "RB44")
    st5 = Student("Male", 19, "Daniel", "Miller", "RB55")
    st6 = Student("Female", 18, "Olivia", "Jones", "RB66")
    st7 = Student("Male", 20, "David", "Johnson", "RB77")
    st8 = Student("Female", 21, "Jessica", "Williams", "RB88")
    st9 = Student("Female", 18, "Sarah", "Davis", "RB99")
    st10 = Student("Male", 19, "Michael", "Garsia", "RB10")
    st11 = Student("Male", 19, "James", "Wilson", "RB11")

    group = Group("AM1")
    group.add_student(st1)
    group.add_student(st2)
    group.add_student(st3)
    group.add_student(st4)
    group.add_student(st5)
    group.add_student(st6)
    group.add_student(st7)
    group.add_student(st8)
    group.add_student(st9)
    group.add_student(st10)
    #  group.add_student(st11)
    print(group)

    assert group.find_student("Garsia") == st10
    assert group.find_student("Jobs") == st10

    # group.add_student(st3)
    # print(group)

    # group.delete_student("Cruz")
    # group.delete_student("Black")
    # print(group)


if __name__ == '__main__':
    main()