def palindrome(test_list):
    rev_list = list(reversed(test_list))
    res = rev_list == test_list
    return res
