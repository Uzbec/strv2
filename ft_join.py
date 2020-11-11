from . import ft_len as l


def ft_join(lst, sep):
    sp = ""
    if not sep:
        sep = " "
    for i in range(l.ft_len(lst) - 1):
        sp += (lst[i] + sep)
    sp += lst[-1]
    return sp
