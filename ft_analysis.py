def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_analysis(str):
    print(str[2])
    print(str[-2])
    print(str[0] + str[1] + str[2] + str[3] + str[4])
    for i in range(ft_len(str) - 2):
        print(str[i], end="")
    print(end="\n")
    for i in range(0, ft_len(str), 2):
        print(str[i], end="")
    print(end="\n")
    for i in range(1, ft_len(str), 2):
        print(str[i], end="")
    print(end="\n")
    for i in range(ft_len(str) - 1, -1, -1):
        print(str[i], end="")
    print(end="\n")
    for i in range(ft_len(str) - 1, -1, -2):
        print(str[i], end="")
    print(end="\n")
    print(ft_len(str))
