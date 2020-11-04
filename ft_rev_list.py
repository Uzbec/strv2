import ft_len as l


def ft_rev_list(mass):
    for i in range(l.ft_len(mass) // 2):
        mass[i], mass[-i - 1] = mass[-i - 1], mass[i]
    return mass
