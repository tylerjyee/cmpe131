from operator import itemgetter

def sort_tup(t_dict):
    res = sorted(t_dict.values(), key=itemgetter(1))
    return res

t_dict = {"Sam": (1234567, 20), "Peter": (5567823, 32), "Alex": (8907346, 25)}
d = sort_tup(t_dict)
print(d)