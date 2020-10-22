from . import ft_len as l


def ft_change_place_word(str):
    fstr = ""
    sstr = ""
    flag = False
    for i in range(l.ft_len(str)):
        if str[i] == " ":
            for j in range(i + 1, l.ft_len(str)):
                sstr += str[j]
            break
        else:
            fstr += str[i]

    return sstr + " " + fstr
