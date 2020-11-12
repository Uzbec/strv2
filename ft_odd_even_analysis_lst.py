from . import ft_odd_even_separator_lst as k
from . import ft_max_min_sum_count as mms


def ft_odd_even_analysis_lst(lst):
    ch = k.ft_odd_even_separator_lst(lst)[0]
    nech = k.ft_odd_even_separator_lst(lst)[1]
    s = mms.ft_max_min_sum_count(ch)[0]
    knech = mms.ft_max_min_sum_count(nech)[0]
    mch = mms.ft_max_min_sum_count(ch)[1]
    mnech = mms.ft_max_min_sum_count(nech)[1]
    mich = mms.ft_max_min_sum_count(ch)[2]
    minech = mms.ft_max_min_sum_count(nech)[2]
    sch = mms.ft_max_min_sum_count(ch)[3]
    snch = mms.ft_max_min_sum_count(nech)[3]
    otv = f"""Анализ списка:
Количество четных чисел: {s},\t\tКоличество нечетных чисел: {knech}
Максимальная четная цифра: {mch},\t\tМаксимальная нечетная цифра: {mnech},
Минимальная четная цифра: {mich},\t\tМинимальная нечетная цифра: {minech},
Сумма четных чисел: {sch},\t\tСумма нечетных чисел: {snch},"""
    print(otv)
