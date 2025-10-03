def find_primes(limit):

    primes = []
    
    for number in range(2, limit + 1):
       
        for divisor in range(2, number):
            if number % divisor == 0:
                break
        else:

            primes.append(number)
    
    return primes

numbers = find_primes(100)
print("Простые числа от 2 до 100:")
print(numbers)