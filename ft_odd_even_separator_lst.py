def ft_odd_even_separator_lst(lst):
    nech = []
    ch = []
    for i in lst:
        if i % 2 == 0:
            ch.append(i)
        else:
            nech.append(i)
    return [ch, nech]
