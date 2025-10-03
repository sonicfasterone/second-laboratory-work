number = 15

fibonacci = [0, 1]

for i in range(2, number):
    next_fib = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_fib)

print(f"Первые {number} чисел Фибоначчи: {fibonacci}")