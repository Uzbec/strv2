from . import ft_len as l


def ft_even_index_list(mass):
    return [mass[i] for i in range(0, l.ft_len(mass), 2)]
