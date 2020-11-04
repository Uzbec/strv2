from . import ft_len as l


def ft_lshift_list(mass):
    for i in range(1, l.ft_len(mass)):
        mass[i - 1], mass[i] = mass[i], mass[i - 1]
    return mass
