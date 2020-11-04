from . import ft_len as l


def ft_rev_par_list(mass):
    if l.ft_len(mass) % 2 == 0:
        for i in range(0, l.ft_len(mass), 2):
            mass[i], mass[i + 1] = mass[i + 1], mass[i]
        return mass
    else:
        for i in range(0, l.ft_len(mass) - 1, 2):
            mass[i], mass[i + 1] = mass[i + 1], mass[i]
        return mass
