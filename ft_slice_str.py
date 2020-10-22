from . import ft_len as l


def ft_slice_str(str, start, end):
    otv = ""
    if end > l.ft_len(str):
        for i in range(start - 1, l.ft_len(str)):
            otv += str[i]
        return otv
    for i in range(start - 1, end):
        otv += str[i]
    return otv
