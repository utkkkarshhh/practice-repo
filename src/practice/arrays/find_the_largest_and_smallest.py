def find_the_largest(input: list) -> int:
    largest = input[0]

    for i in range(0, len(input) - 1):
        if input[i] > largest:
            largest = input[i]
        
    return largest

def find_the_smallest(input: list) -> int:
    smallest = input[0]

    for i in range(1, len(input)):
        if input[i] < smallest:
            smallest = input[i]

    return smallest

input = [3, 7, 1, 9, 4, 2]
print(find_the_largest(input))
print(find_the_smallest(input))