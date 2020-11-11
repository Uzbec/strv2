from . import ft_odd_even_separator_lst as k
from . import ft_max_min_sum_count as mms


def ft_odd_even_analysis_lst(lst):
    ch = k.ft_odd_even_separator_lst(lst)[0]
    nech = k.ft_odd_even_separator_lst(lst)[1]
    kch = mms.ft_max_min_sum_count(ch)[0]
    knech = mms.ft_max_min_sum_count(nech)[0]
    mch = mms.ft_max_min_sum_count(ch)[1]
    mnech = mms.ft_max_min_sum_count(nech)[1]
    mich = mms.ft_max_min_sum_count(ch)[2]
    minech = mms.ft_max_min_sum_count(nech)[2]
    sch = mms.ft_max_min_sum_count(ch)[3]
    snch = mms.ft_max_min_sum_count(nech)[3]
    kt1 = 2
    kt2 = 2
    kt3 = 2
    kt4 = 2

    otv = "Анализ списка:\n" + f"Количество четных чисел: {kch}," + "\t" * \
          kt1 \
          + f"Количество нечетных чисел: {knech}\n" + \
          f"Максимальная четная " f"цифра: {mch}," + "\t" \
          * kt2 + f"Максимальная нечетная цифра: {mnech},\n" + \
          f"Минимальная четная цифра: {mich}," + "\t" \
          * kt3 + f"Минимальная нечетная цифра: {minech},\n" + \
          f"Сумма четных чисел: {sch}," + "\t" * kt4 + \
          f"Сумма нечетных чисел: {snch},"
    print(otv)
