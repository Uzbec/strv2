from . import ft_len as l


def ft_analysis(str):
    print(str[2])
    print(str[-2])
    print(str[0] + str[1] + str[2] + str[3] + str[4])
    for i in range(l.ft_len(str) - 2):
        print(str[i], end="")
    print(end="\n")
    for i in range(0, l.ft_len(str), 2):
        print(str[i], end="")
    print(end="\n")
    for i in range(1, l.ft_len(str), 2):
        print(str[i], end="")
    print(end="\n")
    for i in range(l.ft_len(str) - 1, -1, -1):
        print(str[i], end="")
    print(end="\n")
    for i in range(l.ft_len(str) - 1, -1, -2):
        print(str[i], end="")
    print(end="\n")
    print(l.ft_len(str))
