def perfect_number(num: int):
    
    """""
    A Perfect number is the one where the sum of all the divisors of a number are equal to the number it self
    """""
    sum_divisors = sum_of_divisors(num)
    if sum_divisors == num:
        return f"{num} is a perfect number!"
    return f"{num} is not a perfect number!"

def sum_of_divisors(num: int) -> list:
    if num <= 1:
        return 0
    
    sum = 1
    limit = int(num **0.5) 
    
    for i in range(2, limit + 1):
        if num % i == 0:
            sum += i
            if i != num // i:
                sum += num // 1
                
    return sum

print(perfect_number(6))
print(perfect_number(28))
print(perfect_number(10))
