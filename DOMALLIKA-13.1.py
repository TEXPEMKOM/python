# ДЗ 13.1. Група студентів
#Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
#На його основі створіть клас Студент (перевизначте метод виведення інформації).
#Створіть клас Група, екземпляр якого складається з об'єктів класу Студент.
#Реалізуйте методи додавання, видалення студента та метод пошуку студента на прізвище.
#Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі,
# інакше - None.
#У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)
#Визначте для групи метод str() для повернення списку студентів у вигляді рядка.
# Заповнюємо надані заголовки.

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

    # метод (функція) __str__ перевизначається, т.я. потрібно надрукувати всю інформацію про студенат, включаючи
    # номер залікової книжки (у текстовому форматі).
    def __str__(self):
        return f" {super().__str__()}, Record_book: {self.record_book}"

# Клас Group - множина, перелік студентів, має атрибут (змінну) - номер групи.
class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    # Для додавання використовується метод add_student
    def add_student(self, student):
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
st3 = Student("Female", 21, "Bob", "White", "RB33")

group = Group("AM1")
group.add_student(st1)
group.add_student(st2)
print(group)

group.add_student(st3)
print(group)

group.delete_student("Cruz")
group.delete_student("Black")
print(group)


#ДЗ 13.2. Клас "Цифровий лічильник"
# Створити клас цифрового лічильника. У класі реалізувати методи:
# встановлення максимального значення лічильника,встановлення мінімального значення лічильника
# встановлення початкового значення лічильника.
# Метод step_up збільшує лічильник на 1,викликати до тих пір, поки значення досягне максимуму.
# При досягненні максимуму слід викинути (raise) виняток ValueError, з описом, що досягнуто максимумуʼ.
# Метод step_down зменшує лічильник на 1, викликати до тих пір, поки значення не досягне
# мінімуму. При досягненні мінімуму потрібно викинути (raise) виняток ValueError, з описом, що
# досягнутий мінімум повернення поточного значення лічильника.
# Початкове, мінімальне та максимальне значення лічильника також можуть бути додані в метод
# ініціалізації екземпляра класу.
# Надано приблизний каркас для класу та варіанти перевірки.

class Counter:
    # ініціалізація (конструктор) лічильника з початковим значенням, мінімальним та максимальним значенням.
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value
    # встановлюємо початкове значення лічильника, яке повинно бути більше мінімального та меньше максимального
    # значення
    def set_current(self, start):
        if self.min_value < start < self.max_value:
            self.current = start
        else:
            raise ValueError (f"Значення {start} не у межах діапазону лічильника з {self.min_value} до {self.max_value}.")

    # встановлюємо максимальне значення лічильника, яке не повинно бути меньше мінімального значення
    def set_max(self, max):
        if max < self.min_value:
            raise ValueError("Максимальне значення не може бути меньше мінімального.")
        self.max_value = max

    # встановлюємо мінімальне значення лічильника, яке не повинно бути більшим максимального значення
    def set_min(self, min):
        if  min > self.max_value :
            raise ValueError("Мінімальне значення не може бути більше максимального.")
        self.min_value = min

    # метод (функція) збільшення значення лічильника на 1 до досягнення максимального значення
    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Досягнуто максімуму.")

    # метод (функція) зменьшення значення лічильника на 1 до досягнення мінімального значення
    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Досягнуто мінімуму.")

    # поточне значення лічильнику
    def get_current(self):
        return self.current


# перевіряємо
# створюємо екземпляр та збільшуємо лічильник з 8 до 10
counter = Counter()
counter.set_current(8)
counter.step_up()
counter.step_up()
# # потім збільшемо ще на 1 (шоб викинуло помилку)
# counter.step_up()
counter.set_min(8)
# зменшуємо лічильник з 10 до 8
counter.step_down()
counter.step_down()
# потім зменьшемо ще на 1 (шоб викинуло помилку)
# counter.step_down()