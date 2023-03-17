def sort_dictionary(dictionary):
    empty_list = []
    age_sort= sorted(dictionary.items(), key=lambda x: x[1][1])
    for name, value in age_sort:
        empty_list.append((name, value[0]))
    return empty_list
