import ft_len as l
from . import ft_slice_str as sl


def ft_change_str(str1, str2, str3):
    if str1 not in str3:
        return False
    else:
        for i in range(l.ft_len(str3)):
            if sl.ft_slice_str(str3, i + 1, i + l.ft_len(str1)) == str1:
                str3 = sl.ft_slice_str(str3, 1, i) + str2 + sl.ft_slice_str(
                    str3, i + l.ft_len(str1) + 1, l.ft_len(str3))

        return str3
