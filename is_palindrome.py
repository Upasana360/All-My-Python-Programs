def is_palindrome(word):
    if word[0::1]==word[::-1]:
        return "palindrome"
    else:
        return "Not palindrome"
print(is_palindrome("madam"))
print(is_palindrome("mmmmm"))