empty_list = []
def sort_dictionary(providedDic: dict):
    age_sort= sorted(providedDic.items(), key=lambda x: x[1][1])
    
    for name, value in age_sort:
        empty_list.append((name, value[0]))
    return empty_list