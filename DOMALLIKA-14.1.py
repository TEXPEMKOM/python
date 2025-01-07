# ДЗ 14.1. Модифікуйте клас Група
# (завдання 13.1) так, щоб при спробі додавання до групи більше 10-ти студентів,
# було порушено виняток користувача.
# Таким чином потрібно створити ще й виняток користувача для цієї ситуації.
# І обробити його поза межами класу,потрібно перехопити цей виняток,
# при спробі додавання 11-го студента.
# У код ДЗ 13.1 необхідно додати клас винятка та внести умови перевірки.

# Клас Humen - основний для опису людини, має конструктор , який приймає аргументи (змінні):
# стать, вік, ім`я та прізвище.
# метод (функція) __str__ друкує інформацію про людину у текстовому форматі
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Gender: {self.gender} "

# Клас Student успадковує клас Human і додає новий атрібут (змінну) - залікову книжку (record_book).

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    # метод (функція) __str__ перевизначається, т.я. потрібно надрукувати всю інформацію про студента, включаючи
    # номер залікової книжки (у текстовому форматі).
    def __str__(self):
        return f" {super().__str__()}, Record_book: {self.record_book}"

# Клас GroupLimitReachedException - для опису винятку щодо досягнення ліміту кількості студентів
# з наслідуванням стандартного класу винятків Exception шоб створити спеціалізований виняток (ліміт кількості студентів)

class GroupLimitReachedException (Exception):
    def __init__(self, message):
        # self.message = message
        super().__init__(message)


# Клас Group - множина, перелік студентів, має атрибут (змінну) - номер групи.
class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    # Для додавання використовується метод add_student
    # додано перевірку щодо досягнення максимальної кількості студентів у групі та
    # використання класу GroupLimitReachedException
    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitReachedException(f"There can be no more than 10 students in a group {self.number}!")
        self.group.add(student)
    # Для видалення використовується метод delete_student
    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
            return True
        return False

    #Для пошуку студента  за прізвищем використовується метод (функція)
    # find_student. Якщо студент не знайдений - повертає None.
    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None
    # Метод (функція) __str__ повертає список студентів у вигляді рядка
    def __str__(self):
        if not self.group:
            return f"У групі {self.number} студенти відсутні."
        all_students = "\n".join (str(student) for student in self.group)
        return f"Group number:{self.number}\n {all_students}"

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
group.add_student(st11)
print(group)

# group.add_student(st3)
# print(group)

# group.delete_student("Cruz")
# group.delete_student("Black")
# print(group)