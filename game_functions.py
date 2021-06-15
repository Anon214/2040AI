def left_stack(my_list):
    for elem in my_list:
        j = 0
        for i in range(3):
            i += 1
            if elem[i] != 0:
                while i > j and elem[j] != 0:
                    j += 1

                if i != j:
                    elem[j] = elem[i]
                    elem[i] = 0

    return my_list


# Check if getting rid of zeros and adding them with numpy has better performance


def right_stack(my_list):
    for elem in my_list:
        j = 3
        k = 2
        for i in range(3):
            if elem[k] != 0:
                while elem[j] != 0 and k < j:
                    j -= 1

                if k != j:
                    elem[j] = elem[k]
                    elem[k] = 0
            k -= 1

    return my_list


# Need to learn numpy array and then implement removing zeros then adding based on stack direction
# Use a while loop with i += 1 to find the earliest number


def up_stack(my_list):
    k = 0
    for i in range(4):
        for j in range(4):
            if my_list[j][i] != 0:
                while my_list[k][i] != 0 and j > k:
                    k += 1

                if k != j:
                    my_list[k][i] = my_list[j][i]
                    my_list[j][i] = 0

    return my_list


def down_stack(my_list):
    t = 3
    for i in range(4):
        k = 3
        for j in range(4):
            if my_list[k][i] != 0:
                while my_list[t][i] != 0 and t > k:
                    t -= 1
                if k != t:
                    my_list[t][i] = my_list[k][i]
                    my_list[k][i] = 0
            k -= 1

    return my_list






