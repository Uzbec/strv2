import ft_len as l


def ft_cut_between_char(char, str):
    svch = 0
    gpin = 0
    otv = ""
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
                return ""
            elif gpin == 0:
                for i in range(svch + 1, l.ft_len(str)):
                    otv += str[i]
            elif svch == l.ft_len(str) - 1:
                for i in range(gpin):
                    otv += str[i]
            else:
                for i in range(gpin):
                    otv += str[i]
                for i in range(svch + 1, l.ft_len(str)):
                    otv += str[i]
            return otv
