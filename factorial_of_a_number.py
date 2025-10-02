number = int(input("Введите число из которого хотите вычислить факторал: "))

result = 1

for i in range(1, number + 1):
    result *= i

print(f"Факториал числа", {number}, "равен:", {result})