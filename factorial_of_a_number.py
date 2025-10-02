print("Введите число из которого хотите получить факториал: ")
num = int(input())


factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Факториал числа", num, "равен:", factorial)