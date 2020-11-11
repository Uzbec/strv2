from . import ft_len as l


def ft_join(lst, *args):
    sp = ""
    if not args:
        sep = " "
    else:
        sep = args[0]
    for i in range(l.ft_len(lst) - 1):
        sp += (lst[i] + sep)
    sp += lst[-1]
    return sp
