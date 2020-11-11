def ft_rmstrchar(str, less):
    otv = ""
    for i in str:
        if i in less:
            continue
        else:
            otv += i
    return otv
