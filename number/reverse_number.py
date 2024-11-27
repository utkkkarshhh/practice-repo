def reverse_number(num: int):
    
    sign = -1 if num < 0 else 1
    num = abs(num)
    reversed_number = 0
    
    while num > 0:
        digit = num % 10
        reversed_number = reversed_number * 10 + digit 
        num //= 10
        
    return sign * reversed_number

print(reverse_number(100))
print(reverse_number(12345))
