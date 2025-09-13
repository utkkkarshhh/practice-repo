def fibonnaci_no_recursion(limit: int):
    a, b = 0, 1
    fib = []
    for _ in range(limit):
        fib.append(a)
        a, b = b, a + b
    return fib
        

# def fibonacci_recursion(limit: int):
#     if limit < 0:
#         return 0
#     elif limit == 1:
#         return 1
#     else:
#         return fibonacci_recursion(limit - 1) + fibonacci_recursion(limit - 2)

def get_fibonacci_sequence_recursion(limit: int):
    if limit <= 0:
        return []
    elif limit == 1:
        return [0]
    elif limit == 2:
        return [0, 1] #Managing case when the limit is == 2
    
    sequence = get_fibonacci_sequence_recursion(limit - 1)
    print(f"{sequence}")
    sequence.append(sequence[-1] + sequence[-2])
    return sequence
        

print(fibonnaci_no_recursion(10))
# print(fibonacci_recursion(10))
print(get_fibonacci_sequence_recursion(10))