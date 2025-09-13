def find_duplicates(input: list)-> list:
    duplicates = []
    duplicate_count = convert_list_to_dict(input)

    for key, value in duplicate_count.items():
        if value > 1:
            duplicates.append(key)

    return duplicates

def convert_list_to_dict(input: list)-> dict:
    converted_dict = {}
    for i in input:
        if i in converted_dict:
            converted_dict[i] += 1
        else:
            converted_dict[i] = 1
    return converted_dict


def get_duplicates(input: list) -> list: #Optimised Solution
    seen = set()
    duplicates = set()

    for num in input:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)


input = [1, 2, 3, 2, 4, 5, 3, 6]
print(find_duplicates(input))
print(get_duplicates(input))