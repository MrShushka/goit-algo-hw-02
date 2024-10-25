from collections import deque

def is_palindrome(s: str) -> bool:
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    char_deque = deque(cleaned_string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  

    return True  

print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("Hello"))  # False