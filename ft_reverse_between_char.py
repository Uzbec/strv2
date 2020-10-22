import ft_len as l
import ft_reverse_str as rev
import ft_slice_str as sl


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
            if gpin == 0 and svch == l.ft_len(str) - 1:
                return rev.ft_reverse_str(str)
            elif gpin == 0:
                return rev.ft_reverse_str(sl.ft_slice_str(str, 1, svch + 1)) \
                       + sl.ft_slice_str(str, svch + 2, l.ft_len(str))

            elif svch == l.ft_len(str) - 1:
                return sl.ft_slice_str(str, 1, gpin) + rev.ft_reverse_str(
                    sl.ft_slice_str(str, gpin + 1, l.ft_len(str)))
            else:
                nac = ""
                con = ""
                for i in range(gpin):
                    nac += str[i]
                for i in range(svch + 1, l.ft_len(str)):
                    con += str[i]
                return nac + rev.ft_reverse_str(sl.ft_slice_str(str, gpin + 1,
                                                                svch + 1)) + \
                       con
