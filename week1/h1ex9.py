def appendsums(lst): 
    """ 
    Repeatedly append the sum of the current last three elements 
    of lst to lst. 
    """

    appended_lst = lst

    for i in range(25):
        last_three = lst[-3:]
        sum_three = sum(last_three)
        appended_lst.append(sum_three)

    return appended_lst

sum_three = [0, 1, 2]
appendsums(sum_three)
print(sum_three[10])
print(sum_three[20])