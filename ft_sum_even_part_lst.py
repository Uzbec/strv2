def ft_sum_even_part_lst(lst):
    otv = 0
    for i in lst:
        if i % 2 == 0:
            otv += i
    return otv
