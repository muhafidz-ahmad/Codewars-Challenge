def count_sel(lst):
    len_lst = len(lst)
    count_unique = len(set(lst))
    count_single_values = 0
    elements_max_occur = list()
    max_occur = 0
    for i in lst:
        count_value = lst.count(i)
        if count_value == 1:
            count_single_values += 1
        if count_value > max_occur:
            max_occur = count_value
            elements_max_occur = [i]
        elif (count_value == max_occur) and (elements_max_occur.count(i) == 0):
            elements_max_occur.append(i)
            elements_max_occur.sort()
    
    return [len_lst, count_unique, count_single_values, [elements_max_occur, max_occur]]
    