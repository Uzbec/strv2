import ft_len as l


def ft_reverse_str(str):
    otv = ""
    for i in range(-1, -l.ft_len(str) - 1, -1):
        otv += str[i]
    return otv
