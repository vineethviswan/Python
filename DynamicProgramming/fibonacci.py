def fibonacci(n):
    sequence = [0, 1]
    
    if n == 0:
        return sequence[0]
    elif n == 1:
        return sequence[1]
    
    for i in range(2, n + 1):
        next_fib = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_fib)
    
    return sequence[n]

fibonacci_number = fibonacci(10)
print(fibonacci_number)