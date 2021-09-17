def unique_numbers(listn):
    unique = False

    num = len(listn)

    num_set = len(set(listn))

    if(num==num_set):
        unique = True
    else:
        unique = False

    return unique



print(unique_numbers([1,3]))


