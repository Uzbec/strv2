from . import ft_len as l


def ft_same_parts_list(mass):
    for i in range(1, l.ft_len(mass)):
        if (mass[i - 1] > 0 and mass[i] > 0) or (
                mass[i - 1] < 0 and mass[i] < 0):
            return True
    return False
