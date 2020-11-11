from . import ft_len as l


def ft_sum_even_lst(lst):
    otv = 0
    for i in range(0, l.ft_len(lst), 2):
        otv += lst[i]
    return otv
