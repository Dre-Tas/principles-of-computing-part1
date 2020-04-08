def format(t):
    a = (t // 600)
    b = (((t % 600) / 10) / 10)
    c = '0'
    if (t > 10):
        c = str(t)[(-2)]
    d = str(t)[(-1)]
    formatedTime = (((((str(a) + ':') + str(b)) + c) + '.') + d)
    return formatedTime

print format(1899)
