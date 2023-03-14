from operator import itemgetter
t_dict = {"Sam": (1234567, 20), "Peter": (5567823, 32), "Alex": (8907346, 25)}

def sort_tup(t_dict):
    res = sorted(t_dict.values(), key=itemgetter(1))

print(sort_tup(t_dict))

