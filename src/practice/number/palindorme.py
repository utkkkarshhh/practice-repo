def if_palindrome(num: int) -> bool:
    original = str(num)
    start = 0
    end = len(original) - 1
    
    while start <= end:
        if original[start] == original[end]:
            start += 1
            end -= 1
        else: return False
        
    return True

print(if_palindrome(2122))
