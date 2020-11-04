import ft_len as l


def ft_remove_str(str1, str2):
    sc = 0
    otv = ''
    for i in str1:
        if i in str2:
            sc += 1
        else:
            otv += i
    if l.ft_len(str1) == sc:
        return False
    else:
        return otv
