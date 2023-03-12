def sort_dictionary(dict):
    tup = list(dict.values())
    tup.sort(key = lambda x: x[1])
    sorted_dict = {i: dict[i] for i in tup}
    return sorted_dict

dict = {"Sam": (1234567, 20), "Peter": (4567823, 32), "Alex": (8907346, 25)}
d = sort_dictionary(dict)
print(d)