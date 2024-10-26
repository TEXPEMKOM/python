def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return ("HET!: HEJIb39I DEJIuTb HA 0! ")
        return a / b
    else:
        return "HE BEPHA9I O/7EPAL|u9I!"

def main():
    try:
        while True:
            a = float(input("BBEDuTE /7EPBOE 4uCJIO: "))
            b = float(input("BBEDuTE BTOPOE 4uCJIO: "))
            operation = input("BbI6EPuTE DEu*CTBUE (+, -, *, /): ")

            result = calculate(a, b, operation)
            print(f"PABHO: {result}")

            continue_calculating = input("/7OBTOPuTb (Yes/No)? ").strip().lower()
            """"
strip() удаляет начальные и конечные пробелы в введенной строке, если они есть.
lower() переводит введенную строку в нижний регистр, чтобы ввод был нечувствителен к регистру
            """
            if continue_calculating != 'Yes':
                break
                """
# if continue_calculating != 'Yes': проверяет, ввел ли пользователь “yes”.
# Если пользователь ввёл что-то другое, цикл прерывается с помощью break, и программа заканчивает свою работу.
                """
    except ValueError:
        print("BBEDuTE DO/7YCTuMOE 3HA4EHuE!")

if __name__ == "__main__":
    main()
