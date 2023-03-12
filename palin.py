def palindrome(word):
    word == word[::-1]
    if word:
        print("true")
    else:
        print("false")
check_word = "racecar"
palindrome(check_word)