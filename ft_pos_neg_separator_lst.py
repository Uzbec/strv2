def ft_pos_neg_separator_lst(lst):
    pos = []
    n = []
    neg = []
    for i in lst:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
        else:
            n.append(i)
    return [neg, n, pos]
