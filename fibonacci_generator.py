def generate_fibonacci(number):

    fibonacci = [0, 1]

    for i in range(2, number):
        next_fib = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_fib)

    return fibonacci

number = int(input("Введите количество чисел Фибоначчи для генерации: "))
fibonacci = generate_fibonacci(number)
print(f"Первые {number} чисел Фибоначчи: {fibonacci}")