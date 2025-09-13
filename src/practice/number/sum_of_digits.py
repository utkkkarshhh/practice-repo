def sum_of_digits(num: int):
    sum = 0
    num = str(num)
    for digit in num:
        sum += int(digit)
    return sum

print(sum_of_digits(159))