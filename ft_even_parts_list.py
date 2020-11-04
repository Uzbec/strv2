from . import ft_len as l


def ft_even_parts_list(mass):
    return [mass[i] for i in range(1, l.ft_len(mass), 2)]
