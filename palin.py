def palindrome(in_list):
    new_list = list(reversed(in_list))
    res = new_list == in_list
    return res
