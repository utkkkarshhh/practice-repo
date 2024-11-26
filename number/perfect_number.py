def perfect_number(num: int):
    
    """""
    A Perfect number is the one where the sum of all the divisors of a number are equal to the number it self
    """""
    all_divisors = find_all_divisors(num)
    if sum(all_divisors) == num:
        return f"{num} is a perfect number!"
    return f"{num} is not a perfect number!"

def find_all_divisors(num: int) -> list:
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return divisors

print(perfect_number(6))
print(perfect_number(28))
print(perfect_number(10))
