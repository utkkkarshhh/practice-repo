def armstrong_number(number: int):
    """""
    Armstrong Number: Check if a number is an Armstrong number.
    Known as narcissistic number
    An Armstrong number is a number where the sum of its digits each raised to the power of the total number of digits is equal to the original number.
    153
    """""
    num_str = str(number)
    num_digits = len(num_str) #Will provide the total number of digits i.e 153 -> 3
    digit_sum = 0
    for digit in num_str:
        digit_sum += int(digit) ** num_digits
        
    return digit_sum == number

print(armstrong_number(153))
print(armstrong_number(1002))