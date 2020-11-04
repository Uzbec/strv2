from . import ft_len as l


def ft_rshift_list(mass):
    for i in range(-1, -l.ft_len(mass), -1):
        mass[i], mass[i - 1] = mass[i - 1], mass[i]
    return mass
