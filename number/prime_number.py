def if_prime(n: int):
    if n <= 1:
        return f"{n} is not a prime number!"
    
    for i in range(2, int(n * 0.5) + 1):
        if n % i == 0:
            return f"{n} is not a prime number!"
        
    return f"{n} is a prime number!"

print(if_prime(11))
