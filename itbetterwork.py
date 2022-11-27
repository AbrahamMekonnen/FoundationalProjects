def nearest_value(values: set, one: int) -> int:
    
    my_list = list(values)
    my_list.sort()
    near_value = []
    for i in range(len(my_list)):
        near_value.append(abs(my_list[i] - one))
    min_val = near_value.index(min(near_value))
    
    return my_list[min_val]

print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
