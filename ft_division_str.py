from . import ft_len as l


def ft_division_str(str):
    nacstr = ""
    konstr = ""
    if l.ft_len(str) % 2 == 0:
        for i in range(l.ft_len(str) // 2):
            nacstr += str[i]
        for i in range(l.ft_len(str) // 2, l.ft_len(str)):
            konstr += str[i]
    else:
        for i in range(l.ft_len(str) // 2 + 1):
            nacstr += str[i]
        for i in range(l.ft_len(str) // 2 + 1, l.ft_len(str)):
            konstr += str[i]
    return konstr + nacstr
