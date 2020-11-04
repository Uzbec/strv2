from . import ft_lshift_list as l
from . import ft_rshift_list as r


def ft_super_shift_list(mass, n):
    if n > 0:
        for i in range(n):
            mass = r.ft_rshift_list(mass)
    elif n < 0:
        for i in range(-n):
            mass = l.ft_lshift_list(mass)
    return mass
