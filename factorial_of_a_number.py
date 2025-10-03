import math

def get_correct_number():
    while True:
        try:
            number = int(input("Введите неотрицательное целое число :"))
            if number >= 0:
                return number
            print("Число не может быть отрицательным. Попробуй снова.")
        except ValueError:
            print("Пожалуйста, введите целое число.")


def main():
    number = get_correct_number()
    result = math.factorial(number)
    print(f"Файториал числа {number} равен {result}")

if __name__ == "__main__":
    main()