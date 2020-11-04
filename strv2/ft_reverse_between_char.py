import ft_len as l
from . import ft_reverse_str as rev
from . import ft_slice_str as sl


def ft_reverse_between_char(char, str):
    svch = 0
    gpin = 0

    if char not in str:
        return -2
    else:
        pin = None
        flag = False
        for i in range(l.ft_len(str)):
            if not flag:
                if str[i] == char:
                    gpin = i
                    flag = True
            else:
                if str[i] == char:
                    pin = i
                    svch = i

        if not pin:
            return -1
        else:
            return rev.ft_reverse_str(sl.ft_slice_str(str, gpin + 1, svch + 1))
