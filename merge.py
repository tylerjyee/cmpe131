list1 = [1, 2, 4, 5]
list2 = [1, 3, 5, 7]
def merge(list1, list2):
    res = sorted(list1 + list2)
    return res

result= merge(list1, list2)
print(result)