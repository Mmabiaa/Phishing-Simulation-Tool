def is_Palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False

word = input("Enter a word: ")
print(is_Palindrome(word))
