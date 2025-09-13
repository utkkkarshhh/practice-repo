def total_digits_count(num: int):
    counter = 0
    while num > 0:
        num //= 10 #Removes digit from the number
        counter += 1 #Increments the counter by one after removing a digit
    return counter
    

print(total_digits_count(1792))
print(total_digits_count(1231792))
print(total_digits_count(172131192))