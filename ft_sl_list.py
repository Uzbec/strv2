import ft_len as l


def ft_sl_list(mass):
    kol = 0
    for i in range(1, l.ft_len(mass)):
        if mass[i - 1] < mass[i]:
            kol += 1
    return kol
