def ft_count_words(str):
    col = 1
    for i in str:
        if i == " ":
            col += 1
    return col
