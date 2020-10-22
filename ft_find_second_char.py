import ft_len as l


def ft_find_second_char(char, str):
    if char not in str:
        return -2
    else:
        pin = None
        flag = False
        for i in range(l.ft_len(str)):
            if not flag:
                if str[i] == char:
                    flag = True
            else:
                if str[i] == char:
                    pin = i
        if not pin:
            return -1
        else:
            pin = None
            flag = False
            for i in range(l.ft_len(str)):
                if not flag:
                    if str[i] == char:
                        flag = True
                else:
                    if str[i] == char:
                        pin = i
                        break
            return pin
