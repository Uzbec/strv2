from . import ft_len as l


def ft_find_char(char, str):
    if char not in str:
        return False
    else:
        fin = None
        pin = None
        flag = False
        for i in range(l.ft_len(str)):
            if not flag:
                if str[i] == char:
                    fin = i
                    flag = True
            else:
                if str[i] == char:
                    pin = i
        if not pin:
            return fin
        else:
            return fin, pin
