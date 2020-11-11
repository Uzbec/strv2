def ft_max_min_sum_count(lst):
    if not lst:
        return 0, 0, 0, 0, 0
    kol = 0
    max = lst[0]
    min = lst[0]
    sum = 0
    for i in lst:
        kol += 1
        sum += i
        if i > max:
            max = i
        if i < min:
            min = i

    if sum % kol == 0:
        srzn = sum // kol
    else:
        srzn = sum / kol
        srzn = int(srzn * 10) / 10
    return kol, max, min, sum, srzn
