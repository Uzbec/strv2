import ft_len as l


def ft_count_words(str):
    otv = 0
    i = 0
    if str[0] == ' ':
        while i < l.ft_len(str):
            if str[i] == ' ' and str[i - 1] != ' ':
                otv += 1
            i += 1
        return otv
    else:
        while i < l.ft_len(str):
            if str[i] == ' ' and str[i - 1] != ' ':
                otv += 1
            i += 1
        return otv + 1
