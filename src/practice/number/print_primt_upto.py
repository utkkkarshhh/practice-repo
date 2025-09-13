def print_all_primes(n : int) -> list:
    primes = []
    if n < 2:
        return primes
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

print(print_all_primes(100))