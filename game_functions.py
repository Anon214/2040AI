def right_stack(my_list):
    new_list = []
    for elem in my_list:
        for i in range(3):
            if elem[i] != 0 and elem[i + 1] == 0:
                elem[i + 1] = elem[i]
                elem[i] = 0
        new_list.append(elem)
    return new_list
