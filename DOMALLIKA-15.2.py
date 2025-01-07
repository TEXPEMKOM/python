# ДЗ 15.2. Клас «Правильний дріб»
# Створіть клас «Правильний дріб» та реалізуйте методи порівняння, додавання,
# віднімання та множення для екземплярів цього класу.

#  у бібліотеці mach є метод math.gcd(num, denom), який повертає найбільший
#  спільний дільник двох чисел num і denom , використовується для скорочення дробу до найпростішої форми

import math

class Fraction:
    def __init__(self, num, denom):
        if denom == 0:
            raise ValueError ("Denominator can`t be zero.")
        gcd = math.gcd(num, denom)
        self.num = (num // gcd)
        self.denom = denom // gcd

    # магічний метод оператора множення
    def __mul__(self, other):
        return Fraction(self.num * other.num, self.denom * other.denom)

    # магічний метод оператора додавання
    def __add__(self, other):
        return Fraction(self.num * other.denom + other.num * self.denom, self.denom * other.denom)

    # магічний метод оператора віднімання
    def __sub__(self, other):
        return Fraction(self.num * other.denom - other.num * self.denom, self.denom * other.denom)

    # магічний метод оператора порівняння на рівність
    def __eq__(self, other):
        return self.num * other.denom == self.denom * other.num

    # магічний метод оператора більше
    def __gt__(self, other):
        return self.num * other.denom > self.denom * other.num
    # магічний метод оператора менше
    def __lt__(self, other):
        return self.num * other.denom < self.denom * other.num
    # строкове представлення дроби
    def __str__(self):
        return f"Fraction: {self.num}/{self.denom}"

# Використовуємо

fr1 = Fraction(1, 3)
fr2 = Fraction(2, 5)

print(f"Додавання: {fr1 + fr2}")
print(f"Віднімання: {fr1 - fr2}")
print(f"Множення: {fr1 * fr2}")
print(f" Порівняння на рівність: {fr1 == fr2}")
print(f" Порівняння (більше): {fr1 > fr2}")
print(f" Порівняння (менше): {fr1 < fr2}")