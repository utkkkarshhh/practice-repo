def factorial(n: int):
    if n < 0:
        return 'Factorial cannot be defined for negative numbers.'
    
    factorial = 1
    
    for i in range(1, n):
        factorial *= i
    
    return factorial

print(factorial(5))