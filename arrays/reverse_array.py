#Reverse using new array
def reverse_array_with_new_array(input: list) -> list:
    reversed_array = []

    for i in range(len(input) - 1, -1, -1):
        reversed_array.append(input[i])

    return reversed_array 

def reverse_array_without_new_array(input: list) -> list:
    left = 0
    right = len(input) - 1

    while(left < right):
            temp = input[left]
            input[left] = input[right]
            input[right] = temp

            left+= 1
            right -= 1

    return input

input = [10, 20, 30, 40, 50]
# print(reverse_array_with_new_array(input))
print(reverse_array_without_new_array(input))